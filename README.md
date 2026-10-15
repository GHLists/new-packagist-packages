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

## Latest list — 2026-10-15 23:20 UTC

New packages created between 2026-10-15 22:20 UTC and 2026-10-15 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T23-20-51-81846Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 22:31:02 | [wilycode/template](https://www.nuget.org/packages/wilycode%2Ftemplate) | v0.1.0 | Simon Piter | Compiled PHP template engine with layouts, sections, components and extensions. |
| 2026-10-15 22:52:28 | [abolaradev/authora](https://www.nuget.org/packages/abolaradev%2Fauthora) | v1.0.0 | abolaradev | A reusable authentication package for Laravel, designed to provide a flexible a… |
| 2026-10-15 23:02:42 | [wilycode/template-string](https://www.nuget.org/packages/wilycode%2Ftemplate-string) | v0.1.0 | Simon Piter | String and formatting filters for the WilyCode Template engine. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
