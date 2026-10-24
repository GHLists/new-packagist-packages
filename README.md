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

## Latest list — 2026-10-24 08:19 UTC

New packages created between 2026-10-24 07:18 UTC and 2026-10-24 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T08-19-12-151776Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 07:40:37 | [jass-sangha/agora](https://www.nuget.org/packages/jass-sangha%2Fagora) | v0.1.0 | Jass Sangha | Real-time Laravel chat package — 1-on-1 & group messaging, media sharing, react… |
| 2026-10-24 07:41:45 | [ameax/filter-core](https://www.nuget.org/packages/ameax%2Ffilter-core) | v1.0.0 | Michael Schmidt | Type-safe filtering system for Laravel with 6 filter types, 18 match modes, AND… |
| 2026-10-24 07:46:18 | [panda-men/think-queue-stream](https://www.nuget.org/packages/panda-men%2Fthink-queue-stream) | v0.1.0 |  | Redis Streams task queue for ThinkPHP 8 and PHP 8.2+ |
| 2026-10-24 08:05:23 | [slashmark/composer-suite](https://www.nuget.org/packages/slashmark%2Fcomposer-suite) | v1.0.0 | Slash Mark IT Solutions | PHP Package Intelligence Suite: 32 terminal tools to search, inspect, audit and… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
