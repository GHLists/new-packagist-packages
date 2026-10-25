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

## Latest list — 2026-10-25 12:21 UTC

New packages created between 2026-10-25 11:19 UTC and 2026-10-25 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T12-21-34-860902Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 11:40:20 | [baptchau/feature-manager](https://www.nuget.org/packages/baptchau%2Ffeature-manager) | v0.1.0 | BaptChau | Feature flag manager configured from a YAML file |
| 2026-10-25 11:45:59 | [ptbdynamic/plinth](https://www.nuget.org/packages/ptbdynamic%2Fplinth) | v0.1.1 |  | Plinth, the design system of BDynamic's projects: Blade components, a Filament… |
| 2026-10-25 12:01:14 | [blackcube/starter](https://www.nuget.org/packages/blackcube%2Fstarter) | 1.0.0 | Philippe Gaultier | Blackcube CMS starter |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
