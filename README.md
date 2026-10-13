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

## Latest list — 2026-10-13 07:20 UTC

New packages created between 2026-10-13 06:21 UTC and 2026-10-13 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T07-20-34-812422Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 06:38:27 | [magna-cms/forms](https://www.nuget.org/packages/magna-cms%2Fforms) | v0.1.0 |  | Forms for Magna: build, place, collect. |
| 2026-10-13 06:57:47 | [zeimoto/image](https://www.nuget.org/packages/zeimoto%2Fimage) | v0.1.0 | zeimoto | Responsive image rendering with art direction and crop helpers. |
| 2026-10-13 06:59:54 | [zeimoto/writer](https://www.nuget.org/packages/zeimoto%2Fwriter) | v0.1.0 | zeimoto | An inline-only extension of the Kirby Writer field. |
| 2026-10-13 07:04:57 | [zeimoto/blocks](https://www.nuget.org/packages/zeimoto%2Fblocks) | v0.1.0 | zeimoto | Custom Kirby blocks with Panel editors and public rendering snippets. |
| 2026-10-13 07:17:48 | [zeimoto/branding](https://www.nuget.org/packages/zeimoto%2Fbranding) | v0.1.0 | zeimoto | Site logo marks, color palettes, and a palette-backed Panel field. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
