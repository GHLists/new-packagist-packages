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

## Latest list — 2026-10-16 15:20 UTC

New packages created between 2026-10-16 14:20 UTC and 2026-10-16 15:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T15-20-21-382625Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 14:22:47 | [stoyishi/checkout-uz](https://www.nuget.org/packages/stoyishi%2Fcheckout-uz) | 2.0.0 | Hasanov Otabek | Checkout.uz payment gateway PHP SDK |
| 2026-10-16 14:23:18 | [saucebase/coming-soon](https://www.nuget.org/packages/saucebase%2Fcoming-soon) | v0.1.1 | Saucebase | A configurable coming soon page and site access gate for Saucebase. |
| 2026-10-16 14:31:31 | [ldkafka/yii3-google-firestore](https://www.nuget.org/packages/ldkafka%2Fyii3-google-firestore) | v0.1.0 | ldkafka | Google Cloud Firestore for PHP 8.4 / Yii3 over the REST API, without gRPC or th… |
| 2026-10-16 14:34:58 | [lathe/lathe](https://www.nuget.org/packages/lathe%2Flathe) | v1.0.0-beta.1 |  | Admin panel builder for Laravel on Inertia, React and shadcn/ui. |
| 2026-10-16 14:37:35 | [tmonier/sylius-channel-access-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-channel-access-plugin) | v0.1.0 | Thibaut Monier | Per-channel access mode for Sylius 2 (open, prices hidden, closed): anonymous v… |
| 2026-10-16 14:51:19 | [laminas/internal-tooling](https://www.nuget.org/packages/laminas%2Finternal-tooling) | 1.0.0 |  | Internal tooling configuration and defaults for Laminas and Mezzio projects |
| 2026-10-16 14:54:17 | [kipchak/driver-sftp](https://www.nuget.org/packages/kipchak%2Fdriver-sftp) | 1.0 |  | An SFTP driver for exchanging files with partners and other systems from the Ki… |
| 2026-10-16 14:54:23 | [tmonier/sylius-registration-approval-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-registration-approval-plugin) | v0.1.0 | Thibaut Monier | Registration approval for Sylius 2: accounts registered on a channel stay pendi… |
| 2026-10-16 15:07:12 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.5.9 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-16 15:10:08 | [amtgard/host-env-vault](https://www.nuget.org/packages/amtgard%2Fhost-env-vault) | v0.1.0 |  | Runtime-mode unix socket client for host-env-vault profiles. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
