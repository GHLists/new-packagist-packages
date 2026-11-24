# New Packagist packages

Hourly lists of packages newly created on
[Packagist.org](https://packagist.org/), the default package registry for
[Composer](https://getcomposer.org/). New packages are discovered through
Packagist's [metadata changes feed](
https://packagist.org/metadata/changes.json), which lists every package
updated since a cursor timestamp; because the feed does not distinguish new
packages from updates, each touched package is checked against its p2
metadata, whose earliest version release date decides whether the package was
created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-packagist-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 15:20 UTC

New packages created between 2026-11-24 14:22 UTC and 2026-11-24 15:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T15-20-33-372622Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 14:23:10 | [wiseadmin/wise-crontab](https://www.nuget.org/packages/wiseadmin%2Fwise-crontab) | v1.0.1 | WiseAdmin Team | WiseAdmin 定时任务调度引擎 — 支持语义化调度与 Cron 表达式、双驱动任务源、分布式锁、任务编排、告警通知、并行执行与后台可视化界面 |
| 2026-11-24 14:24:13 | [wiseadmin/wise-mcp](https://www.nuget.org/packages/wiseadmin%2Fwise-mcp) | v1.0.1 | WiseAdmin Team | WiseAdmin MCP (Model Context Protocol) 基础设施包 — 协议内核、stdio/Streamable HTTP 传输、Se… |
| 2026-11-24 14:25:59 | [wiseadmin/wise-rag](https://www.nuget.org/packages/wiseadmin%2Fwise-rag) | v1.0.1 | WiseAdmin Team | WiseAdmin RAG 知识库包 — 文档摄取、向量检索、引用溯源，插件零接入；内含独立命名空间的 Wiki 知识编译引擎（wise\wiki） |
| 2026-11-24 14:26:22 | [wiseadmin/wise-url](https://www.nuget.org/packages/wiseadmin%2Fwise-url) | v1.0.1 | WiseAdmin Team | WiseAdmin URL 规则引擎 — 方案化 URL 生成与解析、前缀隔离、历史 301、PHPCMS v9 风格规则语法、内置方案与自定义方案 |
| 2026-11-24 14:35:12 | [sy/bootstrap-wysiwyg](https://www.nuget.org/packages/sy%2Fbootstrap-wysiwyg) | 1.0.1 | Syone | Shared WYSIWYG engine and CKEditor backend for the sy/bootstrap plugins |
| 2026-11-24 14:39:01 | [rkr/ai-watermark-removal-tools](https://www.nuget.org/packages/rkr%2Fai-watermark-removal-tools) | v1.1.0 |  | Clean invisible Unicode marks in text and remove embedded C2PA provenance metad… |
| 2026-11-24 14:41:07 | [prolificjones/npm-plugin-installer](https://www.nuget.org/packages/prolificjones%2Fnpm-plugin-installer) | 0.0.3 |  | Installs npm packages and patches package.json after composer install/update. |
| 2026-11-24 14:58:05 | [mrdellimore/rusty-sheet](https://www.nuget.org/packages/mrdellimore%2Frusty-sheet) | 0.1.0 |  | Rust-powered PHP extension for streaming XLSX and CSV: OpenSpout-compatible rea… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
