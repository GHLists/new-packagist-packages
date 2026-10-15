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

## Latest list — 2026-10-15 03:22 UTC

New packages created between 2026-10-15 02:19 UTC and 2026-10-15 03:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T03-22-55-577715Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 02:30:51 | [runapi-ai/heygen-video](https://www.nuget.org/packages/runapi-ai%2Fheygen-video) | v0.1.0 | RunAPI | RunAPI HeyGen Video Composer package for PHP applications |
| 2026-10-15 02:30:53 | [runapi-ai/qwen-2.1](https://www.nuget.org/packages/runapi-ai%2Fqwen-2.1) | v0.1.0 | RunAPI | RunAPI Qwen 2.1 Composer package for PHP applications |
| 2026-10-15 02:30:55 | [runapi-ai/vidu](https://www.nuget.org/packages/runapi-ai%2Fvidu) | v0.1.0 | RunAPI | RunAPI Vidu Composer package for PHP applications |
| 2026-10-15 02:39:46 | [magezon/module-ui-builder](https://www.nuget.org/packages/magezon%2Fmodule-ui-builder) | 1.0.14 |  | Magezon UI Builder - shared admin form/UI element framework for Magezon extensi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
