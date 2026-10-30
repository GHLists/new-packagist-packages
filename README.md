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

## Latest list — 2026-10-30 17:21 UTC

New packages created between 2026-10-30 16:19 UTC and 2026-10-30 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T17-21-08-891708Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 16:25:33 | [maristas/sigem-api-client](https://www.nuget.org/packages/maristas%2Fsigem-api-client) | 0.1.0 |  | Cliente HTTP con cache para consumir la API SSO de SIGEM desde sistemas perifer… |
| 2026-10-30 17:04:19 | [owebstudio/kirby-license](https://www.nuget.org/packages/owebstudio%2Fkirby-license) | 1.0.0 | oweb studio | LemonSqueezy license keys for the paid oweb studio plugins for Kirby |
| 2026-10-30 17:06:36 | [survos/ai-duckdb-store](https://www.nuget.org/packages/survos%2Fai-duckdb-store) | 2.45.9 | Christopher Hertel; Oskar Sta… | DuckDB vector store bridge for Symfony AI |
| 2026-10-30 17:12:12 | [akawaka/sylius-seo-plugin](https://www.nuget.org/packages/akawaka%2Fsylius-seo-plugin) | v0.1.0 |  | SEO for Sylius 2: meta tags, canonical, hreflang, Open Graph and Twitter cards… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
