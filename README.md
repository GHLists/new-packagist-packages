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

## Latest list — 2026-11-24 14:22 UTC

New packages created between 2026-11-24 13:20 UTC and 2026-11-24 14:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T14-22-04-409643Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 13:47:03 | [jelix/ldapadmin-module](https://www.nuget.org/packages/jelix%2Fldapadmin-module) | v1.0.0-rc.1 | Laurent Jouanneau | Module for Jelix, displaying an interface to manage an LDAP configuration used… |
| 2026-11-24 13:49:47 | [avaro/sdk](https://www.nuget.org/packages/avaro%2Fsdk) | v1.0.0 | Jan Habbo Brüning | PHP SDK for the Avaro API v3: shop catalog, customer sign-in, quotes, orders, i… |
| 2026-11-24 13:59:21 | [scalecommerce/videooptimizer-typo3](https://www.nuget.org/packages/scalecommerce%2Fvideooptimizer-typo3) | v1.0.2 | ScaleCommerce GmbH | Integrates ScaleCommerce VideoOptimizer into TYPO3: pick, upload and manage CDN… |
| 2026-11-24 14:05:43 | [qdpops/breeze](https://www.nuget.org/packages/qdpops%2Fbreeze) | v1.1.0 |  | Breeze: a light, modern skin for Roundcube 1.6 (date groups, attachment chips,… |
| 2026-11-24 14:05:43 | [qdpops/tw-folders](https://www.nuget.org/packages/qdpops%2Ftw-folders) | v1.1.0 |  | Companion plugin for the Breeze skin: folder icons and colors, folder rules wit… |
| 2026-11-24 14:07:52 | [communiqate/communiqate-php](https://www.nuget.org/packages/communiqate%2Fcommuniqate-php) | v0.1.0 |  | Framework-independent PHP SDK for the CommuniQate Workspaces API and webhooks. |
| 2026-11-24 14:08:58 | [communiqate/communiqate-laravel](https://www.nuget.org/packages/communiqate%2Fcommuniqate-laravel) | v0.1.1 |  | Laravel mail, notifications, facade and webhook integration for CommuniQate Wor… |
| 2026-11-24 14:12:04 | [brikdigital/craft-queue-monitor](https://www.nuget.org/packages/brikdigital%2Fcraft-queue-monitor) | 1.0.0 |  |  |
| 2026-11-24 14:14:39 | [limegreentangerine/svelte-builder](https://www.nuget.org/packages/limegreentangerine%2Fsvelte-builder) | 0.0.0 | Lee Jones |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
