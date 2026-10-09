# 维护指南

## 正文与生成文件

每个章节或附录的 `sections/` 保存唯一正文；对应的 `assets/` 保存图示。章节 `README.md`、`chapter.md` 及根目录 `目录.md` 都由工具生成。修改小节后运行：

```sh
python3 维护工具/tools/build_book.py
python3 维护工具/tools/check_book.py
```

阅读顺序和小节来源页码记录在 `维护工具/reading-order.json`。新增章节时，先整理小节并完成核对，再登记到此文件。未整理章节仅出现在全书目录，不生成空白阅读页。

`source-map.json` 记录 PDF 的版本、校验值和全部章节范围，`asset-map.json` 记录图片对应的 PDF 页码、资源编号、像素和校验值。页码清单由 PDF 书签建立，小节标题取自页面文字；附录 G 的 xv6 拼写按章首页修正。

## 本地网站

网站使用 Material for MkDocs，正文和 GitHub 阅读使用同一份 Markdown。依赖版本固定在 `website/requirements.txt`。

```sh
python3 -m venv .tools/venv
.tools/venv/bin/python -m pip install -r website/requirements.txt
.tools/venv/bin/python website/build.py
python3 维护工具/tools/check_site.py
.tools/venv/bin/python -m mkdocs serve --config-file website/build/mkdocs.yml --dev-addr 127.0.0.1:8000
```

浏览器打开 `http://127.0.0.1:8000/`。修改小节后重新执行 `website/build.py`，不要编辑 `website/build/` 中的文件。

网站使用本地字体，支持中文搜索、前后页导航、脚注、代码复制和明暗主题。整章页面不重复加入搜索索引。

## PDF 核对

源 PDF 保留在用户原路径，不复制进仓库。转换工具依赖固定在 `维护工具/requirements.txt`。当前使用 PyMuPDF 1.26.7；本机 Python 3.11 下 1.27.2.3 的批量字体追踪出现引用计数崩溃，故固定为已经完成全书转换的版本。

```sh
.tools/venv/bin/python -m pip install -r 维护工具/requirements.txt
.tools/venv/bin/python 维护工具/tools/audit_fonts.py '/完整路径/操作系统导论 中文.pdf'
.tools/venv/bin/python 维护工具/tools/convert_pdf.py '/完整路径/操作系统导论 中文.pdf'
.tools/venv/bin/python website/build.py
```

`convert_pdf.py` 会重写第 18 章以外的转换正文；日常编校只改 `sections/` 并运行 `build_book.py`，无需重新抽取 PDF。需要让修复在重新转换后保留时，将其记录到 `layout-overrides.json` 或转换工具中。第 18 章的人工样章保留不动。

`font-map.json` 保存字形校正；`layout-overrides.json` 保存经版面核对的复杂公式区域和行内分式。`conversion-coverage.json` 记录每页来源行的去向及字形修复，不代表逐句人工审校。

`tmp/` 存放本地提取文本和页面预览，`.tools/` 存放本地依赖；均由 Git 忽略。机械检查验证结构和资源，不能替代逐页内容核对。验证记录保存在 `维护工具/reports/`。

## 发布

仓库地址为 <https://github.com/yus3nable/ostep-zh-markdown>，阅读地址为 <https://yus3nable.github.io/ostep-zh-markdown/>。`main` 保存书稿和构建工具，`gh-pages` 保存生成的网站；GitHub Pages 从 `gh-pages` 分支根目录发布。

修改书稿后，构建、检查并发布：

```sh
.tools/venv/bin/python website/build.py
.tools/venv/bin/python 维护工具/tools/check_book.py
.tools/venv/bin/python 维护工具/tools/check_site.py
.tools/venv/bin/python -m ghp_import -n -p -b gh-pages website/build/site
```

书稿修改另行提交并推送到 `main`；仅推送 `main` 不会更新网站。发布后检查 GitHub 的 Pages 部署状态和实际阅读网址。`website/mkdocs.base.yml` 中的 `site_url` 必须包含仓库子路径，保证 404 页资源与导航可用。源 PDF、临时文本和本地运行环境均不上传。
