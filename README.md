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

## Latest list — 2026-10-14 06:21 UTC

New packages created between 2026-10-14 05:21 UTC and 2026-10-14 06:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T06-21-23-837221Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 05:25:25 | [asyntai/mautic-ai-chatbot](https://www.nuget.org/packages/asyntai%2Fmautic-ai-chatbot) | 1.0.0 | Asyntai | Asyntai AI Chatbot for Mautic: an AI chat assistant on your landing pages that… |
| 2026-10-14 05:59:08 | [alifcoder/exportable](https://www.nuget.org/packages/alifcoder%2Fexportable) | v1.0.1 |  | Async document export (csv/xlsx) for Laravel with alifcoder/query-filter |
| 2026-10-14 06:02:37 | [fiber-interop/process](https://www.nuget.org/packages/fiber-interop%2Fprocess) | v0.1.1 |  | Cooperative proc_open() for fiber-interop/api: async\process\run() and start()… |
| 2026-10-14 06:04:46 | [zhongchuanhao/ex-webman-admin](https://www.nuget.org/packages/zhongchuanhao%2Fex-webman-admin) | v2.0.5 | rocky | Ex-Admin for webman 2.x：基于 Ant Design of Vue + webman 的后台系统构建工具（原 rockys/ex-adm… |
| 2026-10-14 06:06:16 | [caiyun/meeting](https://www.nuget.org/packages/caiyun%2Fmeeting) | v1.0.0 | 刘骏霖 | 为 Laravel 提供统一的在线会议能力，支持腾讯会议、华为云会议、钉钉会议与飞书会议。 |
| 2026-10-14 06:06:58 | [kaungsithu883/laravel-offline](https://www.nuget.org/packages/kaungsithu883%2Flaravel-offline) | v0.1.0 | Kaungsithu883 | Durable browser drafts and idempotent offline form synchronization for Laravel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
