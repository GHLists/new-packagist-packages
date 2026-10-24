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

## Latest list — 2026-10-24 20:21 UTC

New packages created between 2026-10-24 19:19 UTC and 2026-10-24 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T20-21-07-479113Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 19:29:22 | [bjthecod3r/laravel-docket](https://www.nuget.org/packages/bjthecod3r%2Flaravel-docket) | 0.1.0 | Bolaji Ajani | Reporting and change management for Laravel: threaded reports with statuses, ow… |
| 2026-10-24 19:51:07 | [skeeks/cms-communication-telegram](https://www.nuget.org/packages/skeeks%2Fcms-communication-telegram) | 1.0.0 | Semenov Alexander | Telegram bot driver for skeeks/cms-communication |
| 2026-10-24 19:51:58 | [cristianradulescu/staccato-bundle](https://www.nuget.org/packages/cristianradulescu%2Fstaccato-bundle) | v0.1.0 |  | Symfony bundle that turns Markdown content into a static site. |
| 2026-10-24 20:15:29 | [xhulav/charts](https://www.nuget.org/packages/xhulav%2Fcharts) | v0.1.0 | Vladimír Hůla | Integration of Charts.js as Nette Framework component. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
