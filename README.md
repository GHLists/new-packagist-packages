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

## Latest list — 2026-11-14 07:21 UTC

New packages created between 2026-11-14 06:21 UTC and 2026-11-14 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T07-21-32-756889Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 06:45:51 | [breizhwave/wave-security-ip-restrict](https://www.nuget.org/packages/breizhwave%2Fwave-security-ip-restrict) | v1.0.0 | erwanpia | Restrict a whole Laravel application to an IP allow list (IPv4, IPv6, CIDR), ma… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
