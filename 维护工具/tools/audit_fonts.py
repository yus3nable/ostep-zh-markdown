import fitz,io,hashlib,json,collections
from fontTools.ttLib import TTFont
from pathlib import Path
import argparse
ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser(description='按相同字形跨字体子集比对 Unicode 映射')
parser.add_argument('pdf');args=parser.parse_args()
PDF=args.pdf
expected=json.loads((ROOT/'维护工具/source-map.json').read_text())['sha256']
if hashlib.sha256(Path(PDF).read_bytes()).hexdigest()!=expected:raise SystemExit('底本 SHA256 不匹配')
doc=fitz.open(PDF)
fonts={}; signatures={};seen=collections.defaultdict(collections.Counter);sources=collections.defaultdict(set)
examples={}
for page in doc:
 fm={f[3].split('+')[-1]:f[0] for f in page.get_fonts() if f[1]=='ttf'}
 for sp in page.get_texttrace():
  fid=fm.get(sp['font'])
  if not fid:continue
  if fid not in fonts:
   try:fonts[fid]=TTFont(io.BytesIO(doc.extract_font(fid)[3]))
   except:fonts[fid]=None
  font=fonts[fid]
  if font is None or 'glyf' not in font:continue
  for c in sp['chars']:
   uni,gid=c[:2]
   if uni<0x3000 and not 48<=uni<=57:continue
   key=(fid,gid)
   if key not in signatures:
    gly=font['glyf'][font.getGlyphName(gid)]
    co,en,fl=gly.getCoordinates(font['glyf'])
    sig=hashlib.sha256(repr((list(co),list(en),list(fl))).encode()).hexdigest()
    signatures[key]=sig
   sig=signatures[key];examples.setdefault(sig, {'pdf_page': page.number+1, 'bbox': list(c[3])});seen[sig][chr(uni)]+=1;sources[(sig,chr(uni))].add(fid)
conflicts=[]; fixes={}
for sig,cc in seen.items():
 if len(cc)>1:
  ranking=sorted(cc,key=lambda c:(len(sources[(sig,c)]),cc[c]),reverse=True)
  winner={'随御':'御','变金':'金','我夸':'夸'}.get(''.join(cc),ranking[0]); conflicts.append({'example':examples[sig],'candidates':dict(cc),'font_votes':{c:len(sources[(sig,c)]) for c in cc},'winner':winner})
  for (fid,gid),s in signatures.items():
   if s==sig: fixes[f'{fid}:{gid}']=winner
print(json.dumps(conflicts,ensure_ascii=False,indent=2))
json.dump({'conflicts':conflicts,'glyphs':fixes},open(ROOT/'维护工具/font-map.json','w'),ensure_ascii=False,indent=2)
print('fonts',len(fonts),'glyphs',len(signatures),'conflicts',len(conflicts))
