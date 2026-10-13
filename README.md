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

## Latest list — 2026-10-13 00:19 UTC

New packages created between 2026-10-12 23:19 UTC and 2026-10-13 00:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T00-19-45-794675Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 23:26:17 | [sifadi/core](https://www.nuget.org/packages/sifadi%2Fcore) | 1.0.0 | Sifadi | SDK PHP (framework-agnostic) para la API de Sifadi: timbra CFDI 4.0, cancela, d… |
| 2026-10-12 23:26:24 | [sifadi/laravel](https://www.nuget.org/packages/sifadi%2Flaravel) | v1.0.0 | Sifadi | Integración de Sifadi para Laravel: ServiceProvider, Facade y config sobre el S… |
| 2026-10-12 23:44:41 | [wilycode/database-query-executor](https://www.nuget.org/packages/wilycode%2Fdatabase-query-executor) | v0.1.0 | Simon Piter | Lightweight query execution layer connecting WilyCode SQL queries, binders and… |
| 2026-10-12 23:46:45 | [mykholy/laravel-accessproof](https://www.nuget.org/packages/mykholy%2Flaravel-accessproof) | v1.0.1 | Ahmed El-Kholy | Catch Laravel authorization regressions, IDOR/BOLA, cross-tenant leaks and unau… |
| 2026-10-13 00:01:52 | [wilycode/database-query-executor-cache](https://www.nuget.org/packages/wilycode%2Fdatabase-query-executor-cache) | v0.1.0 | Simon Piter | PSR-16 caching decorator for WilyCode database query executors with transaction… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
