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

## Latest list — 2026-10-12 13:18 UTC

New packages created between 2026-10-12 12:21 UTC and 2026-10-12 13:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T13-18-54-742846Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 12:24:17 | [davingm/laravel-runtime](https://www.nuget.org/packages/davingm%2Flaravel-runtime) | v1.0.0 |  | Internal Composer plugin that installs the Laravel runtime directory. |
| 2026-10-12 12:27:26 | [straschek-io/typo3-backend-feedback](https://www.nuget.org/packages/straschek-io%2Ftypo3-backend-feedback) | v1.1.0 | Michael Straschek | Backend toolbar button for editors to send feedback such as a missing permissio… |
| 2026-10-12 12:32:41 | [liquiddesign/eshop-doryo-admin](https://www.nuget.org/packages/liquiddesign%2Feshop-doryo-admin) | v0.1.0 |  | Zápis do administrace e-shopu pro Doryo/Kolego — headless spouštění admin prese… |
| 2026-10-12 13:07:13 | [hostkurd/flocms-admin](https://www.nuget.org/packages/hostkurd%2Fflocms-admin) | v0.1.0 | HostKurd | Admin panel builder for FloCMS: resources declared in PHP, server-rendered CRUD… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
