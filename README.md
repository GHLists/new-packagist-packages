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

## Latest list — 2026-10-19 14:22 UTC

New packages created between 2026-10-19 13:20 UTC and 2026-10-19 14:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T14-22-29-05493Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 13:24:53 | [fruitcake/phpunit-tia-laravel](https://www.nuget.org/packages/fruitcake%2Fphpunit-tia-laravel) | v0.1.0 | Barry vd. Heuvel | Laravel integration for phpunit-tia: links tests to the views they render and t… |
| 2026-10-19 13:37:21 | [njdigitallab/laranonce](https://www.nuget.org/packages/njdigitallab%2Flaranonce) | v1.0.0 | Jenry Ollivierre | A nounce generator for Laravel applications. |
| 2026-10-19 13:39:33 | [siberfx/chat-hybrid-ai](https://www.nuget.org/packages/siberfx%2Fchat-hybrid-ai) | v2.0.0 | Siberfx | API-first hybrid chat for Laravel: chat bubble, admin inbox, AI agents (Laravel… |
| 2026-10-19 13:46:08 | [lzk/laravel-duplicate-detector](https://www.nuget.org/packages/lzk%2Flaravel-duplicate-detector) | v0.1.0 |  | Configurable, explainable read-only exact and fuzzy duplicate detection for Lar… |
| 2026-10-19 13:56:04 | [salimi-my/admin-dashboard-template](https://www.nuget.org/packages/salimi-my%2Fadmin-dashboard-template) | v1.0.0 |  | A Laravel and Inertia React admin dashboard starter kit with a floating sidebar… |
| 2026-10-19 14:03:01 | [scottoffen/wp-github-updater](https://www.nuget.org/packages/scottoffen%2Fwp-github-updater) | v1.0.0 | Scott Offen | Update WordPress plugins and themes from GitHub releases using both public and… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
