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

## Latest list — 2026-11-13 13:20 UTC

New packages created between 2026-11-13 12:20 UTC and 2026-11-13 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T13-20-53-245399Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 12:31:42 | [janalis/php-profiler](https://www.nuget.org/packages/janalis%2Fphp-profiler) | v0.1.0-alpha.1 |  | Local PHP profiler implemented in Rust |
| 2026-11-13 12:43:16 | [iq2i/herse-bundle](https://www.nuget.org/packages/iq2i%2Fherse-bundle) | 0.1.0 |  | Account security building blocks for Symfony and Sylius: password policy, login… |
| 2026-11-13 13:10:10 | [dwenzel/be-environment-indicator](https://www.nuget.org/packages/dwenzel%2Fbe-environment-indicator) | 0.1.0 | Dirk Wenzel | Shows the current environment (application context) and the admin role in the T… |
| 2026-11-13 13:10:11 | [rsgrinko/ai-sdk](https://www.nuget.org/packages/rsgrinko%2Fai-sdk) | v0.1.0 | rsgrinko | Лёгкий PHP SDK для агентов с вызовом инструментов поверх OpenAI-совместимых API… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
