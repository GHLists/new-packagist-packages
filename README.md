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

## Latest list — 2026-10-03 07:21 UTC

New packages created between 2026-10-03 06:19 UTC and 2026-10-03 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T07-21-46-467815Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 06:35:53 | [itxshakil/laravel-form-shield](https://www.nuget.org/packages/itxshakil%2Flaravel-form-shield) | v1.0.1 | Shakil Alam | CAPTCHA-free spam scoring for Laravel forms: quarantine instead of reject, keep… |
| 2026-10-03 06:53:28 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.6 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |
| 2026-10-03 07:15:43 | [php-bug-catcher/perf-collector](https://www.nuget.org/packages/php-bug-catcher%2Fperf-collector) | 2.0.0-RC1 |  | Per-request performance collector for Bug Catcher: an auto_prepend_file hook an… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
