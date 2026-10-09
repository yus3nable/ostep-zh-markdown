#!/usr/bin/env python3
"""从唯一的小节正文生成整章和阅读目录。只使用标准库。"""
import argparse
import json
import re
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ORDER = ROOT / '维护工具/reading-order.json'


def chapters():
    return json.loads(ORDER.read_text())['chapters']


def chapter_text(chapter):
    has_opening=chapter['sections'][0]['title']==chapter['title']
    parts = [] if has_opening else ['# '+chapter['title']]
    for i, section in enumerate(chapter['sections']):
        text = (ROOT / chapter['directory'] / section['path']).read_text().strip()
        # 小节比整章深一级：所有相对文件引用统一向上移动一级。
        text = re.sub(r'\]\(\.\./([^\s)]+)\)', r'](\1)', text)
        if i or not has_opening:
            text = re.sub(r'^(#{1,5}) ', r'#\1 ', text, flags=re.M)
        parts.append(text)
    return '\n\n'.join(parts) + '\n'


def outputs():
    result = {}
    for chapter in chapters():
        directory = ROOT / chapter['directory']
        result[directory / 'chapter.md'] = chapter_text(chapter)
        catalog=os.path.relpath(ROOT/'目录.md',directory)
        lines = [f'# {chapter["title"]}', '', f'[整章连续阅读](chapter.md) · [全书目录]({catalog})', '']
        lines += [f'- [{s["title"]}]({s["path"]})' for s in chapter['sections']]
        result[directory / 'README.md'] = '\n'.join(lines) + '\n'
    source = json.loads((ROOT/'维护工具/source-map.json').read_text())
    lines = ['# 全书目录', '', '底本：2019 年中文第 1 版。50 章正文、A—G 附录、书前资料和三部分导语均可阅读。', '', '| 内容 | PDF 页码 | 阅读方式 |', '| --- | --- | --- |']
    for c in chapters():
        first=c['sections'][0]['pdf_pages'][0];last=c['sections'][-1]['pdf_pages'][1]
        lines.append(f'| [{c["title"]}]({c["directory"]}/README.md) | {first}—{last} | [连续阅读]({c["directory"]}/chapter.md) |')
    lines += ['', '正文以可编辑 Markdown 保存；复杂表格与独立公式保留原版局部图像，表格另附文字。版本与转录说明见[编校说明](编校说明.md)。']
    result[ROOT/'目录.md']='\n'.join(lines)+'\n'
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    stale=[]
    for path,content in outputs().items():
        if args.check:
            if not path.exists() or path.read_text()!=content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(content)
    if stale:
        raise SystemExit('生成文件与小节不同步：'+', '.join(stale))
    print('整章和目录一致性通过。' if args.check else '已生成整章和目录。')

if __name__=='__main__':
    main()
