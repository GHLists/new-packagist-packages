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

## Latest list — 2026-10-27 18:20 UTC

New packages created between 2026-10-27 17:19 UTC and 2026-10-27 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T18-20-48-480137Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 17:32:38 | [tyto-php/foundation](https://www.nuget.org/packages/tyto-php%2Ffoundation) | v0.1.0-rc.1 | Viktor Leite |  |
| 2026-10-27 17:34:54 | [mojointeractive/craft-observer](https://www.nuget.org/packages/mojointeractive%2Fcraft-observer) | 1.2.0 | mojo | mojo observer's connector for Craft CMS: signed status endpoints, deploy marker… |
| 2026-10-27 17:41:40 | [spreedly/composer-sdk-server](https://www.nuget.org/packages/spreedly%2Fcomposer-sdk-server) | v1.0.0 | Spreedly | Composer Server SDK for PHP |
| 2026-10-27 17:43:16 | [spamacom/laravel-html](https://www.nuget.org/packages/spamacom%2Flaravel-html) | v1.0 | Mouhammad Alali; Adam Engebre… | HTML and Form Builders for the Laravel Framework \| Upgraded by Mouhammad Alali |
| 2026-10-27 18:02:58 | [spamacom/adminlte-templates](https://www.nuget.org/packages/spamacom%2Fadminlte-templates) | 6.1 | Mouhammad Alali | AdminLTE templates for Laravel Generator |
| 2026-10-27 18:03:30 | [spamacom/laravel-generator-helpers](https://www.nuget.org/packages/spamacom%2Flaravel-generator-helpers) | 5.1 | Mouhammad Alali | Helper functions for generator packages |
| 2026-10-27 18:03:57 | [spamacom/laravel-ui-adminlte](https://www.nuget.org/packages/spamacom%2Flaravel-ui-adminlte) | 5.2 | Mouhammad Alali | Laravel frontend preset for AdminLTE Theme |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
