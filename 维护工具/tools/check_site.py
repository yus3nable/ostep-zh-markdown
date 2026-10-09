#!/usr/bin/env python3
"""检查生成站点内的页面、图片、样式和锚点，包括中文路径。"""
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit

ROOT=Path(__file__).resolve().parents[2]
SITE=ROOT/'website/build/site'
config=(ROOT/'website/mkdocs.base.yml').read_text()
site_url=re.search(r'^site_url:\s*(\S+)',config,re.M)
BASE_PATH=urlsplit(site_url.group(1)).path if site_url else '/'
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=set(); self.refs=[]; self.images=[]; self.reading_links={}
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        if tag in ('a','link') and 'href' in attrs: self.refs.append((tag,attrs['href']))
        if tag in ('img','script') and 'src' in attrs: self.refs.append((tag,attrs['src']))
        if tag=='img': self.images.append(attrs)
        if tag=='a':
            for direction in ('prev','next'):
                if f'md-footer__link--{direction}' in attrs.get('class','').split():
                    self.reading_links[direction]=attrs.get('href','')

pages={}
errors=[]
for p in SITE.rglob('*.html'):
    page=Page(); page.feed(p.read_text()); pages[p.resolve()]=page
if not pages: raise SystemExit('网站尚未生成')
for p,page in pages.items():
    for tag,ref in page.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc: continue
        if u.path.startswith('/'):
            decoded=unquote(u.path)
            if not decoded.startswith(BASE_PATH):
                errors.append(f'{p.relative_to(SITE)}: 链接缺少部署前缀 {ref}')
                continue
            target=SITE/decoded[len(BASE_PATH):]
        else: target=p.parent/unquote(u.path) if u.path else p
        if target.is_dir(): target=target/'index.html'
        target=target.resolve()
        if not target.is_relative_to(SITE.resolve()) or not target.exists():
            errors.append(f'{p.relative_to(SITE)}: {tag} {ref}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{p.relative_to(SITE)}: 未找到锚点 {ref}')
    for img in page.images:
        if not img.get('alt'): errors.append(f'{p.relative_to(SITE)}: 图片缺替代文字')
for a in json.loads((ROOT/'维护工具/asset-map.json').read_text()):
    p=SITE/a['path']
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:
        errors.append(f'网页原图不一致：{a["path"]}')
# 翻页只能沿唯一正文序列前进，不能绕回章节目录或整章副本。
order=json.loads((ROOT/'维护工具/reading-order.json').read_text())['chapters']
reading=[(SITE/c['directory']/s['path']).with_suffix('.html').resolve()
         for c in order if c['id'] not in {'front-35','front-213','front-319'} for s in c['sections']]
for i,path in enumerate(reading):
    for direction,offset in [('prev',-1),('next',1)]:
        expected=reading[i+offset] if 0<=i+offset<len(reading) else None
        ref=pages[path].reading_links.get(direction)
        actual=(path.parent/unquote(urlsplit(ref).path)).resolve() if ref else None
        if actual!=expected:
            errors.append(f'{path.relative_to(SITE)}: {direction} 未按正文顺序跳转')
search=SITE/'search/search_index.json'
if not search.exists(): errors.append('缺少搜索索引')
else:
    data=json.loads(search.read_text())
    if any('chapter.html' in d['location'] for d in data['docs']): errors.append('整章重复进入搜索')
    if not any('18.2' in d['title'] for d in data['docs']): errors.append('小节未进入搜索索引')
report={'status':'passed' if not errors else 'failed','html_pages':len(pages),'errors':errors,
        'scope':'静态资源、链接、锚点及搜索索引；交互另行在浏览器验证'}
(ROOT/'维护工具/reports/site-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
