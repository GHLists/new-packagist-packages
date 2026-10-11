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

## Latest list — 2026-10-11 09:20 UTC

New packages created between 2026-10-11 08:22 UTC and 2026-10-11 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T09-20-26-527489Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 08:50:28 | [cysquale/plays-games-widget](https://www.nuget.org/packages/cysquale%2Fplays-games-widget) | 1.1.2 | Cysquale | Plays Games Widget - TikTok-style HTML5 game feed with player scores, leaderboa… |
| 2026-10-11 09:05:36 | [antevemus/aspecification](https://www.nuget.org/packages/antevemus%2Faspecification) | v1.10.0 | Heliton Junior - CTO @ Anteve… | Enterprise Specification Pattern Framework for PHP 8.2+ (DDD, Notification Patt… |
| 2026-10-11 09:07:41 | [antevemus/alinq-collection](https://www.nuget.org/packages/antevemus%2Falinq-collection) | v1.5.1 | Heliton Junior - CTO @ Anteve… | Enterprise LINQ-Style Collection Framework for PHP 8.4+ (Fluent API, Native Arr… |
| 2026-10-11 09:08:14 | [units/ai](https://www.nuget.org/packages/units%2Fai) | v1.0.1 |  | AI unit - ask, chat and tool calling over an injected provider, on the patterns… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
