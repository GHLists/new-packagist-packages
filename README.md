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

## Latest list — 2026-11-21 21:19 UTC

New packages created between 2026-11-21 20:22 UTC and 2026-11-21 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T21-19-55-583488Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 20:34:33 | [sendzly/sendzly-php](https://www.nuget.org/packages/sendzly%2Fsendzly-php) | v1.0.0 | Sendzly Team | SDK oficial de Sendzly para PHP y Laravel: envía correos transaccionales (MT 1-… |
| 2026-11-21 20:51:51 | [trail/editor](https://www.nuget.org/packages/trail%2Feditor) | 0.5.0 | Alex Brindley | Markdown and page editor for trail |
| 2026-11-21 20:55:32 | [absdev/laravel-modules](https://www.nuget.org/packages/absdev%2Flaravel-modules) | 1.0.6 | Mark Gregory | Laravel Module Management |
| 2026-11-21 21:02:29 | [yasinkuyu/omnipay-paytr](https://www.nuget.org/packages/yasinkuyu%2Fomnipay-paytr) | v3.0.0 | Yasin Kuyu; Contributors | PayTR gateway for Omnipay: iFrame payment page, signed notification (callback)… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
