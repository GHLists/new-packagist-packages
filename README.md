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

## Latest list — 2026-11-26 00:19 UTC

New packages created between 2026-11-25 23:19 UTC and 2026-11-26 00:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T00-19-30-260619Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 23:37:58 | [obelaw/ium](https://www.nuget.org/packages/obelaw%2Fium) | v1.0.0 | Karim Mohamed; Obelaw Team | Obelawium (IUM) Core — Modular ERP Domain Standard, Registry, Contracts, Buildi… |
| 2026-11-25 23:40:26 | [obelaw/ium-accounting](https://www.nuget.org/packages/obelaw%2Fium-accounting) | v1.0.0 | Obelaw Team | Enterprise General Ledger & Financial Management (FMS) Domain Module for Obelaw… |
| 2026-11-25 23:42:29 | [obelaw/runner-laravel](https://www.nuget.org/packages/obelaw%2Frunner-laravel) | v1.0.0 | Obelaw Team | A Laravel package that provides a runner system for executing tasks with depend… |
| 2026-11-25 23:45:04 | [chr-z/valida-nfse](https://www.nuget.org/packages/chr-z%2Fvalida-nfse) | v1.0.0 | Christian Eliel | Validador offline de XML de NFS-e (DPS/NFSe padrao nacional e ABRASF) para PHP.… |
| 2026-11-26 00:02:12 | [dmstr/neuron-ai-bundle](https://www.nuget.org/packages/dmstr%2Fneuron-ai-bundle) | 0.1.0 | diemeisterei GmbH | Symfony bundle integrating the Neuron AI framework: provider factory (Anthropic… |
| 2026-11-26 00:04:08 | [obelaw/trail](https://www.nuget.org/packages/obelaw%2Ftrail) | v1.0.0 |  | Minimal, activity trail for Eloquent models. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
