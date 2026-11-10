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

## Latest list — 2026-11-10 04:21 UTC

New packages created between 2026-11-10 03:20 UTC and 2026-11-10 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T04-21-58-692171Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 03:34:02 | [hanshs474/freeimagetovideo](https://www.nuget.org/packages/hanshs474%2Ffreeimagetovideo) | v0.1.0 | Free Image to Video | Free image to video AI with no daily cap: start with no sign-up, keep going on… |
| 2026-11-10 03:40:49 | [pembayaranku/laravel](https://www.nuget.org/packages/pembayaranku%2Flaravel) | 1.0.2 | PT MEDIA SIRINGO ABADI | Official Laravel integration for PembayaranKU Merchant API V1 and Hosted Checko… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
