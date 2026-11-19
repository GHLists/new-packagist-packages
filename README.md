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

## Latest list — 2026-11-19 04:21 UTC

New packages created between 2026-11-19 03:19 UTC and 2026-11-19 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T04-21-49-183388Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 03:37:20 | [intelligence-cloud/sdk](https://www.nuget.org/packages/intelligence-cloud%2Fsdk) | v0.1.0 |  | PHP SDK for the Intelligence Cloud partner API: customer lifecycle and conversa… |
| 2026-11-19 04:05:08 | [ernestdefoe/community-reviews](https://www.nuget.org/packages/ernestdefoe%2Fcommunity-reviews) | 1.0.1 | Ernest Defoe | Community Reviews: a catalog of products your members review, with a rating and… |
| 2026-11-19 04:15:44 | [ernestdefoe/skylight](https://www.nuget.org/packages/ernestdefoe%2Fskylight) | 1.0.0 | Ernestdefoe | Skylight: a calm glass-and-daylight theme for Flarum 2, with a Studio where eac… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
