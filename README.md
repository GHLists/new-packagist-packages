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

## Latest list — 2026-11-06 11:20 UTC

New packages created between 2026-11-06 10:19 UTC and 2026-11-06 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T11-20-06-545159Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 10:26:17 | [pdir/contao-matomo-ai-tracking](https://www.nuget.org/packages/pdir%2Fcontao-matomo-ai-tracking) | 1.0.0 | pdir GmbH; Mathias Arzberger | Serverseitiges Tracking von AI-Chatbots (ChatGPT-User, Claude-User, Perplexity-… |
| 2026-11-06 10:30:00 | [raylongsolutions/gst-gateway](https://www.nuget.org/packages/raylongsolutions%2Fgst-gateway) | v1.0.0 | Raylong Solutions | Generate GST e-invoices (IRN) and e-way bills from PHP with GST Gateway by Rayl… |
| 2026-11-06 10:31:48 | [chaima24/algeria-geo-laravel](https://www.nuget.org/packages/chaima24%2Falgeria-geo-laravel) | v1.0.0 | chaima24 | Algerian geography for Laravel: 69 wilayas and 1,541 communes, with optional re… |
| 2026-11-06 10:43:23 | [cgv/localized-resource](https://www.nuget.org/packages/cgv%2Flocalized-resource) | v1.0.0 |  | Comando para crear recursos localizados de Filament |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
