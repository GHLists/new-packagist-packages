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

## Latest list — 2026-10-26 07:20 UTC

New packages created between 2026-10-26 06:18 UTC and 2026-10-26 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T07-20-57-234894Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 06:23:12 | [gzxy/flysystem-qiniu](https://www.nuget.org/packages/gzxy%2Fflysystem-qiniu) | 3.2.7 | gzxy | Flysystem adapter for the Qiniu storage. |
| 2026-10-26 06:30:10 | [mj-zana/audit](https://www.nuget.org/packages/mj-zana%2Faudit) | v2.2.0 |  | Content revisions for Zana applications: who changed what and when, per locale,… |
| 2026-10-26 06:30:12 | [mj-zana/media](https://www.nuget.org/packages/mj-zana%2Fmedia) | v2.2.0 |  | Responsive images for Zana applications: WebP and AVIF variants, metadata strip… |
| 2026-10-26 06:30:12 | [mj-zana/scheduler](https://www.nuget.org/packages/mj-zana%2Fscheduler) | v2.2.0 |  | Scheduled tasks for Zana applications: cron expressions, a scope per run, overl… |
| 2026-10-26 06:30:12 | [mj-zana/session](https://www.nuget.org/packages/mj-zana%2Fsession) | v2.2.0 |  | Server-side sessions and flash messages for Zana applications, stored in a PSR-… |
| 2026-10-26 06:30:13 | [mj-zana/view-markdown](https://www.nuget.org/packages/mj-zana%2Fview-markdown) | v2.2.0 |  | Safe Markdown rendering for mj-zana/view, on league/commonmark |
| 2026-10-26 06:59:14 | [gzxy/laravel-filesystem-qiniu](https://www.nuget.org/packages/gzxy%2Flaravel-filesystem-qiniu) | v3.0.1 | gzxy | A Qiniu storage filesystem for Laravel. |
| 2026-10-26 07:07:24 | [shoplygg/shoply-php](https://www.nuget.org/packages/shoplygg%2Fshoply-php) | v0.6.0 |  | Shoply's API from your own server: every route as a method, safe retries, pages… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
