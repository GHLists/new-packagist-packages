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

## Latest list — 2026-10-20 00:20 UTC

New packages created between 2026-10-19 23:22 UTC and 2026-10-20 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T00-20-28-139Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 23:25:00 | [tryhackx/flarum-topic-rating](https://www.nuget.org/packages/tryhackx%2Fflarum-topic-rating) | 2.6.0 | TryHackX | Interactive 5-star topic rating system for Flarum with half-star precision, liv… |
| 2026-10-19 23:33:47 | [tryhackx/flarum-thumb-sliders](https://www.nuget.org/packages/tryhackx%2Fflarum-thumb-sliders) | 2.2.0 | TryHackX | Extracts images automatically from the first post to display an animated, lazy-… |
| 2026-10-19 23:39:29 | [tryhackx/flarum-magnet-link](https://www.nuget.org/packages/tryhackx%2Fflarum-magnet-link) | 2.10.0 | TryHackX | Secure magnet link integration for Flarum with SHA-256 token protection, SSRF-h… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
