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

## Latest list — 2026-10-24 21:21 UTC

New packages created between 2026-10-24 20:21 UTC and 2026-10-24 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T21-21-49-147694Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 20:42:29 | [systonia/holidays](https://www.nuget.org/packages/systonia%2Fholidays) | v0.1.0 | Lento Leisenfeld | The public holidays of Germany, nationwide and per state. |
| 2026-10-24 20:43:25 | [sergiynezbritskiy/ukrposhta-api](https://www.nuget.org/packages/sergiynezbritskiy%2Fukrposhta-api) | 1.0.0 |  | Library for connecting to Ukrposhta API |
| 2026-10-24 20:58:19 | [sajjadh47/php2shell-php](https://www.nuget.org/packages/sajjadh47%2Fphp2shell-php) | v1.0.0 | sajjadh47 | Detect php2shell (CVE-2026-109618 / CVE-2026-109619) on remote PHP targets — be… |
| 2026-10-24 21:00:15 | [cybat/sdk](https://www.nuget.org/packages/cybat%2Fsdk) | v1.0.0 |  | Cybat SDK for PHP -- PSR-15 middleware that reports HTTP traffic directly to th… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
