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

## Latest list — 2026-11-10 15:21 UTC

New packages created between 2026-11-10 14:19 UTC and 2026-11-10 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T15-21-35-977179Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 14:25:47 | [osamaelnagar/oomycache](https://www.nuget.org/packages/osamaelnagar%2Foomycache) | v0.1.0-alpha.1 | Osama Mohammed Elnagar | Eloquent query caching for Laravel — built for Filament-scale data. |
| 2026-11-10 14:26:56 | [vivaltodev/connect-php](https://www.nuget.org/packages/vivaltodev%2Fconnect-php) | v0.2.3 |  | PHP SDK for the Vivalto Connect API: SMS, PDF, images and webhooks |
| 2026-11-10 14:31:34 | [sohaibbinmohsin/pak-geodata](https://www.nuget.org/packages/sohaibbinmohsin%2Fpak-geodata) | v0.11.0 | Sohaib Bin Mohsin | Comprehensive, typed, offline geographic data for all areas and cities in Pakis… |
| 2026-11-10 14:39:51 | [eiclu/simplesamlphp-module-loginaudit](https://www.nuget.org/packages/eiclu%2Fsimplesamlphp-module-loginaudit) | v1.0.0 |  | Login audit for SimpleSAMLphp: logs every successful login, shows the history i… |
| 2026-11-10 14:54:51 | [janalis/collaborate_drupal](https://www.nuget.org/packages/janalis%2Fcollaborate_drupal) | 0.5.0 |  | Live collaboration for Drupal's administration: shared drafts of entity forms,… |
| 2026-11-10 14:58:19 | [towardstudio/craft-cms-guide](https://www.nuget.org/packages/towardstudio%2Fcraft-cms-guide) | 1.0.0 | Toward | A CMS guide for content editors, built into the Craft control panel |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
