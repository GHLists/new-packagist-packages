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

## Latest list — 2026-10-12 14:21 UTC

New packages created between 2026-10-12 13:18 UTC and 2026-10-12 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T14-21-41-940083Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 13:31:39 | [zcwilt/forumkit-forums](https://www.nuget.org/packages/zcwilt%2Fforumkit-forums) | v0.1.0 |  | Forums for ForumKit: forum groups, forums, threads and posts, visibility and po… |
| 2026-10-12 13:31:56 | [ichinya/laratesto-rector](https://www.nuget.org/packages/ichinya%2Flaratesto-rector) | 0.1.0 | Ichi | Rector rules to migrate Laravel PHPUnit test suites to Laratesto. |
| 2026-10-12 13:38:04 | [momh/shroud](https://www.nuget.org/packages/momh%2Fshroud) | v0.1.0 | bricebou | Deterministic, CMS-agnostic pseudonymisation of a relational database: consiste… |
| 2026-10-12 13:58:33 | [mdoq/infrastructure](https://www.nuget.org/packages/mdoq%2Finfrastructure) | 1.0.0 |  | MDOQ infrastructure module for MAP integration |
| 2026-10-12 14:02:29 | [zero1/request-limiter](https://www.nuget.org/packages/zero1%2Frequest-limiter) | 1.0.0 |  | Request limiter for Magento 2 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
