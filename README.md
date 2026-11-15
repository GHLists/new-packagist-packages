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

## Latest list — 2026-11-15 21:22 UTC

New packages created between 2026-11-15 20:19 UTC and 2026-11-15 21:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T21-22-14-873848Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 20:31:01 | [willwright/module-category-sorting](https://www.nuget.org/packages/willwright%2Fmodule-category-sorting) | v1.0.1 |  | Magento 2 category sorting by stock availability, paid sales, review rating and… |
| 2026-11-15 20:37:23 | [but-mmi-beziers/babel-moteur](https://www.nuget.org/packages/but-mmi-beziers%2Fbabel-moteur) | v1.0.0 |  | Moteur de la Bibliothèque de Babel : permutation à clé entre adresses et pages… |
| 2026-11-15 20:38:20 | [shmuelakam/greenjeans](https://www.nuget.org/packages/shmuelakam%2Fgreenjeans) | v0.8.0 | Shmuel A. Kam | PHP SDK and persistence layer for Geni.com API |
| 2026-11-15 20:48:58 | [tomvondracek/bolt-request-analytics](https://www.nuget.org/packages/tomvondracek%2Fbolt-request-analytics) | v1.0.0 | Tomáš Vondráček | Cookieless, server-side visitor statistics for Bolt CMS 6, built only from the… |
| 2026-11-15 21:12:08 | [abitechdev/antibot-laravel](https://www.nuget.org/packages/abitechdev%2Fantibot-laravel) | v1.0.1 | Abimael Fernandez | Protege los formularios de Laravel contra bots con Cloudflare Turnstile o Googl… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
