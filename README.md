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

## Latest list — 2026-11-27 02:22 UTC

New packages created between 2026-11-27 01:20 UTC and 2026-11-27 02:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T02-22-17-884542Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 01:29:01 | [checknetworks/checknetworks-php](https://www.nuget.org/packages/checknetworks%2Fchecknetworks-php) | v2.0.0-RC6 |  | The official PHP client for the Check Networks API. |
| 2026-11-27 01:41:27 | [gustavo-peixoto/php-qa-scope](https://www.nuget.org/packages/gustavo-peixoto%2Fphp-qa-scope) | 0.1.0 | GustavoPeixoto | Synchronize managed PHP QA scope blocks across PHP QA tool configuration files. |
| 2026-11-27 01:46:01 | [mdgascar/mdg-utils-bundle](https://www.nuget.org/packages/mdgascar%2Fmdg-utils-bundle) | v0.1.0 |  | Symfony bundle: validation constraints, Twig filters and Doctrine types for Mal… |
| 2026-11-27 02:02:25 | [businessapi/monitorhq-php](https://www.nuget.org/packages/businessapi%2Fmonitorhq-php) | v1.0.2 | Business API | PHP SDK for the MonitorHQ API: Australian company, trust, sole trader and ABN m… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
