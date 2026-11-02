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

## Latest list — 2026-11-02 05:21 UTC

New packages created between 2026-11-02 04:20 UTC and 2026-11-02 05:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T05-21-24-697687Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 04:24:03 | [subarist/waterhole-user-cover](https://www.nuget.org/packages/subarist%2Fwaterhole-user-cover) | v1.0.0 |  | User cover images for Waterhole |
| 2026-11-02 04:34:42 | [atannex/foundation](https://www.nuget.org/packages/atannex%2Ffoundation) | v1.0.0 | Atanga Leke Collins | Headless foundation for Atannex Laravel packages: package descriptors, dependen… |
| 2026-11-02 04:51:58 | [eric-sa/zca-php](https://www.nuget.org/packages/eric-sa%2Fzca-php) | v2.0.0 |  | Unofficial Zalo API for PHP (port of zca-js) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
