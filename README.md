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

## Latest list — 2026-11-12 10:21 UTC

New packages created between 2026-11-12 09:21 UTC and 2026-11-12 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T10-21-42-642365Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 09:27:22 | [traffman/sdk-php](https://www.nuget.org/packages/traffman%2Fsdk-php) | v1.0.0 | Traffman; modeewine | Transport-agnostic PHP SDK for the Traffman API (content exchange network). |
| 2026-11-12 09:40:58 | [solutionforest/laravel-recommender](https://www.nuget.org/packages/solutionforest%2Flaravel-recommender) | v0.0.5 | Solution Forest Limited | Self-hosted, low-overhead recommendation feeds for Laravel (co-interaction simi… |
| 2026-11-12 09:47:48 | [vcat/vc-safety-check](https://www.nuget.org/packages/vcat%2Fvc-safety-check) | 1.0.0 | Joram Wittke; Nico Hoffmann;… | Checks all installed extensions, core packages and their dependencies for known… |
| 2026-11-12 09:53:54 | [welman91/filament-api-service](https://www.nuget.org/packages/welman91%2Ffilament-api-service) | v1.0.1 | Welman | A simple api service for supporting filamentphp |
| 2026-11-12 10:20:26 | [solvebeam/oauth2-twinfield](https://www.nuget.org/packages/solvebeam%2Foauth2-twinfield) | v0.1.0 | SolveBeam; Remco Tolsma | Twinfield OAuth 2.0 provider for the PHP League's OAuth 2.0 Client |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
