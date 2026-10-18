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

## Latest list — 2026-10-18 21:19 UTC

New packages created between 2026-10-18 20:19 UTC and 2026-10-18 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T21-19-26-158321Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 20:27:52 | [loggerai/laravel](https://www.nuget.org/packages/loggerai%2Flaravel) | v0.1.0 |  | LoggerAI for Laravel: performance monitoring, errors, logs, alerts and user ses… |
| 2026-10-18 20:44:30 | [perplorm/perpl-bundle](https://www.nuget.org/packages/perplorm%2Fperpl-bundle) | v1.0.0-RC1 | William Durand | Integration of Propel and Perpl in Symfony |
| 2026-10-18 21:01:25 | [iperson1337/nct-client-bundle](https://www.nuget.org/packages/iperson1337%2Fnct-client-bundle) | v1.0.0 |  | Symfony client for the National Catalog of Goods of Kazakhstan (НКТ): nationalc… |
| 2026-10-18 21:01:34 | [perata-sh/sdk](https://www.nuget.org/packages/perata-sh%2Fsdk) | v0.1.1 |  | Peráta's SDK for PHP: products, customers, checkouts, payments, subscriptions a… |
| 2026-10-18 21:03:26 | [stoneholl/module-admin-accent-color](https://www.nuget.org/packages/stoneholl%2Fmodule-admin-accent-color) | v1.2.0 |  | Safe per-area and per-administrator accent colors for the standard Magento Admi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
