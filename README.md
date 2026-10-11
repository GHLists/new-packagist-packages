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

## Latest list — 2026-10-11 05:19 UTC

New packages created between 2026-10-11 04:18 UTC and 2026-10-11 05:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T05-19-59-054734Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 04:30:07 | [antevemus/alinq-collection](https://www.nuget.org/packages/antevemus%2Falinq-collection) | v1.4.3 | Heliton Junior - CTO @ Anteve… | Enterprise LINQ-Style Collection Framework for PHP 8.4+ (Fluent API, Native Arr… |
| 2026-10-11 04:35:37 | [coretsia/platform-redaction](https://www.nuget.org/packages/coretsia%2Fplatform-redaction) | v0.8.0 | Vladyslav Mudrichenko | Coretsia sensitive-data redaction runtime package: deterministic classification… |
| 2026-10-11 04:45:07 | [msahidurr/laravel-deploy-notifier](https://www.nuget.org/packages/msahidurr%2Flaravel-deploy-notifier) | v1.0.0 | Sahidur Rahman | Git and deployment lifecycle notifications for Laravel, delivered to Telegram |
| 2026-10-11 04:55:55 | [patterns/event-channel](https://www.nuget.org/packages/patterns%2Fevent-channel) | v1.0.0 |  | Event Channel pattern - a transport-agnostic contract for publishing and subscr… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
