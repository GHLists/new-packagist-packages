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

## Latest list — 2026-11-04 16:21 UTC

New packages created between 2026-11-04 15:19 UTC and 2026-11-04 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T16-21-39-05764Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 15:20:44 | [webong/cogent](https://www.nuget.org/packages/webong%2Fcogent) | v0.1.0 | Webong | Laravel Eloquent collection extensions: plug, include and count relations witho… |
| 2026-11-04 15:34:53 | [yogadimas/belajar-php-composer-hello](https://www.nuget.org/packages/yogadimas%2Fbelajar-php-composer-hello) | 2.0.0 | Yogadimas | Library Composer Hello |
| 2026-11-04 15:38:28 | [ryanc342/laravel-agent-starter](https://www.nuget.org/packages/ryanc342%2Flaravel-agent-starter) | v1.0.0 |  | Laravel Agent Starter: a Laravel + Inertia + React starter kit with agent guida… |
| 2026-11-04 15:43:54 | [coworkingview/craft-coworkingview](https://www.nuget.org/packages/coworkingview%2Fcraft-coworkingview) | 1.0.0 | CoworkingView | Flexible office and coworking prices by city from the CoworkingView Price Index. |
| 2026-11-04 15:50:45 | [statamic-addon/paper](https://www.nuget.org/packages/statamic-addon%2Fpaper) | v2.0.0 |  | Import Paper artboards as Visual Editor sections. Local tool: the browser canno… |
| 2026-11-04 15:50:59 | [ibaranov/db-backup-sender](https://www.nuget.org/packages/ibaranov%2Fdb-backup-sender) | v1.0.3 | Your Vendor | Почасовое резервное копирование баз MySQL/MariaDB Laravel-проектов с отправкой… |
| 2026-11-04 15:54:21 | [thelia/cookie-consent-manager-module](https://www.nuget.org/packages/thelia%2Fcookie-consent-manager-module) | 1.0.0 |  | Consent management platform for Thelia 3: banner, consent registry, Google Cons… |
| 2026-11-04 15:56:06 | [helga-agentur/drush-policy-commands](https://www.nuget.org/packages/helga-agentur%2Fdrush-policy-commands) | v1.0.0 |  | Drush policy commands that restrict destructive commands (sql:drop, sql:sync, c… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
