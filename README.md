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

## Latest list — 2026-10-04 16:21 UTC

New packages created between 2026-10-04 15:18 UTC and 2026-10-04 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T16-21-30-082455Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 15:35:32 | [voku/agent-edit](https://www.nuget.org/packages/voku%2Fagent-edit) | 0.1.0 | Lars Moelleken | Deterministic, evidence-backed source mutation for coding agents: validate, app… |
| 2026-10-04 15:41:46 | [danielm/laravel-simple-altcha](https://www.nuget.org/packages/danielm%2Flaravel-simple-altcha) | v0.1.0 |  | ALTCHA (proof-of-work captcha) for Laravel: challenge endpoint, validation rule… |
| 2026-10-04 16:01:32 | [mage2kishan/module-notification-bar](https://www.nuget.org/packages/mage2kishan%2Fmodule-notification-bar) | 1.0.19 | Kishan Savaliya | Panth Notification Bar — display customizable notification bars, promo banners,… |
| 2026-10-04 16:10:41 | [veloxrouter/router](https://www.nuget.org/packages/veloxrouter%2Frouter) | v1.0.0 | Ortiz David | Lightning-fast HTTP routing engine for PHP |
| 2026-10-04 16:17:29 | [studioespresso/craft-varnish-purger](https://www.nuget.org/packages/studioespresso%2Fcraft-varnish-purger) | 1.0.0 | Studio Espresso | Tag-based Varnish purging for Craft CMS: tracks the elements and queries used o… |
| 2026-10-04 16:20:36 | [mage2kishan/module-performance-debugger](https://www.nuget.org/packages/mage2kishan%2Fmodule-performance-debugger) | 1.1.3 | Kishan Savaliya | Production-grade Magento 2 frontend performance debugger and profiler. Tracks b… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
