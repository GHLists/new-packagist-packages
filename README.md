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

## Latest list — 2026-11-01 11:20 UTC

New packages created between 2026-11-01 10:20 UTC and 2026-11-01 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T11-20-30-83738Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 11:02:38 | [voku/agent-skills](https://www.nuget.org/packages/voku%2Fagent-skills) | v0.1.0 |  | Portable, tool-neutral engineering skills for coding agents. |
| 2026-11-01 11:08:42 | [passioncorners/up-keep-agent](https://www.nuget.org/packages/passioncorners%2Fup-keep-agent) | v1.0.0 |  | Reports a Laravel app's errors, health and server stats to up-keep on one secre… |
| 2026-11-01 11:10:34 | [tualo/dbchecker](https://www.nuget.org/packages/tualo%2Fdbchecker) | 1.0.1 |  | DB Vitality Package Tualo Office |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
