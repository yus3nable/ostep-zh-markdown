"""Keep reading order independent of overview pages and whole-chapter copies."""
import html
import json
import posixpath
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = {'front-35', 'front-213', 'front-319'}
redirects = {}


def on_nav(nav, config, files):
    chapters = json.loads((ROOT / '维护工具/reading-order.json').read_text())['chapters']
    reading = []
    redirects.clear()
    for chapter in chapters:
        if chapter['id'] in PARTS:
            continue
        paths = [f'{chapter["directory"]}/{s["path"]}' for s in chapter['sections']]
        reading.extend(files.get_file_from_path(path).page for path in paths)
        redirects[f'{chapter["directory"]}/README.md'] = files.get_file_from_path(paths[0]).page
        if len(paths) == 1:
            redirects[f'{chapter["directory"]}/chapter.md'] = files.get_file_from_path(paths[0]).page
    for page in nav.pages:
        page.previous_page = page.next_page = None
    for i, page in enumerate(reading):
        page.previous_page = reading[i-1] if i else None
        page.next_page = reading[i+1] if i+1 < len(reading) else None
    # 分部导览的开始方向也进入正文，不插入正文的翻页序列。
    for chapter in chapters:
        if chapter['id'] in PARTS:
            first = next(c for c in chapters if c['kind'] == 'chapter' and c.get('part') == chapter['part'])
            files.get_file_from_path(f'{chapter["directory"]}/README.md').page.next_page = files.get_file_from_path(f'{first["directory"]}/{first["sections"][0]["path"]}').page
    return nav


def on_post_page(output, page, config):
    target = redirects.get(page.file.src_uri)
    if target is None:
        return output
    url = html.escape(posixpath.relpath(target.url, posixpath.dirname(page.url)), quote=True)
    return f'<!doctype html><html lang="zh"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={url}"><title>{html.escape(target.title)}</title></head><body><a href="{url}">进入正文</a></body></html>'
