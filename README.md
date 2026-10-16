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

## Latest list — 2026-10-16 09:19 UTC

New packages created between 2026-10-16 08:21 UTC and 2026-10-16 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T09-19-57-806117Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 08:26:23 | [dwivedianuj9118/mediaflow-laravel](https://www.nuget.org/packages/dwivedianuj9118%2Fmediaflow-laravel) | v1.0.2 | Anuj Dwivedi | Universal media management infrastructure and UI for Laravel applications |
| 2026-10-16 08:46:45 | [hostfog/toolkit](https://www.nuget.org/packages/hostfog%2Ftoolkit) | v0.1.0 | HostFog | Zero-dependency toolkit for web developers and server admins: domain normalisat… |
| 2026-10-16 09:00:06 | [qiangvei/magento2-theme-amazon](https://www.nuget.org/packages/qiangvei%2Fmagento2-theme-amazon) | 1.0.2 |  | Amazon style theme for Magento 2.4 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
