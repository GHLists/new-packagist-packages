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

## Latest list — 2026-11-19 09:20 UTC

New packages created between 2026-11-19 08:19 UTC and 2026-11-19 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T09-20-44-51026Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 08:26:42 | [formfeed/laravel](https://www.nuget.org/packages/formfeed%2Flaravel) | v0.3.28 | Formfeed | Formfeed for Laravel: the API client from config/formfeed.php, the Formfeed fac… |
| 2026-11-19 08:26:42 | [formfeed/sdk](https://www.nuget.org/packages/formfeed%2Fsdk) | v0.3.28 | Formfeed | PHP client for the Formfeed API: PDFs and images from templates, HTML or URLs,… |
| 2026-11-19 08:48:18 | [chunkify/chunkify-analytics-php](https://www.nuget.org/packages/chunkify%2Fchunkify-analytics-php) | v0.9.0 |  | Chunkify Analytics PHP SDK |
| 2026-11-19 08:52:15 | [dskripchenko/laravel-telemetry](https://www.nuget.org/packages/dskripchenko%2Flaravel-telemetry) | v0.2.0 | Denis Skripchenko | Performance telemetry for Laravel without an agent or a database: a Server-Timi… |
| 2026-11-19 08:57:19 | [showmac/pay-sdk](https://www.nuget.org/packages/showmac%2Fpay-sdk) | v1.0.0 |  | ShowMac 支付网关 PHP 客户端 |
| 2026-11-19 09:03:46 | [specialistaweb/rss-news-import](https://www.nuget.org/packages/specialistaweb%2Frss-news-import) | 2.0.1 | Giulia Tuveri | Imports external RSS/Atom feeds into EXT:news via the Scheduler and SimplePie,… |
| 2026-11-19 09:06:08 | [dashed/dashed-cookies](https://www.nuget.org/packages/dashed%2Fdashed-cookies) | v4.0.1 | Robin van Maasakker | Cookie consent, cookie overview and consent logging for Dashed CMS |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
