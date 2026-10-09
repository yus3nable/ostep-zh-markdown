#!/usr/bin/env python3
"""验证已登记书稿的结构、相对链接、原图哈希和生成一致性。"""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote,urlsplit
from build_book import ROOT,chapters,outputs

errors=[]
files=[ROOT/p for p in ['README.md','目录.md','来源说明.md','编校说明.md','维护工具/README.md']]
for chapter in chapters():
    base=ROOT/chapter['directory']
    files.extend([base/'README.md',base/'chapter.md'])
    files.extend(base/s['path'] for s in chapter['sections'])
for path,expected in outputs().items():
    if not path.exists() or path.read_text()!=expected:
        errors.append(f'生成文件不同步：{path.relative_to(ROOT)}')
for path in files:
    if not path.exists():
        errors.append(f'缺少文件：{path}'); continue
    text=path.read_text()
    fences=re.findall(r'^\s*```',text,re.M)
    if len(fences)%2: errors.append(f'代码围栏未闭合：{path}')
    if '\ufffd' in text or 'homeofbook.com' in text:
        errors.append(f'遗留乱码或重复页脚：{path}')
    definitions=re.findall(r'^\[\^([^\]]+)\]:',text,re.M)
    used=set(re.findall(r'\[\^([^\]]+)\](?!:)',text))
    if used-set(definitions):errors.append(f'脚注缺定义：{path} {used-set(definitions)}')
    without_code=re.sub(r'(?ms)^\s*```.*?^\s*```[^\n]*','',text)
    for dest in re.findall(r'\]\(([^)\s]+)\)',without_code):
        url=urlsplit(dest)
        if url.scheme or url.netloc or not url.path: continue
        target=(path.parent/unquote(url.path)).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f'失效或越界链接：{path.relative_to(ROOT)} -> {dest}')
assets=json.loads((ROOT/'维护工具/asset-map.json').read_text())
for a in assets:
    p=ROOT/a['path']
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:
        errors.append(f'图片内容与 PDF 提取记录不符：{a["path"]}')
book=(ROOT/'第18章-分页介绍/chapter.md').read_text()
for n in range(1,8):
    if f'图 18.{n}' not in book: errors.append(f'缺图 18.{n}')
for n in range(1,7):
    if not re.search(fr'^## 18\.{n} ',book,re.M): errors.append(f'缺小节 18.{n}')
homework=(ROOT/'第18章-分页介绍/sections/homework.md').read_text()
if re.findall(r'^(\d)\. ',homework,re.M)!=['1','2','3','4']:
    errors.append('作业题号不全或顺序异常')
if '2<sup>6</sup>' not in book or '2<sup>20</sup>' not in book:
    errors.append('样章指数结构丢失')
source=json.loads((ROOT/'维护工具/source-map.json').read_text())
if len([u for u in source['units'] if u['kind']=='chapter'])!=50:
    errors.append('来源清单应有 50 章')
registered=chapters()
numbers={int(c['id']) for c in registered if c.get('kind')=='chapter'}
appendices={c['id'] for c in registered if c.get('kind')=='appendix'}
if numbers!=set(range(1,51)):errors.append('正文登记未覆盖第 1—50 章')
if appendices!=set('ABCDEFG'):errors.append('附录登记未覆盖 A—G')
for unit in source['units']:
    if unit['kind'] not in ('chapter','appendix'):continue
    ident=str(unit['chapter']) if unit['kind']=='chapter' else re.match(r'附录([A-G])',unit['title'])[1]
    matches=[c for c in registered if c['id']==ident]
    if not matches:continue
    c=matches[0]
    expected={m[0] for s in unit['outline_sections'] if (m:=re.match(r'^(?:\d+|[A-G])\.\d+',s['title']))}
    present={m[0] for s in c['sections'] if (m:=re.match(r'^(?:\d+|[A-G])\.\d+',s['title']))}
    if expected-present:errors.append(f'{ident} 章缺小节：{expected-present}')
coverage=json.loads((ROOT/'维护工具/reports/conversion-coverage.json').read_text())
covered={p['pdf_page'] for p in coverage['pages']}|set(range(150,160))
if covered!=set(range(1,501)):errors.append('页级覆盖不完整')
for p in coverage['pages']:
    if 'source_lines' in p and p['source_lines']!=p['represented_lines']:
        errors.append(f'PDF {p["pdf_page"]} 页有未表示的来源行')
if coverage['undefined_footnotes']:errors.append('来源脚注匹配不完整')
report={'status':'passed' if not errors else 'failed','markdown_files':len(files),'images_checked':len(assets),
        'chapters_in_inventory':50,'chapters_structurally_checked':len(numbers),'appendices_checked':len(appendices),
        'pdf_pages_covered':len(covered),'sections':sum(len(c['sections']) for c in registered),'errors':errors,
        'scope':'结构、图片与生成一致性；不等同于全书内容审校'}
(ROOT/'维护工具/reports/book-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
