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

## Latest list — 2026-10-30 10:20 UTC

New packages created between 2026-10-30 09:21 UTC and 2026-10-30 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T10-20-40-921294Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 09:28:24 | [patrickfischer/monolog-ntfy-safe](https://www.nuget.org/packages/patrickfischer%2Fmonolog-ntfy-safe) | 1.0.2 | Patrick Fischer | A non fatal version of a Monolog handler for ntfy.sh |
| 2026-10-30 09:30:31 | [waqas-badar/php-saga](https://www.nuget.org/packages/waqas-badar%2Fphp-saga) | v1.0.1 | Waqas Badar; Antigravity (Goo… | A lightweight, framework-agnostic Saga orchestrator for PHP. |
| 2026-10-30 09:32:45 | [mammothwp/wp-kit](https://www.nuget.org/packages/mammothwp%2Fwp-kit) | v2.0.1 | Mammoth WP | Declare a WordPress feature once and expose it as a REST route, a WP-CLI comman… |
| 2026-10-30 09:42:59 | [mage2kishan/module-ai-visibility](https://www.nuget.org/packages/mage2kishan%2Fmodule-ai-visibility) | 1.0.0 | Kishan Savaliya | Panth AI Visibility - analytics for Magento 2 that counts AI crawler requests (… |
| 2026-10-30 09:55:02 | [mammothwp/wp-release](https://www.nuget.org/packages/mammothwp%2Fwp-release) | v1.0.0 | Mammoth WP | Prepare, verify and ship a Mammoth WP plugin release to wordpress.org and GitHu… |
| 2026-10-30 09:56:28 | [mammothwp/support](https://www.nuget.org/packages/mammothwp%2Fsupport) | v1.1.0 | Mammoth WP | One shared Support screen for every plugin that bundles it: the customer fills… |
| 2026-10-30 10:17:59 | [artisan-build/telltale-crashes](https://www.nuget.org/packages/artisan-build%2Ftelltale-crashes) | v1.2.0 |  | NativePHP Mobile crash collection and typed Telltale outbox import. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
