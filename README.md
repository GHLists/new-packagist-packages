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

## Latest list — 2026-11-19 11:19 UTC

New packages created between 2026-11-19 10:21 UTC and 2026-11-19 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T11-19-01-58877Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 10:29:34 | [jiannius/mailog](https://www.nuget.org/packages/jiannius%2Fmailog) | v0.1.0 | TJ | Jiannius Mailog - outgoing email audit logging for Laravel |
| 2026-11-19 10:32:29 | [altayofficial/binaryutils](https://www.nuget.org/packages/altayofficial%2Fbinaryutils) | 0.2.8 |  | Classes and methods for conveniently handling binary data |
| 2026-11-19 10:32:29 | [altayofficial/color](https://www.nuget.org/packages/altayofficial%2Fcolor) | 0.3.2 |  | Color handling library used by PocketMine-MP and related projects |
| 2026-11-19 10:32:29 | [altayofficial/errorhandler](https://www.nuget.org/packages/altayofficial%2Ferrorhandler) | 0.7.2 |  | Utilities to handle nasty PHP E_* errors in a usable way |
| 2026-11-19 10:32:30 | [altayofficial/log](https://www.nuget.org/packages/altayofficial%2Flog) | 0.4.1 |  | Logging components used by PocketMine-MP and related projects |
| 2026-11-19 10:32:30 | [altayofficial/math](https://www.nuget.org/packages/altayofficial%2Fmath) | 1.0.1 |  |  |
| 2026-11-19 10:32:30 | [altayofficial/snooze](https://www.nuget.org/packages/altayofficial%2Fsnooze) | 0.5.1 |  | Thread notification management library for code using the pthreads extension |
| 2026-11-19 10:46:11 | [moduhelp/laravel](https://www.nuget.org/packages/moduhelp%2Flaravel) | v0.1.0 |  | Laravel package that adds the ModuHelp support widget to your HTML pages. |
| 2026-11-19 10:47:26 | [diakonie-sh/dsh-mastodon](https://www.nuget.org/packages/diakonie-sh%2Fdsh-mastodon) | v1.0.0 | Friedemann Altrock | Publish TYPO3 records as Mastodon posts. |
| 2026-11-19 10:50:47 | [net-os/laravel-release-control](https://www.nuget.org/packages/net-os%2Flaravel-release-control) | v0.1.0 |  | Shared maintenance state and client compatibility policy for Laravel deployment… |
| 2026-11-19 10:59:00 | [derkosmonaut/nightmode-contao](https://www.nuget.org/packages/derkosmonaut%2Fnightmode-contao) | v0.1.1 |  | Nachtmodus für Infomonitore in Contao: Inhalte nur während der Öffnungszeiten,… |
| 2026-11-19 11:05:44 | [ajaydhakal/qfpay-sdk](https://www.nuget.org/packages/ajaydhakal%2Fqfpay-sdk) | v1 | Ajay Dhakal | QFPay payment and checkout SDK for Laravel |
| 2026-11-19 11:09:44 | [maxcode/module-popup](https://www.nuget.org/packages/maxcode%2Fmodule-popup) | 1.0.2 |  | EN: Editable welcome popup for Magento 2 - shown once to each new visitor, cont… |
| 2026-11-19 11:14:50 | [survos/connections-contract](https://www.nuget.org/packages/survos%2Fconnections-contract) | 2.45.66 |  | Immutable values for a connections view: nodes, edges with source evidence, and… |
| 2026-11-19 11:14:53 | [survos/connections-bundle](https://www.nuget.org/packages/survos%2Fconnections-bundle) | 2.45.66 |  | Renders a connections graph (survos/connections-contract) as an accessible SVG… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
