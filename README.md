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

## Latest list — 2026-09-29 00:20 UTC

New packages created between 2026-09-28 23:21 UTC and 2026-09-29 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T00-20-50-462218Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 23:22:00 | [upbot/dependencies](https://www.nuget.org/packages/upbot%2Fdependencies) | v0.1.0 |  | Send a minimal Composer/npm dependency inventory to UpBot |
| 2026-09-28 23:31:11 | [upbot/laravel-dependencies](https://www.nuget.org/packages/upbot%2Flaravel-dependencies) | v0.1.0 |  | UpBot dependency reports through Laravel Artisan and Scheduler |
| 2026-09-28 23:48:58 | [monkeyscloud/monkeyslegion-feature-flags](https://www.nuget.org/packages/monkeyscloud%2Fmonkeyslegion-feature-flags) | 1.0.0 |  | Feature flags package for MonKeysLegion framework |
| 2026-09-28 23:48:59 | [4rn0/statamic-cp-bar](https://www.nuget.org/packages/4rn0%2Fstatamic-cp-bar) | v1.0.0 | Arno Hoogma | WordPress's admin bar, rebuilt for Statamic: edit, add and refresh any page fro… |
| 2026-09-28 23:49:31 | [monkeyscloud/monkeyslegion-webhooks](https://www.nuget.org/packages/monkeyscloud%2Fmonkeyslegion-webhooks) | 1.0.0 |  | Webhook management package for MonKeysLegion framework |
| 2026-09-28 23:50:05 | [monkeyscloud/monkeyslegion-markdown](https://www.nuget.org/packages/monkeyscloud%2Fmonkeyslegion-markdown) | 1.0.0 |  | Markdown rendering package for MonKeysLegion framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
