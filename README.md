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

## Latest list — 2026-10-02 13:20 UTC

New packages created between 2026-10-02 12:20 UTC and 2026-10-02 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T13-20-28-552938Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 12:48:52 | [lekoala/kaly](https://www.nuget.org/packages/lekoala%2Fkaly) | 0.1.0 | Thomas | A small modular PSR HTTP framework with convention-based routing and first-clas… |
| 2026-10-02 12:53:53 | [yesjoar/t3monitoring-client-extended](https://www.nuget.org/packages/yesjoar%2Ft3monitoring-client-extended) | 0.1.0 | Kai Seliger | Monitoring: scheduler and log insights - Adds scheduler, system log and log fil… |
| 2026-10-02 13:00:56 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.7 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |
| 2026-10-02 13:03:57 | [ismailnakkar/laravel-listing](https://www.nuget.org/packages/ismailnakkar%2Flaravel-listing) | v0.1.0 | Ismail Nakkar | Easy, typed querying and filtering for Blade list pages: declare filters and so… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
