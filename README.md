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

## Latest list — 2026-10-29 12:21 UTC

New packages created between 2026-10-29 11:19 UTC and 2026-10-29 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T12-21-59-552772Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 11:33:54 | [islam016/arabic-search](https://www.nuget.org/packages/islam016%2Farabic-search) | v1.0.0 | Islam Gaber | Arabic-aware text normalization and search for PHP and Laravel: find "أحمد" whe… |
| 2026-10-29 11:34:43 | [se7enxweb/exponential-php-floor](https://www.nuget.org/packages/se7enxweb%2Fexponential-php-floor) | 1.3.0 |  | Lets Exponential 6.0.15 and later install on every PHP version it supports (7.4… |
| 2026-10-29 11:41:48 | [senanthewnaka/lanka-kit](https://www.nuget.org/packages/senanthewnaka%2Flanka-kit) | v1.2.0 | Senan Thewnaka | Sri Lankan developer toolkit for PHP & Laravel: NIC, Phone, Banks, Currency, Li… |
| 2026-10-29 11:44:33 | [hardcastle/xahau-php](https://www.nuget.org/packages/hardcastle%2Fxahau-php) | 1.0.0 | Alexander Busse | PHP SDK / Client for the Xahau Network, built on hardcastle/xrpl_php |
| 2026-10-29 11:46:41 | [wpelevator/php-changesets](https://www.nuget.org/packages/wpelevator%2Fphp-changesets) | 0.1.1 |  | Changeset-based release preparation for PHP projects |
| 2026-10-29 12:06:13 | [quebracho/x402](https://www.nuget.org/packages/quebracho%2Fx402) | v0.1.0 |  | x402 payments for PHP: EIP-712/EIP-3009 signing, PSR-15 middleware and PSR-18 p… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
