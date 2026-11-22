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

## Latest list — 2026-11-22 21:20 UTC

New packages created between 2026-11-22 20:20 UTC and 2026-11-22 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T21-20-25-540979Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 20:25:48 | [delgraf/module-cart-item-image-fix](https://www.nuget.org/packages/delgraf%2Fmodule-cart-item-image-fix) | v1.0.0 | Delgraf | Restores the core data (product_id, ...) on Magento 2 cart item images replaced… |
| 2026-11-22 20:26:03 | [denetorus/galaxy-validation](https://www.nuget.org/packages/denetorus%2Fgalaxy-validation) | v0.1.0 |  | Independent value validation and normalization with explicit type rules. |
| 2026-11-22 20:27:34 | [thud/laravel](https://www.nuget.org/packages/thud%2Flaravel) | v0.1.0 |  | Catch Laravel jobs, scheduled commands and webhooks that report success but did… |
| 2026-11-22 20:49:59 | [avdeb/kirby-avdeb](https://www.nuget.org/packages/avdeb%2Fkirby-avdeb) | 1.0.0 | AVDEB | Show AVDEB products (a creator's shop, a category, a search or a single product… |
| 2026-11-22 21:15:53 | [ashenrayne/ar_docs](https://www.nuget.org/packages/ashenrayne%2Far_docs) | 1.0.1 |  | Hosts Ashen Rayne client docs at private links; recipients answer in any browse… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
