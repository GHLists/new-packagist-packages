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

## Latest list — 2026-11-13 12:20 UTC

New packages created between 2026-11-13 11:19 UTC and 2026-11-13 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T12-20-51-996785Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 11:21:38 | [standa/diseval](https://www.nuget.org/packages/standa%2Fdiseval) | 0.3.1 |  | Disables eval() in PHP 8 (PIE-installable wrapper around mk-j/PHP_diseval_exten… |
| 2026-11-13 11:23:20 | [nonini/db-migration](https://www.nuget.org/packages/nonini%2Fdb-migration) | v0.2.0 |  | Simple DB migration helper |
| 2026-11-13 11:26:55 | [renatomaldonado/laravel-mcp-docs](https://www.nuget.org/packages/renatomaldonado%2Flaravel-mcp-docs) | v0.1.2 |  | Generate a browsable documentation page for your Laravel MCP servers: tools, re… |
| 2026-11-13 11:33:44 | [druidfi/symfony-minor-pin](https://www.nuget.org/packages/druidfi%2Fsymfony-minor-pin) | 8.1.0 |  | Keeps every Symfony component on the 8.1 line without Symfony Flex (e.g. for Re… |
| 2026-11-13 11:49:34 | [lakedrops/docker4php](https://www.nuget.org/packages/lakedrops%2Fdocker4php) | 1.0.0 | Jürgen Haas; Richard Papp | Composer Plugin to prepare local PHP/Apache development environment for Docker. |
| 2026-11-13 11:50:53 | [flexiapp/api-connector-v2](https://www.nuget.org/packages/flexiapp%2Fapi-connector-v2) | v1.0.0 | Josef Burger | PHP connector for the FlexiApp headless CMS REST API v2: read access, file cach… |
| 2026-11-13 12:00:15 | [concept-image/laravel-checks](https://www.nuget.org/packages/concept-image%2Flaravel-checks) | 1.1.0 | Aurélien Cellier | Laravel Checks: extra Spatie Laravel Health checks (public directory, public/in… |
| 2026-11-13 12:04:28 | [mertaydin/elasticsearch-monitoring](https://www.nuget.org/packages/mertaydin%2Felasticsearch-monitoring) | v0.1.0 |  | A Laravel dashboard and metric collector for Elasticsearch clusters. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
