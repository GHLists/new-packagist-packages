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

## Latest list — 2026-10-08 05:19 UTC

New packages created between 2026-10-08 04:20 UTC and 2026-10-08 05:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T05-19-06-981686Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 04:23:41 | [inovartecnologia/ofx-simple-parser](https://www.nuget.org/packages/inovartecnologia%2Fofx-simple-parser) | v1.0.0 |  | Leitor OFX 1.x para extratos de conta corrente |
| 2026-10-08 04:51:45 | [mochipay/php-sdk](https://www.nuget.org/packages/mochipay%2Fphp-sdk) | v1.0.0 |  | PHP client for the MochiPay crypto payment order API. |
| 2026-10-08 05:09:29 | [habeuk/habeuk_static_page](https://www.nuget.org/packages/habeuk%2Fhabeuk_static_page) | 1.0.0 | kouwa stephane | Pour les pages static principalement de promotion. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
