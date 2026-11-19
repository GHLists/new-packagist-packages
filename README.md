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

## Latest list — 2026-11-19 14:21 UTC

New packages created between 2026-11-19 13:20 UTC and 2026-11-19 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T14-21-17-537618Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 13:21:39 | [fisharebest/figlet](https://www.nuget.org/packages/fisharebest%2Ffiglet) | 1.0.0 | Greg Roach | A zero-dependency PHP library and CLI for rendering FIGlet text banners. |
| 2026-11-19 13:26:45 | [market-media/plates](https://www.nuget.org/packages/market-media%2Fplates) | v1.0.0 |  | Plates, o sistema de templates nativo do PHP que é rápido, fácil de usar e fáci… |
| 2026-11-19 13:27:07 | [baldie81/magento2-sdk](https://www.nuget.org/packages/baldie81%2Fmagento2-sdk) | v1.0.0 | baldie81 | Framework-independent PHP SDK for the Magento 2 REST API: products, attributes,… |
| 2026-11-19 13:42:34 | [stolt/hyde-reading-time](https://www.nuget.org/packages/stolt%2Fhyde-reading-time) | v0.9.0 | Raphael Stolt | Estimated Markdown reading times for HydePHP pages. |
| 2026-11-19 13:55:34 | [portalcurso/php-template](https://www.nuget.org/packages/portalcurso%2Fphp-template) | v1.0.0 | Edivan Fontes | Sistema de templates nativo em PHP puro (7.4+), inspirado no League Plates: lay… |
| 2026-11-19 14:01:23 | [eii/filament-language-switch](https://www.nuget.org/packages/eii%2Ffilament-language-switch) | v1.0.0 |  | Filament topbar language switcher plugin |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
