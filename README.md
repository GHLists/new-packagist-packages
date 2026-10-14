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

## Latest list — 2026-10-14 23:20 UTC

New packages created between 2026-10-14 22:22 UTC and 2026-10-14 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T23-20-20-061028Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 22:36:40 | [pushinbr/pam-native-svg](https://www.nuget.org/packages/pushinbr%2Fpam-native-svg) | v0.1.0 |  | Native SVG for PAM Native: retained vector nodes, gradients, dashes and render-… |
| 2026-10-14 22:54:12 | [gosimple/rs-fiscal](https://www.nuget.org/packages/gosimple%2Frs-fiscal) | v0.1.0 | GoSimple | Serbian fiscal helpers for PHP: PIB (tax ID) validation and NBS IPS QR code gen… |
| 2026-10-14 23:01:53 | [gosimple/tezga-laravel](https://www.nuget.org/packages/gosimple%2Ftezga-laravel) | v0.1.0 | GoSimple | Laravel integration for the Tezga Fiscal API: config, a Tezga facade, and a sig… |
| 2026-10-14 23:11:56 | [paygate-to/paygate-php](https://www.nuget.org/packages/paygate-to%2Fpaygate-php) | v1.0.0 |  | PHP SDK for PayGate.to: card and crypto payments without KYC, instant payouts t… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
