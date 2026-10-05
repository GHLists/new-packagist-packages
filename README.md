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

## Latest list — 2026-10-05 08:21 UTC

New packages created between 2026-10-05 07:20 UTC and 2026-10-05 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T08-21-21-701512Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 07:58:29 | [projek-xyz/callable](https://www.nuget.org/packages/projek-xyz%2Fcallable) | v0.1.0 | Fery Wardiyanto | Auto-wire and invoke any callable through PSR-11 |
| 2026-10-05 08:00:46 | [jishan-shk/laravel-databricks](https://www.nuget.org/packages/jishan-shk%2Flaravel-databricks) | v1.0.0 | Jishan | Databricks SQL client for Laravel over ODBC (Simba Spark / Databricks ODBC driv… |
| 2026-10-05 08:12:16 | [survos/folio](https://www.nuget.org/packages/survos%2Ffolio) | 2.35.4 |  | Framework-free SQLite folio metadata reader and migration adapter. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
