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

## Latest list — 2026-11-24 21:20 UTC

New packages created between 2026-11-24 20:19 UTC and 2026-11-24 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T21-20-06-363026Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 20:24:20 | [eshimischi/vendor-cleanup](https://www.nuget.org/packages/eshimischi%2Fvendor-cleanup) | v2.1.3 | eshimischi | Global CLI tool & Composer plugin to strip tests, docs, and dev files from vend… |
| 2026-11-24 20:36:24 | [mrcaspan/flarum2-events-calendar](https://www.nuget.org/packages/mrcaspan%2Fflarum2-events-calendar) | v1.1.0 | MrCaspan | Events calendar for Flarum 2.0: discussions in an events tag get a date and app… |
| 2026-11-24 20:45:03 | [jimbojsb/gatekeeper](https://www.nuget.org/packages/jimbojsb%2Fgatekeeper) | v0.1.1 |  | Code-defined roles and permissions for Laravel, stored as a JSON column on the… |
| 2026-11-24 20:48:14 | [hamzaaqq/openqa-toolkit](https://www.nuget.org/packages/hamzaaqq%2Fopenqa-toolkit) | v0.1.0 |  | Small CLI for repeatable web quality checks |
| 2026-11-24 21:11:18 | [zeeshan-elahi/laravel-ai-guard](https://www.nuget.org/packages/zeeshan-elahi%2Flaravel-ai-guard) | v0.1.0 | Zeeshan Elahi | Prompt-injection and tool-safety guard for the Laravel AI SDK: tool policies, u… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
