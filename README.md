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

## Latest list — 2026-11-14 02:19 UTC

New packages created between 2026-11-14 01:20 UTC and 2026-11-14 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T02-19-18-349395Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 01:33:12 | [leazycms/web](https://www.nuget.org/packages/leazycms%2Fweb) | v1.0.1 | Nurul Hudin | Build Easy Cms Laravel |
| 2026-11-14 01:38:17 | [particle-academy/prism-graph](https://www.nuget.org/packages/particle-academy%2Fprism-graph) | v0.1.0 |  | Configurable knowledge graphs with embeddings for Prism: verbatim chunks, conte… |
| 2026-11-14 02:05:40 | [elcreator/hybridauth](https://www.nuget.org/packages/elcreator%2Fhybridauth) | 3.13.1 | Miled | PHP Social Authentication Library |
| 2026-11-14 02:07:18 | [common-doc/aggregate-renderer](https://www.nuget.org/packages/common-doc%2Faggregate-renderer) | 1.0.0-alpha.1 | Joey Smith | Renders every onboarded documentation project and version into one aggregate si… |
| 2026-11-14 02:07:23 | [common-doc/commondoc](https://www.nuget.org/packages/common-doc%2Fcommondoc) | 1.0.0-alpha.1 | Joey Smith | Multi-repository Markdown documentation site builder for PHP. |
| 2026-11-14 02:08:48 | [manuxi/sulu-dashboard-bundle](https://www.nuget.org/packages/manuxi%2Fsulu-dashboard-bundle) | v1.0.0 | Manuxi | Dashboard for the Sulu 3 admin: start page with tiles, plus a small interface f… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
