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

## Latest list — 2026-10-19 15:21 UTC

New packages created between 2026-10-19 14:22 UTC and 2026-10-19 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T15-21-53-51444Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 14:23:38 | [phasync/ext-phasync](https://www.nuget.org/packages/phasync%2Fext-phasync) | 2.0.0 | Frode Børli | PHP extension that makes blocking I/O (PDO, mysqli, curl, streams, sleep) wait… |
| 2026-10-19 14:35:33 | [quietlink/bot-sdk](https://www.nuget.org/packages/quietlink%2Fbot-sdk) | v0.1.0 |  | QuietLink Bot API SDK for PHP with dual crypto modes |
| 2026-10-19 14:38:37 | [j87nl/laravel-cms](https://www.nuget.org/packages/j87nl%2Flaravel-cms) | v0.1.0 | Johan Montenij | Block-based CMS core for Laravel: pages, blocks and server-side public renderin… |
| 2026-10-19 14:38:41 | [j87nl/laravel-vue-cms](https://www.nuget.org/packages/j87nl%2Flaravel-vue-cms) | v0.1.0 | Johan Montenij | Vue and Inertia admin for j87nl/laravel-cms. |
| 2026-10-19 14:54:04 | [kerns/dummy](https://www.nuget.org/packages/kerns%2Fdummy) | v2.0.0 | David Kerns | A content generation toolkit for rapid web prototyping and QA |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
