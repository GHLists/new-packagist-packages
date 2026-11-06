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

## Latest list — 2026-11-06 20:21 UTC

New packages created between 2026-11-06 19:19 UTC and 2026-11-06 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T20-21-54-006352Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 19:20:25 | [bref/laravel-websockets](https://www.nuget.org/packages/bref%2Flaravel-websockets) | 0.1.0 | Matthieu Napoli | WebSockets for Laravel on AWS Lambda with Bref and API Gateway |
| 2026-11-06 19:31:28 | [c-point-labs/laravel-hostyourai](https://www.nuget.org/packages/c-point-labs%2Flaravel-hostyourai) | v0.1.0 | Maarten Tolhuijs | HostYourAI for Laravel: a Prism provider for chat and a typed client for the de… |
| 2026-11-06 19:31:50 | [webx-ui/module-catalog-collections](https://www.nuget.org/packages/webx-ui%2Fmodule-catalog-collections) | v0.94.0 | WebX UI | Product collections of the WebX UI catalogue: a named block of products a manag… |
| 2026-11-06 19:31:50 | [webx-ui/module-catalog-feeds](https://www.nuget.org/packages/webx-ui%2Fmodule-catalog-feeds) | v0.94.0 | WebX UI | Product feeds for the WebX UI catalogue: files for marketplaces and ad platform… |
| 2026-11-06 19:38:56 | [roy-sandip/laravel-view-extended](https://www.nuget.org/packages/roy-sandip%2Flaravel-view-extended) | v1.0.1 |  | Additional, extensible Artisan commands for generating Laravel views. |
| 2026-11-06 19:41:22 | [siberfx/telegram-bot](https://www.nuget.org/packages/siberfx%2Ftelegram-bot) | v0.1.2 | Selim Görmüş | A clean, modern Telegram bot framework for Laravel 13: hears/patterns, conversa… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
