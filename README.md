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

## Latest list — 2026-10-19 13:20 UTC

New packages created between 2026-10-19 12:20 UTC and 2026-10-19 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T13-20-08-754488Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 12:27:35 | [weldist/laravel-passport-client-scopes](https://www.nuget.org/packages/weldist%2Flaravel-passport-client-scopes) | v1.0.0 | X-Adam | Per-client default scopes and RFC 6750 bearer challenges for Laravel Passport c… |
| 2026-10-19 12:32:41 | [frozenplain/flarum-ext-connect](https://www.nuget.org/packages/frozenplain%2Fflarum-ext-connect) | v1.0.0 |  | Optional sign-in to the FrozenPlain forum with a frozenplain.com account. |
| 2026-10-19 12:37:34 | [contenir/extension-api](https://www.nuget.org/packages/contenir%2Fextension-api) | v0.1.0 |  | The add-on API for Contenir CMS: the contracts add-ons build against, the event… |
| 2026-10-19 12:45:59 | [neckarpixel/contao-nptabs-bundle](https://www.nuget.org/packages/neckarpixel%2Fcontao-nptabs-bundle) | 1.0.0 | Neckarpixel | Barrierefreie, responsive Tabs (WAI-ARIA APG, WCAG 2.2 AA) als verschachteltes… |
| 2026-10-19 12:54:05 | [contenir/queue](https://www.nuget.org/packages/contenir%2Fqueue) | v0.1.0 |  | Durable jobs, retries and schedules for Contenir CMS, with a cron-friendly work… |
| 2026-10-19 13:00:21 | [yorvolabs/canary](https://www.nuget.org/packages/yorvolabs%2Fcanary) | v1.0.0 | Darko Poposki | Secure, auditable HTTP endpoints for health monitoring, cache management, and d… |
| 2026-10-19 13:00:25 | [yorvolabs/canary-bridge-shopware](https://www.nuget.org/packages/yorvolabs%2Fcanary-bridge-shopware) | 1.0.0 | Darko Poposki | Shopware 6.6+ plugin bridge for yorvolabs/canary — secure health, cache, and de… |
| 2026-10-19 13:07:47 | [elife/patterns](https://www.nuget.org/packages/elife%2Fpatterns) | v1.0.0-beta |  | eLife patterns |
| 2026-10-19 13:18:06 | [laraarabdev/laravel-turbo-tags](https://www.nuget.org/packages/laraarabdev%2Flaravel-turbo-tags) | v0.1.0 | LaraArabDev | A high-performance polymorphic tagging system with translation support for Lara… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
