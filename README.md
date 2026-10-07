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

## Latest list — 2026-10-07 10:21 UTC

New packages created between 2026-10-07 09:21 UTC and 2026-10-07 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T10-21-06-736765Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 09:53:24 | [vadage/presigned-uploader-bundle](https://www.nuget.org/packages/vadage%2Fpresigned-uploader-bundle) | v0.1.0 | vadage | Presigned direct-to-storage uploads for Symfony, with entity mapping, validatio… |
| 2026-10-07 09:56:37 | [anis-ly/partners](https://www.nuget.org/packages/anis-ly%2Fpartners) | v1.1.0 | Aniscom for Technical Service… | The PHP SDK for the Anis Partner API — signed requests, verified responses, typ… |
| 2026-10-07 09:58:18 | [iperstudio/site-sync](https://www.nuget.org/packages/iperstudio%2Fsite-sync) | v0.2.0 |  | Interactive rsync CLI for synchronizing project content and accounts over SSH. |
| 2026-10-07 10:01:30 | [offline-agency/spid-laravel-trentino](https://www.nuget.org/packages/offline-agency%2Fspid-laravel-trentino) | v2.0.0 | Offline Agency | SPID authentication for Laravel through AAC Trentino (OpenID Connect with PKCE) |
| 2026-10-07 10:01:52 | [ferrox/ferrox-php-config](https://www.nuget.org/packages/ferrox%2Fferrox-php-config) | v1.1.0 |  | Strongly-typed environment loader for Ferrox PHP |
| 2026-10-07 10:01:52 | [ferrox/ferrox-php-core](https://www.nuget.org/packages/ferrox%2Fferrox-php-core) | v1.1.0 |  | Core DI and Bootstrap for Ferrox PHP |
| 2026-10-07 10:01:52 | [ferrox/ferrox-php-cqrs](https://www.nuget.org/packages/ferrox%2Fferrox-php-cqrs) | v1.1.0 |  | CQRS CommandBus & QueryBus for Ferrox PHP |
| 2026-10-07 10:01:52 | [ferrox/ferrox-php-crud-gen](https://www.nuget.org/packages/ferrox%2Fferrox-php-crud-gen) | v1.1.0 |  | Metaprogramming and Attribute-based CRUD generation for Ferrox PHP |
| 2026-10-07 10:01:52 | [ferrox/ferrox-php-data](https://www.nuget.org/packages/ferrox%2Fferrox-php-data) | v1.1.0 |  | Singleflight and Persistence for Ferrox PHP |
| 2026-10-07 10:01:52 | [ferrox/ferrox-php-database-core](https://www.nuget.org/packages/ferrox%2Fferrox-php-database-core) | v1.1.0 |  | Abstract Repository trait and generic persistence contracts for Ferrox PHP |
| 2026-10-07 10:01:52 | [ferrox/ferrox-php-events](https://www.nuget.org/packages/ferrox%2Fferrox-php-events) | v1.1.0 |  | Strongly-typed DomainEvent dispatcher and Pub/Sub bus for Ferrox PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
