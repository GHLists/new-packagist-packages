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

## Latest list — 2026-10-10 20:20 UTC

New packages created between 2026-10-10 19:20 UTC and 2026-10-10 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T20-20-25-621191Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 19:23:06 | [mrfabulous/laravel-shibboleth](https://www.nuget.org/packages/mrfabulous%2Flaravel-shibboleth) | 1.0.2 | Christopher Maio; Michael Sch… | Enable basic Shibboleth support for Laravel. Forked from razorbacks/laravel-shi… |
| 2026-10-10 19:36:33 | [tmonier/sylius-command-palette-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-command-palette-plugin) | v1.0.0 | Thibaut Monier | Command palette (Ctrl+K / Cmd+K global search) for the Sylius 2 admin panel: or… |
| 2026-10-10 19:41:57 | [tamarackdb/tamarackdb-php](https://www.nuget.org/packages/tamarackdb%2Ftamarackdb-php) | v0.3.0 |  | PHP client for TamarackDB, an event store compliant with the DCB specification. |
| 2026-10-10 19:59:59 | [roadrunner/jobs](https://www.nuget.org/packages/roadrunner%2Fjobs) | 4.9.0 | Anton Titov; Pavel Buchnev; A… | PHP API for the RoadRunner Jobs (queues) plugin: manage pipelines, push tasks a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
