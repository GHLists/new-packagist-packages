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

## Latest list — 2026-10-08 14:22 UTC

New packages created between 2026-10-08 13:21 UTC and 2026-10-08 14:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T14-22-19-495561Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 13:24:29 | [appolodev/form-builder-bundle](https://www.nuget.org/packages/appolodev%2Fform-builder-bundle) | v1.0.0 | Fredxd | Moteur de formulaires personnalisés pour Symfony : structure, rendu, réponses e… |
| 2026-10-08 13:26:05 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.2.4 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-08 13:26:29 | [novay/minios](https://www.nuget.org/packages/novay%2Fminios) | 0.0.2 | Noviyanto Rahmadi | MiniOS Desktop Environment for Laravel |
| 2026-10-08 13:44:37 | [obj63mc/silverstripe-forager-elasticsearch](https://www.nuget.org/packages/obj63mc%2Fsilverstripe-forager-elasticsearch) | 0.0.1 | Joe Madden | Elasticsearch provider for silverstripe/silverstripe-forager, using the officia… |
| 2026-10-08 13:55:38 | [wexample/symfony-bpmn](https://www.nuget.org/packages/wexample%2Fsymfony-bpmn) | 1.0.1 |  |  |
| 2026-10-08 13:56:20 | [wexample/symfony-bpmn-ds](https://www.nuget.org/packages/wexample%2Fsymfony-bpmn-ds) | 1.0.1 |  |  |
| 2026-10-08 13:57:09 | [wexample/symfony-bpmn-demo](https://www.nuget.org/packages/wexample%2Fsymfony-bpmn-demo) | 1.0.1 |  |  |
| 2026-10-08 13:57:57 | [wexample/php-bpmn](https://www.nuget.org/packages/wexample%2Fphp-bpmn) | 1.0.1 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
