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

## Latest list — 2026-10-21 16:21 UTC

New packages created between 2026-10-21 15:22 UTC and 2026-10-21 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T16-21-39-707782Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 15:28:49 | [rivalex/lingua](https://www.nuget.org/packages/rivalex%2Flingua) | v2.1.1 | Alessandro Rivolta | Self-hosted Laravel translation manager for the TALL stack: edit, sync, import/… |
| 2026-10-21 15:33:02 | [keel/skeleton](https://www.nuget.org/packages/keel%2Fskeleton) | v1.0.1 |  | Project template for the Keel micro-framework: composer create-project keel/ske… |
| 2026-10-21 15:34:17 | [ad-go/sync](https://www.nuget.org/packages/ad-go%2Fsync) | v0.0.1 | k | Active-active database synchronisation for two CodeIgniter 4 instances over HTT… |
| 2026-10-21 15:36:30 | [pixelfix/installer](https://www.nuget.org/packages/pixelfix%2Finstaller) | 0.1.0 |  | Global CLI installer for PixelFix applications |
| 2026-10-21 15:42:05 | [gvargas/atusan-cli](https://www.nuget.org/packages/gvargas%2Fatusan-cli) | v1.0 |  | Command Line Interface for ATUSAN 3 |
| 2026-10-21 16:02:01 | [hanane/idempotency-guard-bundle](https://www.nuget.org/packages/hanane%2Fidempotency-guard-bundle) | v0.1.0 | Hanane | Idempotency keys and safe response replay for selected Symfony HTTP operations. |
| 2026-10-21 16:05:52 | [dragonbytetech/phpstan-xenforo](https://www.nuget.org/packages/dragonbytetech%2Fphpstan-xenforo) | 1.0.0 | Fillip H. | PHPStan extension for analysing XenForo 2.3 add-ons without false positives fro… |
| 2026-10-21 16:08:10 | [wizniche/wizpay-checkout-sdk](https://www.nuget.org/packages/wizniche%2Fwizpay-checkout-sdk) | v0.1.2 | WIZPay | Server SDK for WIZPay Checkout: create checkout sessions and verify webhooks. |
| 2026-10-21 16:08:22 | [hryvinskyi/magento2-activity-log](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-activity-log) | 1.0.0 | Volodymyr Hryvinskyi | One journal of who did what in the store back office, through which channel and… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
