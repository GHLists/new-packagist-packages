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

## Latest list — 2026-10-28 04:23 UTC

New packages created between 2026-10-28 03:19 UTC and 2026-10-28 04:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T04-23-11-394924Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 03:29:03 | [binhtq1/kern-cms](https://www.nuget.org/packages/binhtq1%2Fkern-cms) | v0.1.0 | Binh Tran | Kern CMS on Laravel 13 |
| 2026-10-28 03:35:34 | [contena-cms/contena-rector](https://www.nuget.org/packages/contena-cms%2Fcontena-rector) | 0.6.0 |  | Contena specific Rector |
| 2026-10-28 03:40:11 | [webimpian/smsniaga-php](https://www.nuget.org/packages/webimpian%2Fsmsniaga-php) | v1.0.0 | Khairul Imran | PHP SDK for the SMS Niaga API: send SMS, track delivery reports, and manage sen… |
| 2026-10-28 03:59:23 | [dipuxike/laravel-boost-command-code](https://www.nuget.org/packages/dipuxike%2Flaravel-boost-command-code) | 1.0.0 |  | Command Code agent for Laravel Boost. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
