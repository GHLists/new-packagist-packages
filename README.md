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

## Latest list — 2026-10-25 10:20 UTC

New packages created between 2026-10-25 09:21 UTC and 2026-10-25 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T10-20-53-581993Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 09:28:03 | [blackcube/fileprovider](https://www.nuget.org/packages/blackcube%2Ffileprovider) | 1.0.0 | Philippe Gaultier | File provider with prefix routing and image processing |
| 2026-10-25 09:34:12 | [blackcube/resumable](https://www.nuget.org/packages/blackcube%2Fresumable) | 1.0.0 | Philippe Gaultier | Resumable.js server side for Yii: chunked upload, preview and delete actions on… |
| 2026-10-25 09:37:24 | [anun333/oe-module-ccbhc-report](https://www.nuget.org/packages/anun333%2Foe-module-ccbhc-report) | v0.1.0 |  | The CCBHC clinic-collected quality measures for OpenEMR: Time to Services, soci… |
| 2026-10-25 09:40:08 | [jamie-humm/kirby-microlighter](https://www.nuget.org/packages/jamie-humm%2Fkirby-microlighter) | v1.0@beta | Jamie Hunter | Kirby Microlighter: a syntax-highlighted code block for Kirby, powered by Micro… |
| 2026-10-25 09:48:05 | [gin/env-merger](https://www.nuget.org/packages/gin%2Fenv-merger) | v1.0.0 | Gin | Smart, format-preserving .env merger with interactive conflict resolution and L… |
| 2026-10-25 09:53:37 | [blackcube/bridge-form-model](https://www.nuget.org/packages/blackcube%2Fbridge-form-model) | 1.0.0 | Philippe Gaultier | Bridged FormModel for Yii framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
