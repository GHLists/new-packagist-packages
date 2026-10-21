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

## Latest list — 2026-10-21 20:21 UTC

New packages created between 2026-10-21 19:19 UTC and 2026-10-21 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T20-21-46-766829Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 19:20:02 | [arm092/omnipay-idbank](https://www.nuget.org/packages/arm092%2Fomnipay-idbank) | v1.1.2 | Apricode Team | IDBank EPG payment gateway driver for Omnipay |
| 2026-10-21 19:25:58 | [vergil-lai/laravel-daily-activity](https://www.nuget.org/packages/vergil-lai%2Flaravel-daily-activity) | v1.0.0 | Vergil | Track daily activities and streaks with compact yearly bitmaps for Laravel. |
| 2026-10-21 19:31:33 | [serwisant/serwisant-silex](https://www.nuget.org/packages/serwisant%2Fserwisant-silex) | 1.0.0 | Arkadiusz Kuryłowicz | Minimal Silex-compatible micro-framework built on Symfony components and Pimple |
| 2026-10-21 19:31:58 | [solophp/http-emitter](https://www.nuget.org/packages/solophp%2Fhttp-emitter) | v1.0.0 | Vitaliy Olos | PSR-7 HTTP Response Emitter |
| 2026-10-21 19:38:47 | [vadykoo/laravel-todo-board](https://www.nuget.org/packages/vadykoo%2Flaravel-todo-board) | v1.0.0 | vadykoo | A standalone Laravel kanban-style todo board with assignees, due dates, images,… |
| 2026-10-21 19:39:29 | [numera11y/ikonym](https://www.nuget.org/packages/numera11y%2Fikonym) | v0.1.0 |  | Portable geometric DiceBear avatar style definitions for five grid densities. |
| 2026-10-21 19:49:42 | [sparkworldke/nativephp-sms-reader-bridge](https://www.nuget.org/packages/sparkworldke%2Fnativephp-sms-reader-bridge) | v1.0.0 | Anthony Tendwa; Sparkworld | A NativePHP Mobile plugin that lets your Android app read SMS messages from the… |
| 2026-10-21 19:55:54 | [yuriitatur/repository](https://www.nuget.org/packages/yuriitatur%2Frepository) | v0.1.0 | Yurii Tatur | A simple framework/db agnostic repository package |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
