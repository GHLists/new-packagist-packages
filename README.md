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

## Latest list — 2026-10-15 17:21 UTC

New packages created between 2026-10-15 16:20 UTC and 2026-10-15 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T17-21-30-689086Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 16:51:51 | [juksgraphic/bladecomponents](https://www.nuget.org/packages/juksgraphic%2Fbladecomponents) | v1.0.0 | Kingsley | Composants Blade (Tailwind, Alpine, Penguin UI) pour Laravel et BladeOne. |
| 2026-10-15 17:04:56 | [citomni/demo-provider](https://www.nuget.org/packages/citomni%2Fdemo-provider) | v1.0.0.1 | Lars Grove Mortensen | Reference provider package for the CitOmni PHP framework: site notices with a R… |
| 2026-10-15 17:10:33 | [tuchsoft/issue-reporter](https://www.nuget.org/packages/tuchsoft%2Fissue-reporter) | v1.0.1 | Mattia Bonzi | A reporting library for static code analysis issues. It reads, aggregates, and… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
