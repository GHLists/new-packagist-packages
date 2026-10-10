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

## Latest list — 2026-10-10 18:19 UTC

New packages created between 2026-10-10 17:20 UTC and 2026-10-10 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T18-19-06-494846Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 17:20:23 | [novay/minios](https://www.nuget.org/packages/novay%2Fminios) | 0.1.0 | Noviyanto Rahmadi | MiniOS Desktop Environment for Laravel |
| 2026-10-10 17:55:41 | [rasuvaeff/context-http](https://www.nuget.org/packages/rasuvaeff%2Fcontext-http) | v0.1.0 | Victor Razuvaev | PSR HTTP adapters for rasuvaeff/context |
| 2026-10-10 17:57:50 | [tmonier/sylius-gpsr-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-gpsr-plugin) | v1.0.0 | Thibaut Monier | EU General Product Safety Regulation (GPSR, Regulation (EU) 2023/988, Art. 19)… |
| 2026-10-10 17:58:58 | [antevemus/aspecification](https://www.nuget.org/packages/antevemus%2Faspecification) | v1.6.1 | Heliton Junior - CTO @ Anteve… | Enterprise Specification Pattern Framework for PHP 8.2+ (DDD, Notification Patt… |
| 2026-10-10 17:59:17 | [antevemus/alinq-collection](https://www.nuget.org/packages/antevemus%2Falinq-collection) | v1.4.1 | Heliton Junior - CTO @ Anteve… | Enterprise LINQ-Style Collection Framework for PHP 8.4+ (Fluent API, Native Arr… |
| 2026-10-10 18:08:52 | [rasuvaeff/context](https://www.nuget.org/packages/rasuvaeff%2Fcontext) | v0.1.0 | Victor Razuvaev | Deadline, cancellation and request-scoped values for PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
