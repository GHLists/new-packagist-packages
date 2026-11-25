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

## Latest list — 2026-11-25 11:21 UTC

New packages created between 2026-11-25 10:19 UTC and 2026-11-25 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T11-21-07-190781Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 10:19:04 | [atannex/claude-support](https://www.nuget.org/packages/atannex%2Fclaude-support) | v1.2.1 | Atanga Leke Collins | Claude Code support for Laravel: curated slash commands, subagents and skills (… |
| 2026-11-25 10:20:11 | [nietthijmen/laravel-kernel](https://www.nuget.org/packages/nietthijmen%2Flaravel-kernel) | v1.0.0 | nietthijmen | A kernel.sh wrapper for laravel |
| 2026-11-25 10:20:33 | [mowzs/article](https://www.nuget.org/packages/mowzs%2Farticle) | v1.0.0 | sunboy | 文章 |
| 2026-11-25 10:20:35 | [mowzs/system](https://www.nuget.org/packages/mowzs%2Fsystem) | v1.0.0 | sunboy | 系统核心模块 |
| 2026-11-25 10:20:36 | [mowzs/static](https://www.nuget.org/packages/mowzs%2Fstatic) | v1.0.0 | sunboy | 静态资源 |
| 2026-11-25 10:20:40 | [mowzs/lib](https://www.nuget.org/packages/mowzs%2Flib) | v1.0.0 | sunboy |  |
| 2026-11-25 10:34:35 | [kirbydesk/kirbyblock-divider](https://www.nuget.org/packages/kirbydesk%2Fkirbyblock-divider) | 1.0.0 | Christian Fickinger | Divider Block for Kirby CMS |
| 2026-11-25 10:54:58 | [net-os/laravel-emqx](https://www.nuget.org/packages/net-os%2Flaravel-emqx) | v1.0.0 | Rick Bongers | MQTT publishing and EMQX credential management for Laravel. |
| 2026-11-25 11:05:24 | [tuxweb-it/pyroshape](https://www.nuget.org/packages/tuxweb-it%2Fpyroshape) | v0.9.1 | Dino Ciuffetti | Reusable backend toolkit for Pyroshape applications |
| 2026-11-25 11:13:41 | [simflex/texted](https://www.nuget.org/packages/simflex%2Ftexted) | v1.0.0 |  | texted — блочный редактор статей для сайтов и CMS: textarea → блоки → чистый HT… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
