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

## Latest list — 2026-11-20 13:22 UTC

New packages created between 2026-11-20 12:19 UTC and 2026-11-20 13:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T13-22-03-918031Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 12:20:00 | [lessormq/client](https://www.nuget.org/packages/lessormq%2Fclient) | v0.1.0 |  | PHP client and worker for LessorMQ, the message queue over HTTP where the serve… |
| 2026-11-20 12:20:05 | [lessormq/messenger](https://www.nuget.org/packages/lessormq%2Fmessenger) | v0.1.0 |  | Symfony Messenger transport for LessorMQ: the queue decides retries, delays and… |
| 2026-11-20 12:23:42 | [hanshs474/aibirthday](https://www.nuget.org/packages/hanshs474%2Faibirthday) | v0.1.0 | AI Birthday Video Generator | AI birthday video generator from a single photo: they pop champagne on a park b… |
| 2026-11-20 12:32:54 | [absdev/laravel-modules](https://www.nuget.org/packages/absdev%2Flaravel-modules) | v1.0.2 | Mark Gregory | Laravel Module Management |
| 2026-11-20 12:32:54 | [spryker/product-attachment-extension](https://www.nuget.org/packages/spryker%2Fproduct-attachment-extension) | 1.0.0 |  | ProductAttachmentExtension module |
| 2026-11-20 12:54:06 | [mr-glubschi/seat-contracts](https://www.nuget.org/packages/mr-glubschi%2Fseat-contracts) | v0.2.0 |  | SeAT plugin: prices of capital ships from contracts in all regions, with one cl… |
| 2026-11-20 12:58:05 | [vlec/laravel-verifactu](https://www.nuget.org/packages/vlec%2Flaravel-verifactu) | v0.1.0 | Ilie | Issue VERI*FACTU invoices from a Laravel app through the Verifactu service. |
| 2026-11-20 13:00:08 | [intelligent-intern/sepa-creator](https://www.nuget.org/packages/intelligent-intern%2Fsepa-creator) | v0.1.1 |  | SEPA transfers, direct debits and payment status reading with exact amounts and… |
| 2026-11-20 13:07:07 | [wearejust/statamic-video-storage](https://www.nuget.org/packages/wearejust%2Fstatamic-video-storage) | 0.0.1 |  |  |
| 2026-11-20 13:10:25 | [enigmoss/php-sdk](https://www.nuget.org/packages/enigmoss%2Fphp-sdk) | v1.0.0 |  | Official PHP SDK for the Enigmoss Project API v4: payments, static wallets, pay… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
