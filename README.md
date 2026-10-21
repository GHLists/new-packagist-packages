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

## Latest list — 2026-10-21 11:20 UTC

New packages created between 2026-10-21 10:20 UTC and 2026-10-21 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T11-20-37-271615Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 10:46:19 | [hampel/xenforo-phpstan](https://www.nuget.org/packages/hampel%2Fxenforo-phpstan) | 0.1.0 | Simon Hampel | PHPStan for XenForo add-ons - the configuration an add-on needs to be analysed… |
| 2026-10-21 10:52:43 | [astrophp/verse](https://www.nuget.org/packages/astrophp%2Fverse) | v0.1.0 | Melih Ucar | AstroPHP Verse: a static site generator. Write in Markdown, design with Blade,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
