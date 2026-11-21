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

## Latest list — 2026-11-21 01:19 UTC

New packages created between 2026-11-21 00:20 UTC and 2026-11-21 01:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T01-19-53-908365Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 00:34:04 | [pushery/tax-audit-export-for-laravel](https://www.nuget.org/packages/pushery%2Ftax-audit-export-for-laravel) | v0.1.0 | Pushery | Writes the index.xml, DTD and CSV files of a tax audit data export (GoBD, GDPdU… |
| 2026-11-21 00:35:00 | [pushery/sovereign-ai-for-laravel](https://www.nuget.org/packages/pushery%2Fsovereign-ai-for-laravel) | v0.1.0 | Pushery | IONOS AI Model Hub and OVHcloud AI Endpoints as providers for the Laravel AI SD… |
| 2026-11-21 00:48:10 | [datacircle/laravel-ai-tools](https://www.nuget.org/packages/datacircle%2Flaravel-ai-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. Four Laravel AI SDK tools call Datacircle's public API.… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
