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

## Latest list — 2026-10-19 12:20 UTC

New packages created between 2026-10-19 11:22 UTC and 2026-10-19 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T12-20-21-001597Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 11:22:39 | [dmitriy-zhukov/otus-composer-package](https://www.nuget.org/packages/dmitriy-zhukov%2Fotus-composer-package) | 1.0.0 | Дмитрий Жуков | test package |
| 2026-10-19 11:25:21 | [emitwave/php](https://www.nuget.org/packages/emitwave%2Fphp) | v0.1.0 | EmitWave | EmitWave server publish SDK (framework-free). |
| 2026-10-19 11:28:10 | [emitwave/laravel](https://www.nuget.org/packages/emitwave%2Flaravel) | v0.1.0 | EmitWave | EmitWave broadcasting driver for Laravel. |
| 2026-10-19 11:30:49 | [wapplersystems/t3-pricing](https://www.nuget.org/packages/wapplersystems%2Ft3-pricing) | 0.2.0 | Sven Wappler | Pricing tables for TYPO3 — plan cards, comparison table and compact rows from o… |
| 2026-10-19 11:35:52 | [petecoop/protec](https://www.nuget.org/packages/petecoop%2Fprotec) | 0.1.0 | Pete Cooper | Extensible suspicious activity detection and temporary IP blocks for Laravel an… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
