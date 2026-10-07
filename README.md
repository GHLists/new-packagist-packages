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

## Latest list — 2026-10-07 09:21 UTC

New packages created between 2026-10-07 08:20 UTC and 2026-10-07 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T09-21-05-22015Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 08:44:01 | [abdulwahhabkhan/laravel-react-starter-kit](https://www.nuget.org/packages/abdulwahhabkhan%2Flaravel-react-starter-kit) | v0.0.2 |  | Laravel React starter kit with opinionated configuration. |
| 2026-10-07 08:44:42 | [wazum/fluid-blocks](https://www.nuget.org/packages/wazum%2Ffluid-blocks) | 1.0.0 | Wolfgang Klinger | Send HTML from content element and plugin templates to named slots in the page… |
| 2026-10-07 08:52:29 | [osd84/aurox](https://www.nuget.org/packages/osd84%2Faurox) | 1.0.0 | osd84.fr | Lib for build web app |
| 2026-10-07 09:02:29 | [peppol-sh/sdk](https://www.nuget.org/packages/peppol-sh%2Fsdk) | v0.1.0 |  | Official PHP SDK for the peppol.sh Peppol API: Peppol e-invoicing (UBL, EN 1693… |
| 2026-10-07 09:08:40 | [msahidurr/laravel-error-notifier](https://www.nuget.org/packages/msahidurr%2Flaravel-error-notifier) | v1.0.0 | msahidurr | Send Laravel exception reports to Telegram and other channels. |
| 2026-10-07 09:15:03 | [gecka/spamfilter](https://www.nuget.org/packages/gecka%2Fspamfilter) | v1.0.0 | Laurent Dinclaux | Statistical spam filter for short user-submitted texts (contact forms, comments… |
| 2026-10-07 09:15:09 | [byte8/module-migration-forecast](https://www.nuget.org/packages/byte8%2Fmodule-migration-forecast) | 0.1.0 | Byte8 Ltd | Forecast what setup:upgrade will do to your Magento 2 database before you run i… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
