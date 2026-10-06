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

## Latest list — 2026-10-06 07:20 UTC

New packages created between 2026-10-06 06:21 UTC and 2026-10-06 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T07-20-24-603646Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 06:42:22 | [themusicdev/edge-cache](https://www.nuget.org/packages/themusicdev%2Fedge-cache) | v1.0.0 | TheMusicDev | CakePHP 5 plugin: cache headers for CDN-fronted sites (public pages cached at t… |
| 2026-10-06 06:42:23 | [calisero/calisero-symfony](https://www.nuget.org/packages/calisero%2Fcalisero-symfony) | 1.0.1 | Calisero | Symfony bundle for sending SMS through the Calisero API |
| 2026-10-06 06:43:24 | [helsingborg-stad/wpmu-noindex-by-config](https://www.nuget.org/packages/helsingborg-stad%2Fwpmu-noindex-by-config) | 0.1.2 | Thor Brink | Disables indexing for the all sites based on configuration. |
| 2026-10-06 06:45:37 | [weijukeji/laravel-ekp-org-sync](https://www.nuget.org/packages/weijukeji%2Flaravel-ekp-org-sync) | v1.0.0 |  | Reusable EKP organization synchronization into the optional Laravel IAM directo… |
| 2026-10-06 07:01:36 | [digicademy/typo3-sentry-transaction-handler](https://www.nuget.org/packages/digicademy%2Ftypo3-sentry-transaction-handler) | 1.0.0 | Frodo Podschwadek | Opens a Sentry transaction per TYPO3 request so traces_sample_rate actually pro… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
