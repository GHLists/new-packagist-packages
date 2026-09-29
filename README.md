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

## Latest list — 2026-09-29 09:21 UTC

New packages created between 2026-09-29 08:25 UTC and 2026-09-29 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T09-21-17-247401Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 08:36:09 | [ganadev/laravel-shield](https://www.nuget.org/packages/ganadev%2Flaravel-shield) | v1.0.0 | Ganadev | Laravel adapter for Ganadev Shield - adaptive application firewall. |
| 2026-09-29 08:38:38 | [elgentos/module-gallery-mp4-solver](https://www.nuget.org/packages/elgentos%2Fmodule-gallery-mp4-solver) | v1.0.0 |  | MP4 support for the Magento media gallery: upload, sync, poster thumbnails and… |
| 2026-09-29 08:43:06 | [prestouniverse/presto-pay-sdk](https://www.nuget.org/packages/prestouniverse%2Fpresto-pay-sdk) | v0.1.0 | Presto Universe | Presto Pay merchant SDK for PHP |
| 2026-09-29 08:55:24 | [omniphp/framework](https://www.nuget.org/packages/omniphp%2Fframework) | v0.1.0 | owner888 | OmniPHP — The universal PHP framework. Lightweight, Workerman-based: HTTP route… |
| 2026-09-29 09:18:13 | [jeytekdev/explain-lint-codeception](https://www.nuget.org/packages/jeytekdev%2Fexplain-lint-codeception) | v1.1.0 | Jeytekdev | Codeception bridge for jeytekdev/explain-lint — analyzes and reports captured q… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
