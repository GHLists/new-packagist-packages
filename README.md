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

## Latest list — 2026-10-31 18:19 UTC

New packages created between 2026-10-31 17:20 UTC and 2026-10-31 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T18-19-54-167222Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 17:23:23 | [awcodes/thermal](https://www.nuget.org/packages/awcodes%2Fthermal) | v1.0.0 | Adam Weston | Heatmap visualizations for Filament: calendar activity grids and custom tile la… |
| 2026-10-31 17:28:54 | [nestapi/nestapi](https://www.nuget.org/packages/nestapi%2Fnestapi) | v1.0.0 | Hossein Saberi | Dynamic PHP client for the NestAPI web services |
| 2026-10-31 17:56:38 | [nowo-tech/health-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fhealth-kit-bundle) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Liveness and readiness endpoints with pluggable probes (Doctrine, Redis, Messen… |
| 2026-10-31 18:16:10 | [knackline/laravel-olm](https://www.nuget.org/packages/knackline%2Flaravel-olm) | 1.0.0 | Rajkumar Samra | Laravel package for on-device / local language models (MLX, Ollama, LM Studio,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
