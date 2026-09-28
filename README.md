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

## Latest list — 2026-09-28 15:21 UTC

New packages created between 2026-09-28 14:20 UTC and 2026-09-28 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T15-21-38-098285Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 14:36:02 | [quoyer/quoyer-php](https://www.nuget.org/packages/quoyer%2Fquoyer-php) | v1.0.0 | Quoyer | Official PHP SDK for the Quoyer loyalty API: customers, points, redemptions, we… |
| 2026-09-28 15:01:24 | [merkushin/wpal](https://www.nuget.org/packages/merkushin%2Fwpal) | 0.7.0 | Dmitry Merkushin | Provides an abstraction layer for WordPress API |
| 2026-09-28 15:05:23 | [ronald-ph/strong-pass](https://www.nuget.org/packages/ronald-ph%2Fstrong-pass) | v1.0.0 | Ronald PH | Framework-neutral PHP password strength checking with optional Laravel integrat… |
| 2026-09-28 15:13:06 | [featvalue/typo3](https://www.nuget.org/packages/featvalue%2Ftypo3) | 0.1.3 | FeatValue | Embeds the FeatValue client portal in a TYPO3 website. |
| 2026-09-28 15:15:32 | [wonittecnologia/interage-sdk-php](https://www.nuget.org/packages/wonittecnologia%2Finterage-sdk-php) | v0.1.0 | Wonit Tecnologia da Informação | SDK PHP oficial da API pública de clientes da plataforma Interage+ (Wonit). |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
