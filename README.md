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

## Latest list — 2026-11-12 07:21 UTC

New packages created between 2026-11-12 06:21 UTC and 2026-11-12 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T07-21-45-85411Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 06:25:02 | [goomzo/goomzo-php](https://www.nuget.org/packages/goomzo%2Fgoomzo-php) | v0.1.0 |  | The Goomzo API for PHP: messages, templates, customers and webhooks. |
| 2026-11-12 06:30:56 | [vbushuev/laravel-mattermost](https://www.nuget.org/packages/vbushuev%2Flaravel-mattermost) | 1.1.0 | Vladimir Bushuev | Laravel logging package for Mattermost webhooks |
| 2026-11-12 06:36:43 | [henzeb/housepedia-data-intelligence](https://www.nuget.org/packages/henzeb%2Fhousepedia-data-intelligence) | v1.0.0 | Henze Berkheij | Framework-independent PHP SDK for the Housepedia Data Intelligence API |
| 2026-11-12 06:39:00 | [olivcode/form-guard](https://www.nuget.org/packages/olivcode%2Fform-guard) | v1.0.0 | Olivier Gaillot | Progressive abuse protection for PHP forms, with optional JavaScript signals. |
| 2026-11-12 06:47:30 | [henzeb/housepedia-data-intelligence-laravel](https://www.nuget.org/packages/henzeb%2Fhousepedia-data-intelligence-laravel) | v1.0.0 | Henze Berkheij | Laravel integration for the Housepedia Data Intelligence PHP SDK |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
