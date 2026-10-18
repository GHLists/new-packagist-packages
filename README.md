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

## Latest list — 2026-10-18 09:21 UTC

New packages created between 2026-10-18 08:23 UTC and 2026-10-18 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T09-21-04-432509Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 08:25:25 | [request-labs/steward-laravel](https://www.nuget.org/packages/request-labs%2Fsteward-laravel) | v1.0.0 |  | Steward by Request agent for Laravel sites: reports installed package versions… |
| 2026-10-18 08:41:41 | [dehnavi/yii2-jdate](https://www.nuget.org/packages/dehnavi%2Fyii2-jdate) | 1.0.0 | Mohammad Mahdi Gholamian; Moh… | Jalali date and time utilities and a range-capable date picker for Yii2. |
| 2026-10-18 08:51:28 | [waply/waply-php](https://www.nuget.org/packages/waply%2Fwaply-php) | v1.0.0 | Waply Indonesia | Official PHP & Laravel SDK for Waply WhatsApp Gateway & Messaging API Indonesia |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
