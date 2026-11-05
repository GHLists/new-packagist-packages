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

## Latest list — 2026-11-05 21:18 UTC

New packages created between 2026-11-05 20:19 UTC and 2026-11-05 21:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T21-18-55-329407Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 20:30:46 | [mj-zana/outbox](https://www.nuget.org/packages/mj-zana%2Foutbox) | v2.14.0 |  | A transactional outbox and inbox for Zana: events stored with the change they d… |
| 2026-11-05 20:59:09 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.17.0 |  | The skeleton application for the Laravel framework. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
