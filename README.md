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

## Latest list — 2026-10-08 10:19 UTC

New packages created between 2026-10-08 09:20 UTC and 2026-10-08 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T10-19-28-032608Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 09:31:05 | [muhmd/laravel-autoseed](https://www.nuget.org/packages/muhmd%2Flaravel-autoseed) | v1.0.0 | Muhmdhamed | Scan the database schema and fill every table with realistic dummy data, respec… |
| 2026-10-08 09:32:39 | [curtisjackson/bim-core](https://www.nuget.org/packages/curtisjackson%2Fbim-core) | 1.1.7 | Stanislav Semenov; Sergey Ans… | Bitrix db migration core libs |
| 2026-10-08 09:56:09 | [networkteam/oauth2-server](https://www.nuget.org/packages/networkteam%2Foauth2-server) | v1.0.0 | Alex Bilbie; Andy Millington | Fork of league/oauth2-server 9.4.1 with support for PSR-7 1.1 and 2.0. |
| 2026-10-08 10:01:51 | [cam5/domoarigato](https://www.nuget.org/packages/cam5%2Fdomoarigato) | v0.1.0 | Cameron Hurd | Build HTML in PHP with elements and attributes as objects: escaped by default,… |
| 2026-10-08 10:04:57 | [nowo-tech/altcha-type-bundle](https://www.nuget.org/packages/nowo-tech%2Faltcha-type-bundle) | v1.0.0 | Nowo.tech | Symfony FormType for ALTCHA — privacy-friendly, self-hosted proof-of-work CAPTC… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
