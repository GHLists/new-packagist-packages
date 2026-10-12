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

## Latest list — 2026-10-12 20:21 UTC

New packages created between 2026-10-12 19:19 UTC and 2026-10-12 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T20-21-17-899336Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 19:23:16 | [tmonier/sylius-b2b-mcp-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-b2b-mcp-plugin) | v1.0.0 | Thibaut Monier | B2B tools for the official Sylius MCP server: signed-in buyers use Claude or Ch… |
| 2026-10-12 19:31:50 | [roadrunner/cli](https://www.nuget.org/packages/roadrunner%2Fcli) | 3.0.0 | Anton Titov; RoadRunner Commu… | RoadRunner command-line tool: downloads the RoadRunner binary and generates its… |
| 2026-10-12 19:47:45 | [wilycode/container](https://www.nuget.org/packages/wilycode%2Fcontainer) | v0.1.0 | Simon Piter | Lightweight PSR-11 dependency injection container with explicit factories and c… |
| 2026-10-12 19:49:05 | [korioinc/laravel-expo-integrity](https://www.nuget.org/packages/korioinc%2Flaravel-expo-integrity) | v1.0.0 | korioinc | Verify Expo request HMAC signatures and prevent replay in Laravel with file or… |
| 2026-10-12 20:11:06 | [wilycode/cache-file](https://www.nuget.org/packages/wilycode%2Fcache-file) | v0.1.0 | Simon Piter | Lightweight PSR-16 file cache with atomic writes and TTL support. |
| 2026-10-12 20:14:19 | [tamarackdb/tamarackdb-php](https://www.nuget.org/packages/tamarackdb%2Ftamarackdb-php) | v0.4.0 |  | PHP client for TamarackDB, an event store compliant with the DCB specification. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
