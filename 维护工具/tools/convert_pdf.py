#!/usr/bin/env python3
"""按字形、字体及页面坐标转换登记底本；保留已人工校订的第 18 章。"""
import argparse, collections, hashlib, html, json, re
from pathlib import Path
import fitz

ROOT=Path(__file__).resolve().parents[2]
CIRCLES='①②③④⑤⑥⑦⑧⑨⑩'
def dump(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def plain(s):
    return re.sub(r'\s+',' ',s).strip()
def compact(s):
    return re.sub(r'\s+','',s)
def union(rects):
    r=fitz.Rect(rects[0])
    for b in rects[1:]:r|=fitz.Rect(b)
    return r
def inside(b,r):
    b=fitz.Rect(b);r=fitz.Rect(r)
    return r.contains(fitz.Point((b.x0+b.x1)/2,(b.y0+b.y1)/2))
def esc(s):
    s=html.escape(s,quote=False)
    return re.sub(r'([\\*_`])',r'\\\1',s)
def join(a,b):
    if not a:return b
    if re.search(r'[A-Za-z0-9]$',a) and re.match(r'[A-Za-z0-9]',b):return a+' '+b
    return a+b

class Converter:
    def __init__(self,pdf):
        self.source=json.loads((ROOT/'维护工具/source-map.json').read_text())
        if hashlib.sha256(pdf.read_bytes()).hexdigest()!=self.source['sha256']:raise SystemExit('底本 SHA256 不匹配')
        self.doc=fitz.open(pdf)
        self.fonts=json.loads((ROOT/'维护工具/font-map.json').read_text())['glyphs']
        self.layout_overrides=json.loads((ROOT/'维护工具/layout-overrides.json').read_text())
        self.assets=json.loads((ROOT/'维护工具/asset-map.json').read_text())
        self.assets=[a for a in self.assets if a['path'].startswith('第18章-')]
        self.audit=[];self.corrections=[];self.footnotes={};self.references=set()
        self.old=next(c for c in json.loads((ROOT/'维护工具/reading-order.json').read_text())['chapters'] if c['id']=='18')
    def lines(self,page):
        fm={f[3].split('+')[-1]:f[0] for f in page.get_fonts()}
        fixed={}
        for span in page.get_texttrace():
            fid=fm.get(span['font'])
            for code,gid,origin,bbox in span['chars']:
                replacement=self.fonts.get(f'{fid}:{gid}')
                if replacement and replacement!=chr(code):
                    fixed[(round(origin[0],2),round(origin[1],2),chr(code))]=replacement
        lines=[]
        for block in page.get_text('rawdict')['blocks']:
            if block['type']!=0:continue
            for line in block['lines']:
                spans=[]
                for s in line['spans']:
                    text=''
                    for ch in s['chars']:
                        k=(round(ch['origin'][0],2),round(ch['origin'][1],2),ch['c'])
                        value=fixed.get(k,ch['c']);text+=value
                        if value!=ch['c']:self.corrections.append({'pdf_page':page.number+1,'from':ch['c'],'to':value,'origin':list(ch['origin'])})
                    if not text.strip():continue
                    spans.append({**{k:s[k] for k in ['bbox','origin','font','size','flags']},'text':text})
                if not spans:continue
                box=list(union([s['bbox'] for s in spans]))
                if box[1]<62 or box[1]>682:continue
                text=''.join(s['text'] for s in spans)
                lines.append({'spans':spans,'bbox':box,'text':text,'page':page.number+1})
        # PDF 经常把代码行号与代码、行内上下标分成独立行。按基线合并。
        lines.sort(key=lambda l:(round(l['bbox'][1]),l['bbox'][0]))
        rows=[]
        for line in lines:
            y=max(s['origin'][1] for s in line['spans'] if s['size']>=max(t['size'] for t in line['spans'])-.2)
            candidates=[r for r in rows[-5:] if abs(r['baseline']-y)<2.5
                        and abs(max(s['size'] for s in r['spans'])-max(s['size'] for s in line['spans']))<1.1]
            row=candidates[-1] if candidates else None
            if row:
                row['spans']+=line['spans'];row['spans'].sort(key=lambda s:s['bbox'][0]);row['bbox']=list(union([row['bbox'],line['bbox']]))
                row['text']=''.join(s['text'] for s in row['spans'])
            else: rows.append({**line,'baseline':y})
        # 单独抽出的上标/脚注符号应归回相邻正文行，而不是成为新段落。
        for small in list(rows):
            if max(s['size'] for s in small['spans'])>=7.4:continue
            candidates=[r for r in rows if r is not small and max(s['size'] for s in r['spans'])>=9
                        and r['bbox'][0]-2<=small['bbox'][0]<=r['bbox'][2]+7
                        and r['bbox'][1]-3<=small['bbox'][1]<r['bbox'][3]]
            if candidates:
                r=min(candidates,key=lambda r:abs(r['bbox'][1]-small['bbox'][1]))
                r['spans']+=small['spans'];r['spans'].sort(key=lambda s:s['bbox'][0]);r['bbox']=list(union([r['bbox'],small['bbox']]))
                r['text']=''.join(s['text'] for s in r['spans']);rows.remove(small)
        rows.sort(key=lambda l:(l['bbox'][1],l['bbox'][0]))
        for i,l in enumerate(rows):
            l['id']=f'p{page.number+1}-l{i+1}'
            l['size']=max(s['size'] for s in l['spans'])
            l['fonts']={s['font'] for s in l['spans']}
        return rows
    def inline(self,l,foot=False):
        result='';base=l['size'];baseline=l['baseline']
        for s in l['spans']:
            t=s['text'];value=''
            for ch in t:
                if ch in CIRCLES and not foot:
                    key=f'p{l["page"]}-{CIRCLES.index(ch)+1}'
                    self.references.add(key);value+=f'[^{key}]'
                else:value+=esc(ch)
            if s['size']<base*.82 and t.strip() and not any(c in t for c in CIRCLES):
                dy=s['origin'][1]-baseline
                if dy<-1:value='<sup>'+value.strip()+'</sup>'
                elif dy>1:value='<sub>'+value.strip()+'</sub>'
            result+=value
        return plain(result)
    def asset(self,page,rect,directory,name,kind,alt,xref=None):
        path=ROOT/directory/'assets'/f'p{page.number+1:03}-{name}.png'
        path.parent.mkdir(parents=True,exist_ok=True)
        if xref:
            data=self.doc.extract_image(xref)
            path=path.with_suffix('.'+data['ext']);path.write_bytes(data['image'])
            w,h=data['width'],data['height']
        else:
            pix=page.get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=fitz.Rect(rect),alpha=False)
            pix.save(path);w,h=pix.width,pix.height
        self.assets.append({'path':path.relative_to(ROOT).as_posix(),'pdf_page':page.number+1,'printed_page':page.number-17 if page.number>=18 else None,'kind':kind,'bbox':[round(v,2) for v in rect],'xref':xref,'width':w,'height':h,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        return f'![{plain(alt).replace("[","（").replace("]","）")}](../assets/{path.name})'
    def page_events(self,page,directory):
        lines=self.lines(page);events=[];taken=set();areas=[]
        def take(ls):taken.update(l['id'] for l in ls)
        def event(kind,text,ls,bbox=None,**extra):
            box=list(bbox or union([l['bbox'] for l in ls]));take(ls)
            events.append({'kind':kind,'text':text,'page':page.number+1,'bbox':box,'line_ids':[l['id'] for l in ls],**extra})
        # 原图在 PDF 中按资源提取；图题仍可搜索。
        image_groups=[]
        for info in page.get_image_info(xrefs=True):
            hit=[g for g in image_groups if (fitz.Rect(g['bbox'])+(-1,-1,1,1)).intersects(fitz.Rect(info['bbox']))]
            if hit:
                box=union([info['bbox']]+[g['bbox'] for g in hit])
                for g in hit:image_groups.remove(g)
                image_groups.append({'bbox':list(box),'xref':None})
            else:image_groups.append(info)
        for i,info in enumerate(image_groups):
            box=info['bbox']
            if box[1]>690 or box[3]<62:continue
            cap=[l for l in lines if l['id'] not in taken and re.match(r'^图\s*\d+\.\d+',plain(l['text'])) and 0<=l['bbox'][1]-box[3]<22]
            label=plain(cap[0]['text']) if cap else f'原书第 {page.number-17} 页图示 {i+1}'
            text=self.asset(page,box,directory,f'image-{i+1}','original_image',label,info.get('xref') or None)
            event('image',text,cap[:1],box);areas.append(box)
        # 表格检测也会识别灰色补充栏，按楷体排除这类假表格。
        for i,table in enumerate(page.find_tables().tables):
            box=table.bbox;ls=[l for l in lines if inside(l['bbox'],box)]
            if not ls or any('FZKTJW--GB1-0' in l['fonts'] for l in ls) or any(fitz.Rect(box).intersects(fitz.Rect(a)) for a in areas):continue
            if table.col_count<2 or table.row_count<2:continue
            cap=[l for l in lines if re.match(r'^表\s*\d+\.\d+',plain(l['text'])) and 0<=box[1]-l['bbox'][3]<25]
            label=plain(cap[0]['text']) if cap else f'原书第 {page.number-17} 页表格 {i+1}'
            # 复杂合并单元格保留版面，同时提供可搜索、可复制的文字表。
            cells=[]
            for row in table.rows:
                vals=[]
                for cell in row.cells:
                    if cell is None:vals.append('');continue
                    cl=[l for l in ls if inside(l['bbox'],cell)]
                    # 单行可能横跨多个单元格，按 span 中点选择。
                    parts=[]
                    for l in ls:
                        ss=[s for s in l['spans'] if inside(s['bbox'],cell)]
                        if ss:parts.append(plain(''.join(s['text'] for s in ss)))
                    vals.append(esc(' '.join(parts)).replace('|','&#124;'))
                cells.append(vals)
            raw='\n'.join('| '+' | '.join(row)+' |' for row in cells[:1])+ '\n| '+ ' | '.join(['---']*table.col_count)+' |\n'+'\n'.join('| '+' | '.join(row)+' |' for row in cells[1:])
            text=self.asset(page,box,directory,f'table-{i+1}','table_facsimile',label)
            text+='\n\n<details markdown="1">\n<summary>表格文字</summary>\n\n'+raw+'\n\n</details>'
            event('table',text,ls+cap[:1],box);areas.append(box)
        # 注脚由页面底部短横线界定，避免把小字号代码当脚注。
        dividers=[d['rect'].y0 for d in page.get_drawings() if 40<d['rect'].x0<65 and 70<d['rect'].width<110 and d['rect'].height<1.5 and d['rect'].y0>500]
        foot_y=min(dividers) if dividers else 1000
        footlines=[l for l in lines if l['bbox'][1]>foot_y and l['size']<=8]
        key=None
        for l in footlines:
            t=self.inline(l,True)
            if t and t[0] in CIRCLES:
                key=f'p{page.number+1}-{CIRCLES.index(t[0])+1}';t=t[1:].strip()
                self.footnotes[key]=''
            if key:self.footnotes[key]=join(self.footnotes[key],t)
            else:event('footnote_continuation',t,[l])
            take([l])
        # 逐块核过的复杂公式/行内分式覆盖自动几何识别，保证裁切完整。
        for i,region in enumerate(self.layout_overrides.get(str(page.number+1),[])):
            box=region['bbox'];ls=[l for l in lines if l['id'] not in taken and inside(l['bbox'],box)]
            text=region.get('markdown')
            if text is None:text=self.asset(page,box,directory,f'math-reviewed-{i+1}','formula_facsimile',region['label'])
            event('raw',text,ls,box);areas.append(box)
        # 独立公式按整块裁取；保留分数、上下标及原编号的相对位置。
        formula=[]
        for l in lines:
            if str(page.number+1) in self.layout_overrides:break
            if l['id'] in taken or l['bbox'][1]>foot_y:continue
            t=plain(l['text']);fonts=l['fonts'];x=l['bbox'][0]
            if x>100 and l['size']<=11 and not any('Courier' in f or 'FZKT' in f or 'FZHT' in f for f in fonts) and re.search(r'[=∑∏÷]',t) and not re.match(r'[图表]\s*\d',t):
                if len(re.findall(r'[\u4e00-\u9fff]',t))<18:formula.append(l['bbox'])
        for d in page.get_drawings():
            if str(page.number+1) in self.layout_overrides:break
            r=d['rect']
            if d['type']=='s' and r.height<2 and 5<r.width<200 and 85<r.x0<400 and 65<r.y0<680 and not any(fitz.Rect(a).intersects(r+(-1,-1,1,1)) for a in areas):
                formula.append([r.x0-12,r.y0-18,r.x1+15,r.y1+18])
        merged=[]
        for r in formula:
            hit=next((i for i,a in enumerate(merged) if fitz.Rect(a).intersects(fitz.Rect(r))),None)
            if hit is None:merged.append(r)
            else:merged[hit]=list(union([merged[hit],r]))
        for i,box in enumerate(merged):
            ls=[l for l in lines if l['id'] not in taken and l['bbox'][1]<box[3]+2 and l['bbox'][3]>box[1]-2 and l['bbox'][0]>90 and l['size']<=11 and not any('Courier' in f or 'FZKT' in f for f in l['fonts'])]
            if not ls:continue
            box=list(union([box]+[l['bbox'] for l in ls]));box=[box[0]-3,box[1]-3,box[2]+3,box[3]+3]
            if any(fitz.Rect(box).intersects(fitz.Rect(a)) for a in areas):continue
            label=f'原书第 {page.number-17} 页公式 {i+1}'
            text=self.asset(page,box,directory,f'formula-{i+1}','formula_facsimile',label)
            event('formula',text,ls,box);areas.append(box)
        for l in lines:
            if l['id'] in taken:continue
            t=plain(l['text']);fonts=l['fonts'];size=l['size']
            if size>=20 and page.number>=18:kind='chapter'
            elif (any('FZLBJW' in f for f in fonts) and size>=14) or (t in ['参考资料','作业','作业（模拟）','作业（代码）'] and size>=12):kind='heading'
            elif any('FZZDXJW' in f for f in fonts) and size>=11:kind='subheading'
            elif any('Courier' in f for f in fonts):kind='code'
            elif any('FZKTJW' in f for f in fonts):kind='quote'
            elif any('FZHTJW' in f for f in fonts) and size<10 and re.match(r'^(关键|补充|提示|深入|小结|注意|要点)',t):kind='quote_title'
            elif re.match(r'^[图表]\s*\d+\.\d+',t) and size<=9.6:kind='caption'
            else:kind='text'
            if kind=='code':
                ss=l['spans'];x=min(s['bbox'][0] for s in ss);parts='';end=x
                for s in ss:
                    parts+=' '*max(0,round((s['bbox'][0]-end)/4.5))+s['text'];end=s['bbox'][2]
                t=parts.rstrip()
            elif kind in ('heading','chapter','subheading'):t=plain(l['text'])
            else:t=self.inline(l)
            event(kind,t,[l],indent=l['bbox'][0],size=size)
        self.audit.append({'pdf_page':page.number+1,'source_lines':len(lines),'source_chars':sum(len(compact(l['text'])) for l in lines),'represented_lines':len(taken),'footnote_lines':len(footlines),'events':[{k:e[k] for k in ['kind','bbox','line_ids']} for e in events]})
        return sorted(events,key=lambda e:(e['bbox'][1],e['bbox'][0]))
    def render(self,events,references=False):
        out=[];para='';pk=None;prev=None;code=[]
        def flush():
            nonlocal para,pk,code
            if para:out.append(('> ' if pk=='quote' else '')+para);para='';pk=None
            if code:
                numbered=sum(bool(re.match(r'^\d+\s',t)) for t in code)>=len(code)*.65
                if numbered:code=[t[5:] if len(t)>=5 else '' for t in code]
                language='c' if any(re.search(r'#include|int |void |pthread_|sem_|struct ',t) for t in code) else 'text'
                out.append('```'+language+'\n'+'\n'.join(code)+'\n```');code=[]
        for e in events:
            kind,t=e['kind'],e['text']
            if kind=='chapter':continue
            if kind=='code':
                if para:flush()
                if prev and prev['kind']=='code' and e['page']==prev['page'] and e['bbox'][1]-prev['bbox'][3]>19:flush()
                code.append(t);prev=e;continue
            if code:flush()
            if kind in ('image','table','formula','raw','caption','subheading','quote_title','heading'):
                flush()
                if kind=='subheading':t='## '+t
                elif kind=='heading':t='## '+t
                elif kind=='quote_title':t='> **'+t+'**'
                elif kind=='caption':t='*'+t+'*'
                out.append(t);prev=e;continue
            k='quote' if kind=='quote' else 'text'
            indent=e.get('indent',55)
            new=pk!=k or indent>=72 or re.match(r'^(?:\d+[.．、](?!\d)\s*|[●•]|[—−]\s)',t) or (references and re.match(r'^\[[^\^].+?\]',t))
            if prev and prev['page']==e['page'] and e['bbox'][1]-prev['bbox'][3]>12:new=True
            if new:flush()
            pk=k;para=join(para,t);prev=e
        flush()
        text='\n\n'.join(out)
        # 引用栏每个自然段保持独立，跨页正文以坐标和缩进判定是否续行。
        return text+'\n'
    def run(self):
        chapters=[];front=[]
        for unit in self.source['units']:
            if unit.get('chapter')==18:
                self.old.update(kind='chapter',part='第一部分 · 虚拟化',status='proofread')
                chapters.append(self.old);unit['status']='proofread';continue
            title=plain(unit['title']);first,last=unit['pdf_pages'];kind=unit['kind']
            if kind=='chapter':
                ident=str(unit['chapter']);title=re.sub(r'^第(\d+)章\s*',r'第 \1 章 ',title)
                short=re.sub(r'^第 \d+ 章 ','',title)
                directory='第'+ident.zfill(2)+'章-'+re.sub(r'[^\w\u4e00-\u9fff-]','',short)
            elif kind=='appendix':
                ident=re.match(r'附录([A-G])',title)[1];directory='附录'+ident+'-'+re.sub(r'[^\w\u4e00-\u9fff-]','',title.split(' ',1)[-1]);title=re.sub(r'^附录([A-G])\s*',r'附录 \1 ',title)
                if ident=='G':title=title.replace('vx6','xv6');directory=directory.replace('vx6','xv6')
            else:
                ident='front-'+str(first);directory='书前与导语/'+title.replace(' ','-');front.append({'id':ident,'title':title,'directory':directory})
            if kind=='front_matter' and (first<=3 or first==13):
                unit['status']='local_reference_only'
                self.audit.extend({'pdf_page':pno,'representation':'local_reference_only'} for pno in range(first,last+1))
                continue
            (ROOT/directory/'sections').mkdir(parents=True,exist_ok=True)
            events=[]
            for pno in range(first,last+1):
                if kind=='front_matter' and first in (35,213,319):
                    events.append({'kind':'raw','text':'[全书目录](../../../目录.md)','page':pno,'bbox':[0,0,524,700]})
                    self.audit.append({'pdf_page':pno,'representation':'part_navigation'})
                else:events+=self.page_events(self.doc[pno-1],directory)
            # 以可见大号标题为准切小节，避免 PDF 书签错字和页码粒度丢失。
            sections=[];buf=[];current=title;start=first;index=0
            def save(end):
                nonlocal index,buf,start,current
                if not buf:return
                slug='introduction' if current==title else re.match(r'^(\d+\.\d+|[A-G]\.\d+)',current)
                slug=slug[0] if hasattr(slug,'group') else slug
                if not slug:slug='references' if current.startswith('参考') else 'homework' if current.startswith('作业') else f'section-{index}'
                name=f'sections/{slug}.md'
                if any(s['path']==name for s in sections):name=f'sections/{slug}-{index}.md'
                body=self.render(buf,references=current.startswith('参考'))
                refs=set(re.findall(r'\[\^(p\d+-\d+)\]',body))
                for key in sorted(refs):
                    if key in self.footnotes:body+='\n[^'+key+']: '+self.footnotes[key]+'\n'
                (ROOT/directory/name).write_text('# '+current+'\n\n'+body)
                sections.append({'path':name,'title':current,'pdf_pages':[start,end]});buf=[];index+=1
            for e in events:
                if e['kind'] not in ('image','raw') and compact(e['text'])==compact(title):continue
                if e['kind']=='heading':
                    save(buf[-1]['page'] if buf else start);current=e['text'];start=e['page']
                elif e['kind']!='chapter':buf.append(e)
            save(last)
            part=('导读' if first<35 else '第一部分 · 虚拟化' if first<213 else '第二部分 · 并发' if first<319 else '第三部分 · 持久性' if first<436 else '分布式系统' if first<472 else '附录')
            c={'id':ident,'kind':kind,'title':title,'directory':directory,'part':part,'status':'converted','sections':sections}
            chapters.append(c);unit['status']='converted';unit['directory']=directory
            print(title,len(sections),'sections',flush=True)
        # 同页脚注引用可能出现在上节而定义出现在下一节，定义已按全页预先收集。
        dump(ROOT/'维护工具/reading-order.json',{'chapters':chapters})
        dump(ROOT/'维护工具/source-map.json',self.source)
        dump(ROOT/'维护工具/asset-map.json',self.assets)
        dump(ROOT/'维护工具/reports/conversion-coverage.json',{'pages':self.audit,'glyph_corrections':self.corrections,'undefined_footnotes':sorted(self.references-self.footnotes.keys())})
        print('units',len(chapters),'assets',len(self.assets),'glyph corrections',len(self.corrections))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('pdf',type=Path);args=p.parse_args();Converter(args.pdf).run()
