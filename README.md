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

## Latest list — 2026-11-09 15:19 UTC

New packages created between 2026-11-09 14:18 UTC and 2026-11-09 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T15-19-47-825562Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 14:19:27 | [intragile/laravel-mnb-exchange-rates](https://www.nuget.org/packages/intragile%2Flaravel-mnb-exchange-rates) | v1.0.0 | IntrAgile Kft. | MNB (Magyar Nemzeti Bank) official exchange rates without ext-soap: today's and… |
| 2026-11-09 14:35:42 | [medienreaktor/neos-mcp](https://www.nuget.org/packages/medienreaktor%2Fneos-mcp) | 0.1.0 |  | Serves the operations of neos/openapi APIs, preconfigured for the Neos API, as… |
| 2026-11-09 14:35:44 | [medienreaktor/neos-oauth](https://www.nuget.org/packages/medienreaktor%2Fneos-oauth) | 0.1.0 |  | OAuth 2 authorization server and bearer token authentication for Neos, based on… |
| 2026-11-09 14:35:46 | [medienreaktor/neos-openapi-mcp](https://www.nuget.org/packages/medienreaktor%2Fneos-openapi-mcp) | 0.1.0 |  | Expose the operations of a neos/openapi as Model Context Protocol tools, using… |
| 2026-11-09 14:35:49 | [medienreaktor/neos-openapi-bundle](https://www.nuget.org/packages/medienreaktor%2Fneos-openapi-bundle) | 0.1.0 |  | neos/jsonschema, neos/schematic, neos/openapi and neos/openapi-flowadapter in o… |
| 2026-11-09 14:37:34 | [lakedrops/ai-catalog](https://www.nuget.org/packages/lakedrops%2Fai-catalog) | 1.0.0 | Jürgen Haas; Daniel Speicher;… | Composer Plugin to publish an ARD (Agentic Resource Discovery) capability manif… |
| 2026-11-09 14:47:54 | [norialabs/ledger](https://www.nuget.org/packages/norialabs%2Fledger) | v0.1.0 | Joseph Gitonga | Exact, immutable, multi-entity accounting for Laravel applications and accounti… |
| 2026-11-09 14:56:47 | [itk-dev/itkdev_advancedqueue_addons](https://www.nuget.org/packages/itk-dev%2Fitkdev_advancedqueue_addons) | 1.0.0 | Mikkel Ricky | Add-ons for Drupal's Advanced Queue module |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
