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

## Latest list — 2026-11-19 16:19 UTC

New packages created between 2026-11-19 15:20 UTC and 2026-11-19 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T16-19-09-088636Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 15:22:52 | [webwizardsusa/filament-table-layouts](https://www.nuget.org/packages/webwizardsusa%2Ffilament-table-layouts) | v0.1.0 | Jamie Holly | Let people switch a Filament table between a table and a card grid, with an ima… |
| 2026-11-19 15:33:20 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.36.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-19 15:36:39 | [threadlive/threadlive-laravel](https://www.nuget.org/packages/threadlive%2Fthreadlive-laravel) | v0.1.0 | Mikhail Kovchuk | Threadlive — live chat in Telegram threads. The Laravel side: the widget's API,… |
| 2026-11-19 15:42:06 | [neuronaptiq/magento-search](https://www.nuget.org/packages/neuronaptiq%2Fmagento-search) | 2.1.1 |  | Semantic search for Magento 2 powered by the NeuronaptiQ search API |
| 2026-11-19 15:54:20 | [neuronaptiq/magento-search-elasticsuite](https://www.nuget.org/packages/neuronaptiq%2Fmagento-search-elasticsuite) | 2.0.0 |  | Smile ElasticSuite integration of the NeuronaptiQ semantic search for Magento 2 |
| 2026-11-19 16:05:58 | [88pay/webhooks](https://www.nuget.org/packages/88pay%2Fwebhooks) | v1.0.0 |  | Verify notifications (webhooks) sent by 88Pay: HMAC-SHA256 signature, timestamp… |
| 2026-11-19 16:17:18 | [veltra/veltra-laravel](https://www.nuget.org/packages/veltra%2Fveltra-laravel) | v1.0.0 | Veltra Ecosystem Team | Enterprise Admin Dashboard UI Suite for Laravel 10, 11, 12 and 13 powered by Ta… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
