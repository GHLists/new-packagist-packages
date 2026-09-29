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

## Latest list — 2026-09-29 12:22 UTC

New packages created between 2026-09-29 11:20 UTC and 2026-09-29 12:22 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T12-22-41-729372Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 11:22:12 | [odemehub/php-sdk](https://www.nuget.org/packages/odemehub%2Fphp-sdk) | v1.0.0 |  | ödemehub ödeme geçidi için PHP istemcisi. |
| 2026-09-29 11:31:57 | [notideus/notideus-php](https://www.nuget.org/packages/notideus%2Fnotideus-php) | 1.0.0 |  | Official PHP SDK for the Notideus email API |
| 2026-09-29 11:42:29 | [quaxis/hello](https://www.nuget.org/packages/quaxis%2Fhello) | v0.1.0 | Yusuf Özdemir | Quaxis example package. |
| 2026-09-29 11:54:27 | [dhank77/qris-dinamis](https://www.nuget.org/packages/dhank77%2Fqris-dinamis) | v1.0.0 | M. Hamdani Ilham Latjoro; Gid… | Convert static QRIS to dynamic QRIS in PHP: parse, validate, inject amount & se… |
| 2026-09-29 11:56:18 | [php-io-extensions/kqueue](https://www.nuget.org/packages/php-io-extensions%2Fkqueue) | v0.10.0 | Project Saturn Studios, LLC | 1:1 PHP bindings of kqueue(2): kqueue(), kevent(), kevent64(), EV_SET(), EV_SET… |
| 2026-09-29 12:04:35 | [ventusforge/neos-token-auth-manager](https://www.nuget.org/packages/ventusforge%2Fneos-token-auth-manager) | 0.2.0 |  | Backend Module to manage auth tokens for Neos |
| 2026-09-29 12:08:11 | [ffans/community-notes](https://www.nuget.org/packages/ffans%2Fcommunity-notes) | v2.0.0-beta.1 | Golden; FFans | Let the community add and rate notes that provide context for potentially misle… |
| 2026-09-29 12:09:32 | [vibefilter/filament](https://www.nuget.org/packages/vibefilter%2Ffilament) | v0.1.0 | András Horváth | Filter your Filament tables by vibe: natural-language table filters powered by… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
