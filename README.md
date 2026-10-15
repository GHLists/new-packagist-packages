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

## Latest list — 2026-10-15 18:20 UTC

New packages created between 2026-10-15 17:21 UTC and 2026-10-15 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T18-20-33-14067Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 17:24:56 | [liufencn/flarum-mediaembed](https://www.nuget.org/packages/liufencn%2Fflarum-mediaembed) | v1.0.0 | Liufen | 中文媒体站点嵌入：给 Flarum 的 s9e MediaEmbed 补上国内常用视频 / 音乐站点（B站、AcFun、腾讯视频、网易云音乐、西瓜视频），链接… |
| 2026-10-15 17:25:14 | [liufencn/flarum-reply-pin](https://www.nuget.org/packages/liufencn%2Fflarum-reply-pin) | v1.0.0 | Liufen | 帖子内楼层（回复）置顶：把讨论内任意一条回复钉到讨论顶部，并加图钉徽标。 |
| 2026-10-15 17:31:19 | [1994/gift-vouchers-statamic](https://www.nuget.org/packages/1994%2Fgift-vouchers-statamic) | v1.0.0 | 1994 | Gift vouchers for Cargo: sell vouchers with fixed or chosen amounts, email them… |
| 2026-10-15 17:40:10 | [magesentinel/module-monitor](https://www.nuget.org/packages/magesentinel%2Fmodule-monitor) | 2.0.1 | MageSentinel | Store health page, 15-minute health emails, weekly summary and a real-browser t… |
| 2026-10-15 17:45:09 | [docustay/docustay-php](https://www.nuget.org/packages/docustay%2Fdocustay-php) | v0.1.0 | Docustay | Official Docustay API client: send documents for signature and follow them from… |
| 2026-10-15 17:45:39 | [liufencn/flarum-user-delete](https://www.nuget.org/packages/liufencn%2Fflarum-user-delete) | v1.0.0 | Liufen | 后台用户管理补回「删除用户」入口：Flarum 2.0 核心的编辑用户弹窗移除了删除按钮，但后端 DELETE /api/users/{id} 与 canDe… |
| 2026-10-15 17:57:48 | [proceda/fixtures](https://www.nuget.org/packages/proceda%2Ffixtures) | v1.0.0 |  | Fixtures and test data generators for Proceda. |
| 2026-10-15 18:05:35 | [rasuvaeff/context-cli](https://www.nuget.org/packages/rasuvaeff%2Fcontext-cli) | v0.1.0 | Victor Razuvaev | Graceful shutdown for PHP CLI workers: OS signals cancel a rasuvaeff/context Co… |
| 2026-10-15 18:17:10 | [goletter/hyperf-signature](https://www.nuget.org/packages/goletter%2Fhyperf-signature) | v1.0.0 | goletter | System-to-system API signature (HMAC) for hyperf. |
| 2026-10-15 18:19:05 | [ufo-tech/rest-bundle](https://www.nuget.org/packages/ufo-tech%2Frest-bundle) | 1.1.0 | Alex Maistrenko | REST API bundle for building RESTful services in the UFO-Tech ecosystem. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
