# 阅读站视觉改版

2026-10-08，按用户要求参考 [Anthropic 官网](https://www.anthropic.com/) 的暖白、炭黑、陶土色，以及克制的编辑式版面。

## 实现

- 复用 MkDocs Material，保持原有导航、章节地址和搜索功能。
- 暖白背景 `#faf9f5`、正文 `#24231f`、强调色 `#a34f35`，深色模式采用对应的暖灰配色。
- 以宋体标题、章节标识、原书页码和细分隔线组织阅读层级；正文继续使用易读的系统字体。
- 首页和章首页加入原创装饰图，内容为书页、网格和映射连线，使用炭黑线条、陶土色和灰绿色。图片由内置 imagegen 生成，保存在 `website/assets/paging-editorial.png`，不属于原书插图。
- 装饰仅位于首页和章首页，窄屏章首页使用紧凑图样。原书正文与图示未改动。

## 验证

- MkDocs 严格构建通过。
- `check_book.py`：16 个 Markdown 文件、9 张原书图片检查通过。
- `check_site.py`：17 个 HTML 页面资源、链接、锚点和搜索索引检查通过。
- 浏览器检查桌面、手机布局，手机首页目录抽屉和章节跳转、中文搜索结果、浅色与深色切换。
- 修复手机抽屉边缘露出、首页手机目录被隐藏，以及 Material 默认深色页眉覆盖自定义配色的问题。
- 截图：`redesign-desktop.png`、`redesign-home.png`、`redesign-mobile.png`、`redesign-dark.png`。

本次结果为本地预览，未执行 GitHub 发布。
