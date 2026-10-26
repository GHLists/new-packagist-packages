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

## Latest list — 2026-10-26 10:20 UTC

New packages created between 2026-10-26 09:21 UTC and 2026-10-26 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T10-20-32-773237Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 09:28:52 | [elx/chatbot-connector](https://www.nuget.org/packages/elx%2Fchatbot-connector) | v1.0.1 | Elx | ELX Chatbot Connector for Maho - product feed generation and order data sync fo… |
| 2026-10-26 09:29:45 | [atannex/detector](https://www.nuget.org/packages/atannex%2Fdetector) | v1.0.0 | Atanga Leke Collins | Device, OS, browser and bot detection for Laravel: User-Agent and Client Hints… |
| 2026-10-26 09:35:36 | [atannex/limiting](https://www.nuget.org/packages/atannex%2Flimiting) | v1.0.0 | Atanga Leke Collins | Rate limiting for Laravel, built for security: seven atomic algorithms (sliding… |
| 2026-10-26 09:41:47 | [survos/nara-bundle](https://www.nuget.org/packages/survos%2Fnara-bundle) | 2.43.19 |  | Symfony integration for the National Archives Catalog client: env-configured ke… |
| 2026-10-26 09:41:52 | [survos/nara-client](https://www.nuget.org/packages/survos%2Fnara-client) | 2.43.19 | Tac Tacelosky; Survos | PHP client for the National Archives Catalog API v2: search, records, and contr… |
| 2026-10-26 09:48:15 | [azuradara/logonymic](https://www.nuget.org/packages/azuradara%2Flogonymic) | v0.1.1 |  | Recompute and match nymic browser fingerprints on the server |
| 2026-10-26 10:13:54 | [oocscommerce/magento2-lynx-community](https://www.nuget.org/packages/oocscommerce%2Fmagento2-lynx-community) | 1.0.0 |  | Metapackage with Lynx themes and modules for Magento 2 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
