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

## Latest list — 2026-11-19 03:19 UTC

New packages created between 2026-11-19 02:22 UTC and 2026-11-19 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T03-19-47-462607Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 02:37:32 | [pushinbr/nimbus](https://www.nuget.org/packages/pushinbr%2Fnimbus) | v0.1.0 |  | Nimbus: the API-first PHP framework for the PAM runtime. |
| 2026-11-19 02:49:32 | [queen-one/module-connect](https://www.nuget.org/packages/queen-one%2Fmodule-connect) | v1.0.0 |  | Queen One Connect for Magento 2 |
| 2026-11-19 02:58:33 | [content-true/live-swap-face-frame-audit](https://www.nuget.org/packages/content-true%2Flive-swap-face-frame-audit) | v0.1.0 |  | Compare sampled RGB frames and flag abrupt visual changes for manual video revi… |
| 2026-11-19 03:01:05 | [content-true/bank-file-tool-reconciliation](https://www.nuget.org/packages/content-true%2Fbank-file-tool-reconciliation) | v0.1.0 |  | Reconcile normalized bank-statement CSV rows with opening and closing balances |
| 2026-11-19 03:03:38 | [content-true/image-unblur-pixel-compare](https://www.nuget.org/packages/content-true%2Fimage-unblur-pixel-compare) | v0.1.0 |  | Measure pixel changes between aligned original and restored RGB images |
| 2026-11-19 03:17:13 | [bijayx/nepal-pay-laravel](https://www.nuget.org/packages/bijayx%2Fnepal-pay-laravel) | v0.1.0 | Bijay Shrestha | Khalti and eSewa payment gateways for Laravel behind one typed, verified API. |
| 2026-11-19 03:17:18 | [bijayx/iap-guard-laravel](https://www.nuget.org/packages/bijayx%2Fiap-guard-laravel) | v0.1.0 | Bijay Shrestha | Server-side verification and ownership protection for Apple App Store and Googl… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
