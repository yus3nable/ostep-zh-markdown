#!/usr/bin/env python3
"""小节正文和网站共用书稿；网站中间文件始终留在 build/。"""
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
BUILD=ROOT/'website/build'
DOCS=BUILD/'docs'
subprocess.run([sys.executable,str(ROOT/'维护工具/tools/build_book.py')],check=True)
if DOCS.exists():
    shutil.rmtree(DOCS)
DOCS.mkdir(parents=True)
# 保留书稿相对目录；避免生成第二份需要编辑的正文。
for path in ['README.md','目录.md','来源说明.md','编校说明.md','维护工具/README.md']:
    dest=DOCS/path; dest.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(ROOT/path,dest)
order=json.loads((ROOT/'维护工具/reading-order.json').read_text())
PARTS = {
    'front-35': ('第一部分', '虚拟化', '从进程与 CPU 调度，到地址空间与内存管理。'),
    'front-213': ('第二部分', '并发', '从线程与锁，到条件变量、信号量与并发错误。'),
    'front-319': ('第三部分', '持久性', '从 I/O 设备与磁盘，到文件系统、日志与数据完整性。'),
}
nav=[{'书籍介绍':'README.md'},{'全书目录':'目录.md'}]
manifest=[]
groups={}
for chapter in order['chapters']:
    directory=chapter['directory']
    shutil.copytree(ROOT/directory,DOCS/directory)
    contents=[]
    for section in chapter['sections']:
        path=f'{directory}/{section["path"]}'
        contents.append({section['title']:path})
        manifest.append({'source':path,'pdf_pages':section['pdf_pages']})
    group='书前资料' if chapter['sections'][0]['pdf_pages'][0]<19 else chapter.get('part','导读')
    if group not in groups:
        groups[group]=[];nav.append({group:groups[group]})
    if chapter['id'] in PARTS:
        groups[group].append({chapter['title']:f'{directory}/README.md'})
    elif len(contents)==1:
        groups[group].append({chapter['title']:next(iter(contents[0].values()))})
    else:
        groups[group].append({chapter['title']:contents})
    # 聚合页面不重复进入搜索结果。
    p=DOCS/directory/'chapter.md'
    p.write_text('---\nsearch:\n  exclude: true\n---\n\n'+p.read_text())
    p=DOCS/directory/'README.md'
    p.write_text('---\nsearch:\n  exclude: true\n---\n\n'+p.read_text())
nav.extend([{'编校说明':'编校说明.md'},{'来源说明':'来源说明.md'},{'维护指南':'维护工具/README.md'}])
# 网站元数据仅控制呈现，不修改 Markdown 正文或章节路径。
metadata = {'README.md': {'kind':'home','context':'Operating Systems: Three Easy Pieces','description':'虚拟化、并发与持久性。','detail':'50 章正文 · 7 个附录','art':True}}
for chapter in order['chapters']:
    if chapter['id'] in PARTS:
        continue
    for i, section in enumerate(chapter['sections']):
        first,last=section['pdf_pages']
        opening=section['title']==chapter['title']
        metadata[f'{chapter["directory"]}/{section["path"]}']={
            'kind':'opening' if opening else 'section',
            'context':chapter['title'] if opening else chapter.get('part',''),
            'display_title':re.sub(r'^(第 \d+ 章 |附录 [A-G] )','',chapter['title']) if opening else None,
            'anchor':chapter['id'] if i==0 else None,
            'detail':(f'原书第 {first-18} 页' if first==last else f'原书第 {first-18}–{last-18} 页') if first>=19 else (f'PDF 第 {first} 页' if first==last else f'PDF 第 {first}–{last} 页'),
            'art':i==0 and chapter['id']=='18'}
for name,meta in metadata.items():
    p=DOCS/name
    chapter=next((c for c in order['chapters'] if name.startswith(c['directory']+'/')),None)
    data={'ostep':meta}
    if chapter and len(chapter['sections'])>1:
        data['chapter_start']=name==f'{chapter["directory"]}/{chapter["sections"][0]["path"]}'
        data['whole_chapter']=f'{chapter["directory"]}/chapter.html'
    p.write_text('---\n'+yaml.safe_dump(data,allow_unicode=True,sort_keys=False)+'---\n\n'+p.read_text())
for chapter in order['chapters']:
    if len(chapter['sections']) <= 1:
        continue
    p=DOCS/chapter['directory']/'chapter.md'
    first_path=f'{chapter["directory"]}/{chapter["sections"][0]["path"]}'
    meta={'kind':'opening','context':chapter['title'],
          'display_title':re.sub(r'^(第 \d+ 章 |附录 [A-G] )','',chapter['title']),
          'detail':'整章阅读','section_url':first_path.replace('.md','.html')}
    body=p.read_text().split('---\n',2)[2].lstrip()
    p.write_text('---\n'+yaml.safe_dump({'ostep':meta,'search':{'exclude':True}},allow_unicode=True,sort_keys=False)+'---\n\n'+body)
# 纸书分部扉页在网站中成为可操作的章节入口；旧路径仍可阅读。
for chapter in order['chapters']:
    if chapter['id'] not in PARTS:
        continue
    context,title,description=PARTS[chapter['id']]
    members=[c for c in order['chapters'] if c['kind']=='chapter' and c.get('part')==chapter['part']]
    links=[{'number':c['id'], 'title':re.sub(r'^第 \d+ 章 ', '', c['title']),
            'url':f'{c["directory"]}/{c["sections"][0]["path"]}'.replace('.md','.html')} for c in members]
    meta={'kind':'part','context':context,'display_title':title,'description':description,
          'detail':f'第 {members[0]["id"]}–{members[-1]["id"]} 章 · {len(members)} 章',
          'chapters':links}
    # 保留底本扉页作为低干扰的来源链接，不占据阅读主区。
    source=(ROOT/chapter['directory']/chapter['sections'][0]['path']).read_text()
    asset=re.search(r'!\[[^\]]*\]\(\.\./([^)]+)\)',source).group(1)
    meta['source_url']=f'{chapter["directory"]}/{asset}'
    paths=['README.md','chapter.md']+[s['path'] for s in chapter['sections']]
    for path in paths:
        data={'title':f'{context} · {title}', 'ostep':meta}
        if path!='README.md':
            data['search']={'exclude':True}
        p=DOCS/chapter['directory']/path
        p.write_text('---\n'+yaml.safe_dump(data,allow_unicode=True,sort_keys=False)+'---\n\n# '+chapter['title']+'\n')
    catalog=DOCS/'目录.md'
    catalog.write_text(catalog.read_text().replace(
        f'[连续阅读]({chapter["directory"]}/chapter.md)',
        f'[章节导览]({chapter["directory"]}/README.md)'))
# 将 Markdown 图片替代文本同时呈现为网站图注，源文件仍保持通用 Markdown。
# 所有站内章名入口一致指向第一篇正文，单篇章节的整章链接也合并。
for p in DOCS.rglob('*.md'):
    text=p.read_text()
    for chapter in order['chapters']:
        if chapter['id'] in PARTS:
            continue
        start=f'{chapter["directory"]}/{chapter["sections"][0]["path"]}'
        text=text.replace(f']({chapter["directory"]}/README.md)',f']({start})')
        if len(chapter['sections'])==1:
            text=text.replace(f'[连续阅读]({chapter["directory"]}/chapter.md)',f'[阅读正文]({start})')
    p.write_text(text)
for p in DOCS.rglob('*.md'):
    text=p.read_text()
    text=re.sub(r'^!\[([^\]]+)\]\(([^)]+)\)$',
                lambda m:m[0]+'\n\n<p class="image-caption">'+html.escape(m[1])+'</p>',text,flags=re.M)
    p.write_text(text)
shutil.copytree(ROOT/'website/styles',DOCS/'styles',dirs_exist_ok=True)
config=yaml.safe_load((ROOT/'website/mkdocs.base.yml').read_text())
config['theme']['custom_dir']='../overrides'
config['hooks']=['../reading_navigation.py']
shutil.copytree(ROOT/'website/assets',DOCS/'assets',dirs_exist_ok=True)
config.update(docs_dir='docs',site_dir='site',nav=nav)
(BUILD/'mkdocs.yml').write_text(yaml.safe_dump(config,allow_unicode=True,sort_keys=False))
(BUILD/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,'-m','mkdocs','build','--strict','--config-file',str(BUILD/'mkdocs.yml')],check=True)
print('网站已生成：website/build/site/index.html')
