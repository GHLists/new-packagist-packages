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

## Latest list — 2026-11-18 22:22 UTC

New packages created between 2026-11-18 21:22 UTC and 2026-11-18 22:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T22-22-32-484614Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 21:23:11 | [prodbat/prodbat](https://www.nuget.org/packages/prodbat%2Fprodbat) | v0.0.1 |  | Monitoring for apps built with AI: server errors, logs, scheduled jobs and queu… |
| 2026-11-18 21:31:29 | [hryvinskyi/magento2-catalog-sorting-pack](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-pack) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sorting for Magento 2 in the search engine: out-of-stock products and p… |
| 2026-11-18 21:56:11 | [jeffersongoncalves/laravel-privacy](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-privacy) | 1.0.0 | Jefferson Gonçalves | Shared privacy engine for the LGPD, GDPR, CCPA, US state and Quebec Law 25 suit… |
| 2026-11-18 21:59:17 | [apimediaru/filament-documentation](https://www.nuget.org/packages/apimediaru%2Ffilament-documentation) | v0.1.0 |  | Markdown customer guides from installed packages in Filament. |
| 2026-11-18 22:01:30 | [disputeguard/disputeguard-php](https://www.nuget.org/packages/disputeguard%2Fdisputeguard-php) | v0.1.0 |  | PHP client for the DisputeGuard Connect API: push orders and activity evidence,… |
| 2026-11-18 22:01:44 | [uams-web/aether-enums](https://www.nuget.org/packages/uams-web%2Faether-enums) | v0.1.0 | UAMS Web Services; Josh Daugh… | The enums UAMS Statamic sites read (countries, currencies, languages, U.S. geog… |
| 2026-11-18 22:02:12 | [uams-web/aether-fieldtypes](https://www.nuget.org/packages/uams-web%2Faether-fieldtypes) | v0.1.0 | UAMS Web Services; Josh Daugh… | The shared fieldtype add-on for UAMS Statamic sites: the traits, Control Panel… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
