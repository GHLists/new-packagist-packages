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

## Latest list — 2026-11-04 05:19 UTC

New packages created between 2026-11-04 04:19 UTC and 2026-11-04 05:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T05-19-03-741904Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 04:28:54 | [aoding9/qiniu-laravel-storage](https://www.nuget.org/packages/aoding9%2Fqiniu-laravel-storage) | 9.1.0 | zgldh; abcsun | Qiniu Resource (Cloud) Storage SDK for Laravel (fork of zgldh/qiniu-laravel-sto… |
| 2026-11-04 04:28:55 | [aoding9/laravel-admin](https://www.nuget.org/packages/aoding9%2Flaravel-admin) | 2.4.4 | aoding9; Shine; jqh | Dcat admin fork based on PrintNow/dcat-admin — Laravel 10-13 / PHP 8.1+ (incl.… |
| 2026-11-04 04:28:55 | [aoding9/laravel-feie-printer](https://www.nuget.org/packages/aoding9%2Flaravel-feie-printer) | 1.0.0 | Georgie | laravel feie printer |
| 2026-11-04 04:45:52 | [softmedialabs/laravel-route-annotation](https://www.nuget.org/packages/softmedialabs%2Flaravel-route-annotation) | v1.0.0 | Achmad Miftahul Rizqi | Comprehensive PHP 8 Attribute-based Route Annotation library for Laravel |
| 2026-11-04 05:02:03 | [aoding9/qiniu-php-sdk](https://www.nuget.org/packages/aoding9%2Fqiniu-php-sdk) | 7.14.0 | Qiniu | Qiniu Resource (Cloud) Storage SDK for PHP (fork with PHP 8.4+ nullable fixes) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
