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

## Latest list — 2026-10-01 02:19 UTC

New packages created between 2026-10-01 01:20 UTC and 2026-10-01 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T02-19-28-304475Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 01:22:02 | [chargealong/chargealong](https://www.nuget.org/packages/chargealong%2Fchargealong) | v0.1.0 |  | Find EV chargers near a point, plan a road trip through charging stops, and loo… |
| 2026-10-01 01:44:07 | [sambitar/arabic-restore](https://www.nuget.org/packages/sambitar%2Farabic-restore) | v0.1.0 |  | Restore scrambled Arabic text with an OpenAI agent. |
| 2026-10-01 02:00:44 | [omerkoseoglu/devextreme-data](https://www.nuget.org/packages/omerkoseoglu%2Fdevextreme-data) | v0.1.0 |  | Server-side data processing for DevExtreme widgets in PHP: filtering, sorting,… |
| 2026-10-01 02:03:55 | [omerkoseoglu/devextreme-data-laravel](https://www.nuget.org/packages/omerkoseoglu%2Fdevextreme-data-laravel) | v0.1.0 |  | Laravel integration for omerkoseoglu/devextreme-data: server-side DevExtreme da… |
| 2026-10-01 02:05:39 | [omerkoseoglu/devextreme-data-symfony](https://www.nuget.org/packages/omerkoseoglu%2Fdevextreme-data-symfony) | v0.1.0 |  | Symfony bundle for omerkoseoglu/devextreme-data: server-side DevExtreme data pr… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
