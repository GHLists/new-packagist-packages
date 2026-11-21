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

## Latest list — 2026-11-21 09:20 UTC

New packages created between 2026-11-21 08:21 UTC and 2026-11-21 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T09-20-54-679952Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 08:32:38 | [maarheeze/compass](https://www.nuget.org/packages/maarheeze%2Fcompass) | 1.0.0 |  | Repository and deployment status dashboard for GitHub and Laravel Forge |
| 2026-11-21 08:59:03 | [italystrap/empress-cache](https://www.nuget.org/packages/italystrap%2Fempress-cache) | 1.0.0 | overclokk | File based cache for the providers configuration aggregated by italystrap/empre… |
| 2026-11-21 09:19:01 | [datacircle/laragent-tools](https://www.nuget.org/packages/datacircle%2Flaragent-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. Four LarAgent tools call Datacircle's public API. You n… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
