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

## Latest list — 2026-10-12 01:19 UTC

New packages created between 2026-10-12 00:21 UTC and 2026-10-12 01:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T01-19-43-054311Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 00:35:34 | [scottoffen/wp-github-updater](https://www.nuget.org/packages/scottoffen%2Fwp-github-updater) | v0.1.0 | Scott Offen | Update WordPress plugins and themes from GitHub releases using both public and… |
| 2026-10-12 00:52:06 | [linkfast/exengine-cli](https://www.nuget.org/packages/linkfast%2Fexengine-cli) | 1.0.0-a1 | Giancarlo A. Chiappe | exen: command line tool for the ExEngine microframework (new projects, dev serv… |
| 2026-10-12 01:11:49 | [linkfast/exengine-roadrunner](https://www.nuget.org/packages/linkfast%2Fexengine-roadrunner) | 1.0.0-a1 | Giancarlo A. Chiappe | RoadRunner application server support for the ExEngine microframework: long-run… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
