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

## Latest list — 2026-09-30 09:20 UTC

New packages created between 2026-09-30 08:21 UTC and 2026-09-30 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T09-20-04-514096Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 08:24:07 | [mage2kishan/module-smart-badge](https://www.nuget.org/packages/mage2kishan%2Fmodule-smart-badge) | 1.0.11 |  | Smart Product Badge & Label System - Automatically displays beautiful badges on… |
| 2026-09-30 08:32:15 | [baracod/larastarterkit-core](https://www.nuget.org/packages/baracod%2Flarastarterkit-core) | 1.0.0-rc.1 |  | Shared Laravel infrastructure with Auth and Admin modules |
| 2026-09-30 08:36:56 | [baracod/larastarterkit-generator](https://www.nuget.org/packages/baracod%2Flarastarterkit-generator) | 1.0.0-rc.1 |  | Developer tooling for Larastarterkit |
| 2026-09-30 08:52:23 | [tomvondracek/bolt-ai-image-alt](https://www.nuget.org/packages/tomvondracek%2Fbolt-ai-image-alt) | v1.0.0 | Tomas Vondracek | In-browser AI generation of image ALT texts for the Bolt CMS admin (Florence-2… |
| 2026-09-30 08:53:09 | [omniphp/omniphp](https://www.nuget.org/packages/omniphp%2Fomniphp) | v0.1.0 | owner888 | OmniPHP application skeleton — a ready-to-run Workerman project layout for the… |
| 2026-09-30 09:07:14 | [tastysoul/changelog-checker](https://www.nuget.org/packages/tastysoul%2Fchangelog-checker) | 1.0.0 |  | Composer plugin to check changelog files for breaking changes |
| 2026-09-30 09:08:31 | [emse-dev/doxswap](https://www.nuget.org/packages/emse-dev%2Fdoxswap) | 1.1.0 | Michael Deeming | Doxswap is a simple document conversion package for Laravel which uses LibreOff… |
| 2026-09-30 09:09:03 | [emse-dev/onym](https://www.nuget.org/packages/emse-dev%2Fonym) | 1.1.0 | Michael Deeming | Onym is a lightweight Laravel package designed to generate unique, structured,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
