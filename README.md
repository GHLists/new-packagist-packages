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

## Latest list — 2026-11-16 16:18 UTC

New packages created between 2026-11-16 15:21 UTC and 2026-11-16 16:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T16-18-29-978502Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 15:33:35 | [igne-agency/laravel-auth](https://www.nuget.org/packages/igne-agency%2Flaravel-auth) | v0.1.0 | Rick Blanksma | Headless authentication for Laravel apps on top of Laravel Fortify and Sanctum:… |
| 2026-11-16 15:41:19 | [starbug/emails](https://www.nuget.org/packages/starbug%2Femails) | v0.9.0 | Ali Gangji | Starbug emails module. |
| 2026-11-16 15:41:19 | [starbug/files](https://www.nuget.org/packages/starbug%2Ffiles) | v0.9.0 | Ali Gangji | Starbug files module. |
| 2026-11-16 15:41:19 | [starbug/log](https://www.nuget.org/packages/starbug%2Flog) | v0.9.0 | Ali Gangji | Starbug logging module. |
| 2026-11-16 15:41:19 | [starbug/users](https://www.nuget.org/packages/starbug%2Fusers) | v0.9.0 | Ali Gangji | Starbug users module. |
| 2026-11-16 15:53:24 | [starbug/imports](https://www.nuget.org/packages/starbug%2Fimports) | v0.9.0 |  | Imports module. |
| 2026-11-16 15:53:24 | [starbug/menus](https://www.nuget.org/packages/starbug%2Fmenus) | v0.9.0 | Ali Gangji | Starbug menus module. |
| 2026-11-16 15:54:10 | [metadrop/gocontact-php](https://www.nuget.org/packages/metadrop%2Fgocontact-php) | 1.0.0 | Omar Lopesino | PHP client for the GoContact CCaaS REST API: contacts, databases, extrafields a… |
| 2026-11-16 16:11:51 | [starbug/content](https://www.nuget.org/packages/starbug%2Fcontent) | v0.9.0 | Ali Gangji | Starbug content module. |
| 2026-11-16 16:11:51 | [starbug/settings-admin](https://www.nuget.org/packages/starbug%2Fsettings-admin) | v0.9.0 | Ali Gangji | Admin UI for Starbug settings module. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
