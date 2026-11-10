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

## Latest list — 2026-11-10 00:20 UTC

New packages created between 2026-11-09 23:21 UTC and 2026-11-10 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T00-20-00-160132Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 23:33:51 | [companyenrich/sdk](https://www.nuget.org/packages/companyenrich%2Fsdk) | v1.0.0 | CompanyEnrich | Official PHP SDK for the CompanyEnrich API: company and people enrichment, sear… |
| 2026-11-09 23:35:57 | [devletes/filament-chrono-picker](https://www.nuget.org/packages/devletes%2Ffilament-chrono-picker) | v0.1.1 | Devletes | The ultimate date and time picker for Filament: time, date, month, year and ran… |
| 2026-11-10 00:01:56 | [almztech/sdk](https://www.nuget.org/packages/almztech%2Fsdk) | v0.2.0-beta.1 | ALMZTECH SOFTWARES LTDA | SDK oficial PHP para a API da Almztech (emissão, consulta, reconsulta e cancela… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
