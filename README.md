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

## Latest list — 2026-10-28 10:19 UTC

New packages created between 2026-10-28 09:20 UTC and 2026-10-28 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T10-19-50-594897Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 09:31:03 | [packstub/filament-gantt](https://www.nuget.org/packages/packstub%2Ffilament-gantt) | v1.0.0-beta.1 | Ion Caliman; Packstub | A fast Gantt chart and resource timeline for Filament: any Eloquent query with… |
| 2026-10-28 09:32:40 | [rft/laravel-docker](https://www.nuget.org/packages/rft%2Flaravel-docker) | v1.0.0 |  | Zero-file Docker runtime (PHP 8.5 + Apache) and Composer commands for Laravel a… |
| 2026-10-28 09:33:53 | [zxf/res](https://www.nuget.org/packages/zxf%2Fres) | v0.0.1 |  | 共享静态资源（字体、css、js、图片）包 |
| 2026-10-28 09:35:32 | [uxf/composer-proxy](https://www.nuget.org/packages/uxf%2Fcomposer-proxy) | 1.0.0 | UXF | Composer plugin redirecting package dist downloads through the internal compose… |
| 2026-10-28 09:43:42 | [bitlane/magento](https://www.nuget.org/packages/bitlane%2Fmagento) | 0.1.0 |  | Bitlane search for Magento Open Source, Adobe Commerce and Mage-OS 2.4.7 to 2.4… |
| 2026-10-28 09:43:54 | [bitlane/prestashop](https://www.nuget.org/packages/bitlane%2Fprestashop) | v0.3.0 | Bitlane | Bitlane search for PrestaShop 8 and 9: your catalogue in sync with Bitlane in e… |
| 2026-10-28 09:44:04 | [bitlane/wordpress](https://www.nuget.org/packages/bitlane%2Fwordpress) | v0.5.1 | Bitlane | Bitlane search for WordPress and WooCommerce: your catalogue, pages and posts i… |
| 2026-10-28 10:09:54 | [darvis/printserver](https://www.nuget.org/packages/darvis%2Fprintserver) | v1.0.0 | Arvid de Jong | Queue print jobs in Laravel and let a print box on location fetch them over HTT… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
