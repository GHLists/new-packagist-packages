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

## Latest list — 2026-11-22 20:20 UTC

New packages created between 2026-11-22 19:18 UTC and 2026-11-22 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T20-20-39-495028Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 19:18:46 | [hryvinskyi/magento2-admin-setup-wizard](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-admin-setup-wizard) | 1.0.0 | Volodymyr Hryvinskyi | A setup-wizard frame for the Magento admin: scopes, settings with inheritance a… |
| 2026-11-22 19:24:46 | [hryvinskyi/magento2-json-template](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-json-template) | 1.0.0 | Volodymyr Hryvinskyi | Compiled JSON templates for Magento 2: a JSON document with {{ expressions }},… |
| 2026-11-22 19:33:35 | [hryvinskyi/magento2-rich-snippets](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-rich-snippets) | 1.0.0 | Volodymyr Hryvinskyi | Rich snippets for Magento 2: JSON-LD blocks written as templates, placed by kin… |
| 2026-11-22 19:47:08 | [agilisdating/agilis-ads](https://www.nuget.org/packages/agilisdating%2Fagilis-ads) | v0.1.0 | Agilis | Official PHP client for the Agilis Advertising REST API: Offers, Events and web… |
| 2026-11-22 19:56:36 | [marekskopal/lithophane](https://www.nuget.org/packages/marekskopal%2Flithophane) | v0.1.0 | Marek Skopal | Generate printable lithophane STL models from images. Library + CLI. |
| 2026-11-22 20:01:29 | [type-lang/mapper-laravel](https://www.nuget.org/packages/type-lang%2Fmapper-laravel) | 2.0.0-beta8 |  | Laravel integration of the TypeLang mapper |
| 2026-11-22 20:01:46 | [type-lang/mapper-symfony](https://www.nuget.org/packages/type-lang%2Fmapper-symfony) | 2.0.0-beta8 |  | Symfony integration of the TypeLang mapper |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
