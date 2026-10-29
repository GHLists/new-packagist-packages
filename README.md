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

## Latest list — 2026-10-29 21:21 UTC

New packages created between 2026-10-29 20:22 UTC and 2026-10-29 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T21-21-55-75727Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 20:35:44 | [laravelopenpackages/heartbeat](https://www.nuget.org/packages/laravelopenpackages%2Fheartbeat) | v1.0.0 | Zeeshan Ali | One tiny poll tells every open page what changed — live-feeling Laravel apps wi… |
| 2026-10-29 20:39:19 | [ernestdefoe/syllabus](https://www.nuget.org/packages/ernestdefoe%2Fsyllabus) | 1.0.0 | Ernest Defoe | Syllabus — courses inside your Flarum forum. Text, video, assignment and quiz l… |
| 2026-10-29 20:55:14 | [galillei/magento-oauth-client](https://www.nuget.org/packages/galillei%2Fmagento-oauth-client) | v1.0.1 | Vinduesgrossisten | Magento 2 REST API client with OAuth 1.0a (HMAC-SHA256) request signing and a c… |
| 2026-10-29 21:01:32 | [camanru/fastleo](https://www.nuget.org/packages/camanru%2Ffastleo) | 4.0.0 | Roman Zakharov | Admin panel for Laravel sites: each section is described by a single resource c… |
| 2026-10-29 21:06:28 | [ernestdefoe/moments](https://www.nuget.org/packages/ernestdefoe%2Fmoments) | 1.0.0 | Ernest Defoe | Moments — a microblogging social feed for Flarum 2. Short posts in a timeline b… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
