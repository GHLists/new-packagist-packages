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

## Latest list — 2026-10-19 23:22 UTC

New packages created between 2026-10-19 22:19 UTC and 2026-10-19 23:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T23-22-56-205394Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 22:21:21 | [openthc/api](https://www.nuget.org/packages/openthc%2Fapi) | 420.26.292 |  | OpenTHC API |
| 2026-10-19 22:30:16 | [afurgeri/laravel-short-links](https://www.nuget.org/packages/afurgeri%2Flaravel-short-links) | v0.1.1 |  | Trackable short links for Laravel with SQL and MongoDB storage. |
| 2026-10-19 23:00:38 | [tryhackx/flarum-cover-studio](https://www.nuget.org/packages/tryhackx%2Fflarum-cover-studio) | v2.3.0 | TryHackX | Profile covers with repositionable focal point (pos-crop), fully integrated wit… |
| 2026-10-19 23:08:37 | [tryhackx/flarum-advanced-pages](https://www.nuget.org/packages/tryhackx%2Fflarum-advanced-pages) | 2.4.0 | TryHackX | Create advanced custom pages with HTML, BBCode, Markdown, PHP, or plain text, f… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
