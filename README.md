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

## Latest list — 2026-11-02 22:20 UTC

New packages created between 2026-11-02 21:21 UTC and 2026-11-02 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T22-20-45-800016Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 21:25:01 | [owebstudio/kirby-analytics](https://www.nuget.org/packages/owebstudio%2Fkirby-analytics) | 1.0.0 | oweb studio | Self-hosted, cookieless visitor statistics for Kirby with a native Panel dashbo… |
| 2026-11-02 22:04:56 | [refberg/sylius-payu-plugin](https://www.nuget.org/packages/refberg%2Fsylius-payu-plugin) | v1.0.0 | Refberg | PayU REST API payment gateway for Sylius 2, built on Payment Requests (no Payum… |
| 2026-11-02 22:05:12 | [sharkyphp/contracts](https://www.nuget.org/packages/sharkyphp%2Fcontracts) | v2.0.0 | bytesharky | SharkyPHP contracts, shared interfaces for framework components. |
| 2026-11-02 22:10:48 | [pkoutsogiannis/ucache](https://www.nuget.org/packages/pkoutsogiannis%2Fucache) | v1.1.0 | Periklis Koutsogiannis | A shared-memory key-value cache for PHP 7.2 to 8.5 on Windows x64 (IIS, FastCGI… |
| 2026-11-02 22:13:36 | [ahmedelsied/filament-media-browser](https://www.nuget.org/packages/ahmedelsied%2Ffilament-media-browser) | v1.0.0 |  | Filament media browser with a default driver and a Spatie Media driver. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
