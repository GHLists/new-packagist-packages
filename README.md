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

## Latest list — 2026-11-26 19:19 UTC

New packages created between 2026-11-26 18:20 UTC and 2026-11-26 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T19-19-06-614702Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 18:29:00 | [betocampoy/champs-sdk-sicredi](https://www.nuget.org/packages/betocampoy%2Fchamps-sdk-sicredi) | v0.1.0 | Beto Campoy | SDK PHP da Champs para a API de Cobrança do Sicredi: boleto tradicional e híbri… |
| 2026-11-26 18:37:34 | [hryvinskyi/magento2-catalog-sorting-price](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-price) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sort options Price: Low to High and Price: High to Low: two Sort By ent… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
