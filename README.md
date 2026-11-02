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

## Latest list — 2026-11-02 04:20 UTC

New packages created between 2026-11-02 03:19 UTC and 2026-11-02 04:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T04-20-55-222958Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 03:48:25 | [atannex/atannex-provider](https://www.nuget.org/packages/atannex%2Fatannex-provider) | v1.0.0 | Atanga Leke Collins | A base Laravel service provider for packages: declare config files, routes, mig… |
| 2026-11-02 03:59:44 | [polidog/rosanna-state](https://www.nuget.org/packages/polidog%2Frosanna-state) | v0.1.0 | polidog | Server-side state for Rosanna: hooks, signed actions, CSRF, snapshots, storage… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
