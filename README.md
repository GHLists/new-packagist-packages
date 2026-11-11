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

## Latest list — 2026-11-11 14:20 UTC

New packages created between 2026-11-11 13:22 UTC and 2026-11-11 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T14-20-33-190304Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 13:22:43 | [callismart/request-parser](https://www.nuget.org/packages/callismart%2Frequest-parser) | v1.0.0 | Callistus Nwachukwu | Streaming HTTP request body parser for PHP. Fills the gaps in native $_POST/$_F… |
| 2026-11-11 13:27:24 | [ernestdefoe/answers](https://www.nuget.org/packages/ernestdefoe%2Fanswers) | 1.0.0 | Ernest Defoe | Answers: Stack Overflow-style questions and answers for any tag. Answers sorted… |
| 2026-11-11 13:42:13 | [azhimov/laravel-outbox](https://www.nuget.org/packages/azhimov%2Flaravel-outbox) | v0.1.0 | Zhanibek Azhimov | Transactional outbox and inbox for Laravel: publish events in the same database… |
| 2026-11-11 13:53:27 | [maize-tech/laravel-access-logs](https://www.nuget.org/packages/maize-tech%2Flaravel-access-logs) | 1.0.0 | Enrico De Lazzari | Easily log daily user access to your Laravel application |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
