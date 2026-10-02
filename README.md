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

## Latest list — 2026-10-02 14:19 UTC

New packages created between 2026-10-02 13:20 UTC and 2026-10-02 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T14-19-17-842649Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 13:30:45 | [adeshsuryan/next-cache-doctor](https://www.nuget.org/packages/adeshsuryan%2Fnext-cache-doctor) | v0.2.1 |  | Read a Next.js project and report cache layers that can stay stale after invali… |
| 2026-10-02 13:32:32 | [tommica/mailpox](https://www.nuget.org/packages/tommica%2Fmailpox) | v1.0.0 | Tom Mica | A local development mailbox for Laravel applications. |
| 2026-10-02 13:43:36 | [deepphp/laravel-slugify](https://www.nuget.org/packages/deepphp%2Flaravel-slugify) | v1.0.0 |  | Slug generation and uniqueness helpers for Laravel. |
| 2026-10-02 14:03:41 | [mage2kishan/magento2-claude-ai](https://www.nuget.org/packages/mage2kishan%2Fmagento2-claude-ai) | 1.9.1 | Kishan Savaliya | Magento 2 Automation with Claude AI - natural-language store management. Update… |
| 2026-10-02 14:13:59 | [amphp/uv](https://www.nuget.org/packages/amphp%2Fuv) | v0.3.1 | Bob Weinand; Aaron Piotrowski | PHP extension providing access to libuv functions |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
