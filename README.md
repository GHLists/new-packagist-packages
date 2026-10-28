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

## Latest list — 2026-10-28 11:19 UTC

New packages created between 2026-10-28 10:19 UTC and 2026-10-28 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T11-19-25-906774Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 10:40:34 | [webmasterskaya/dellin-php-sdk](https://www.nuget.org/packages/webmasterskaya%2Fdellin-php-sdk) | v1.0.0 |  | PHP SDK для работы с API сервиса Деловые Линии (dellin.ru) |
| 2026-10-28 10:42:07 | [tacraft-sociality/flarum-html-errors](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-html-errors) | 1.0.0 |  | Redirect error responses to custom pages |
| 2026-10-28 11:02:45 | [yireo/magento2-store-view-commands](https://www.nuget.org/packages/yireo%2Fmagento2-store-view-commands) | 1.0.0 |  | N/A |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
