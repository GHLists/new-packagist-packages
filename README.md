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

## Latest list — 2026-11-14 17:18 UTC

New packages created between 2026-11-14 16:18 UTC and 2026-11-14 17:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T17-18-38-571393Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 16:25:29 | [filagora/filagora-newsletters](https://www.nuget.org/packages/filagora%2Ffilagora-newsletters) | v0.1.0 |  | Newsletters for Filagora: subscribers with consent, campaigns built from conten… |
| 2026-11-14 16:31:11 | [aathiappan/native-mailer-php](https://www.nuget.org/packages/aathiappan%2Fnative-mailer-php) | v1.0.0 |  | Local SMTP email testing sink with a web inbox, built for Windows + WAMP. |
| 2026-11-14 16:32:24 | [horngunnotes/flarum-horn-signals](https://www.nuget.org/packages/horngunnotes%2Fflarum-horn-signals) | v1.0.0 | Horn Notes | Write railroad horn signals as plain text, such as [horn]- - o -[/horn], and sh… |
| 2026-11-14 16:39:32 | [wit3/filament-relation-navigator](https://www.nuget.org/packages/wit3%2Ffilament-relation-navigator) | v1.0.0 | Salvatore Scalzi | Give every Filament relation manager its own page (/{record}/{relation}) and sw… |
| 2026-11-14 17:08:29 | [ubaidsaleem/laravel-crudgen](https://www.nuget.org/packages/ubaidsaleem%2Flaravel-crudgen) | v1.0.2 | Ubaid Saleem | Generate Livewire 4 CRUD pages from a model's fields() definition |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
