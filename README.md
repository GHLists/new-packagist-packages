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

## Latest list — 2026-10-29 06:19 UTC

New packages created between 2026-10-29 05:20 UTC and 2026-10-29 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T06-19-25-808717Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 05:27:16 | [zhandos717/moonshine-docx-editor](https://www.nuget.org/packages/zhandos717%2Fmoonshine-docx-editor) | v1.3.1 | Zhandos | WYSIWYG DOCX editor for MoonShine admin panel, built on docen |
| 2026-10-29 05:40:02 | [vaartix/vaartix-php](https://www.nuget.org/packages/vaartix%2Fvaartix-php) | v0.1.0 | NAP Designs | Official PHP SDK for the Vaartix email API |
| 2026-10-29 05:46:56 | [gosuccess/endoflife-api](https://www.nuget.org/packages/gosuccess%2Fendoflife-api) | 0.1.0 | GoSuccess GmbH | A modern, strongly-typed, dependency-free PHP client for the endoflife.date API… |
| 2026-10-29 05:49:31 | [aisdk/typesafe](https://www.nuget.org/packages/aisdk%2Ftypesafe) | v0.10.0 |  | Native TypeSafe Jev decisions for the framework-agnostic PHP AI SDK. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
