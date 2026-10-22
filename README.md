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

## Latest list — 2026-10-22 21:21 UTC

New packages created between 2026-10-22 20:20 UTC and 2026-10-22 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T21-21-22-583824Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 20:39:59 | [vincentauger/orcid-php-sdk](https://www.nuget.org/packages/vincentauger%2Forcid-php-sdk) | v0.1.0 | Vincent Auger | A modern, framework-agnostic PHP SDK for the ORCID API |
| 2026-10-22 20:54:19 | [jmoati/icloudpd](https://www.nuget.org/packages/jmoati%2Ficloudpd) | 1.32.3 | The iCloud Photo Downloader A… | Pure PHP port of icloud_photos_downloader (icloudpd): download photos and video… |
| 2026-10-22 20:56:37 | [teknoo/east-ux](https://www.nuget.org/packages/teknoo%2Feast-ux) | 0.1.0 | Richard Déloge | Symfony bundle, following the #East programming philosophy, build on Teknoo/Eas… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
