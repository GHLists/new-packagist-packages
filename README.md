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

## Latest list — 2026-10-19 21:21 UTC

New packages created between 2026-10-19 20:22 UTC and 2026-10-19 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T21-21-59-521497Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 20:47:02 | [talovicnedim/berthq-client](https://www.nuget.org/packages/talovicnedim%2Fberthq-client) | v0.1.1 | Nedim Talovic | PHP client and Laravel queue driver for Berthq, a single-binary message broker |
| 2026-10-19 20:51:54 | [etfusion/vari-php-sdk](https://www.nuget.org/packages/etfusion%2Fvari-php-sdk) | v1.0.0 |  | PHP SDK for the V-ARI Stable API (mutual TLS): identity, certificate rotation,… |
| 2026-10-19 21:10:00 | [chakchakman/flarum-interactive-maps](https://www.nuget.org/packages/chakchakman%2Fflarum-interactive-maps) | v0.1.0-beta.1 | Chakchakman | Interactive tabletop maps and controlled character tokens for Flarum |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
