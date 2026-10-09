#!/usr/bin/env python3
"""记录用户提供的 PDF 的页码和图片来源；不把源 PDF 放入仓库。"""
import argparse
import hashlib
import json
import re
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('pdf', type=Path)
args = parser.parse_args()
expected_path = ROOT/'维护工具/source-map.json'
existing=json.loads(expected_path.read_text()) if expected_path.exists() else {}
source_hash = hashlib.sha256(args.pdf.read_bytes()).hexdigest()
if expected_path.exists() and json.loads(expected_path.read_text())['sha256'] != source_hash:
    raise SystemExit('此工具的图片映射只适用于已登记的 PDF；新底本需重新核对页码和资源编号。')
doc = fitz.open(args.pdf)
toc = doc.get_toc()
top = [r for r in toc if r[0] == 1]
units = []
for i, (_, title, start) in enumerate(top):
    end = top[i + 1][2] - 1 if i + 1 < len(top) else len(doc)
    m = re.match(r'第(\d+)章', title)
    kind = 'chapter' if m else 'appendix' if title.startswith('附录') else 'front_matter'
    units.append({'title': title, 'kind': kind, 'chapter': int(m[1]) if m else None,
                  'pdf_pages': [start, end], 'printed_pages': [start-18,end-18] if start>=19 else None,
                  'status': 'sample_transcribed' if m and int(m[1]) == 18 else 'not_started',
                  'outline_sections': [{'title':t, 'pdf_page':p} for level,t,p in toc if level>1 and start<=p<=end]})
    previous=next((u for u in existing.get('units',[]) if u['pdf_pages']==[start,end]),None)
    if previous:
        for key in ('status','directory','title','outline_sections','bookmark_title'):
            if key in previous:units[-1][key]=previous[key]
data = {'source_file': args.pdf.name, 'sha256': hashlib.sha256(args.pdf.read_bytes()).hexdigest(),
        'pdf_pages': len(doc), 'edition': '人民邮电出版社，2019 年 6 月第 1 版，王海鹏译',
        'inventory_basis': existing.get('inventory_basis','PDF 书签'),
        'public_release': existing.get('public_release','pending_rights_confirmation'), 'units': units}
(ROOT/'维护工具/source-map.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
# 每张图片按 PDF 实际嵌入资源提取，保持源像素，不重绘。
images = [(151,648,'fig-18-1-address-space'),(151,649,'fig-18-2-physical-memory'),
          (151,650,'virtual-address-bits'),(151,651,'vpn-offset-bits'),
          (152,655,'address-21-bits'),(152,656,'fig-18-3-translation'),
          (153,660,'fig-18-4-page-table'),(154,664,'fig-18-5-x86-pte'),
          (157,674,'fig-18-7-memory-trace')]
asset_path=ROOT/'维护工具/asset-map.json'
assets=[a for a in json.loads(asset_path.read_text()) if not a['path'].startswith('第18章-')] if asset_path.exists() else []
for page,xref,name in images:
    content=doc.extract_image(xref)
    path=ROOT/'第18章-分页介绍/assets'/f'{name}.{content["ext"]}'
    path.write_bytes(content['image'])
    assets.append({'path':path.relative_to(ROOT).as_posix(),'pdf_page':page,'printed_page':page-18,
                   'xref':xref,'width':content['width'],'height':content['height'],
                   'sha256':hashlib.sha256(content['image']).hexdigest()})
(ROOT/'维护工具/asset-map.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2)+'\n')
print(f'PDF {len(doc)} 页；{sum(u["kind"]=="chapter" for u in units)} 章；{sum(u["kind"]=="appendix" for u in units)} 附录；提取 {len(assets)} 张图。')
