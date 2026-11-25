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

## Latest list — 2026-11-25 23:19 UTC

New packages created between 2026-11-25 22:19 UTC and 2026-11-25 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T23-19-20-253665Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 22:23:28 | [atom-fm/framework](https://www.nuget.org/packages/atom-fm%2Fframework) | v0.1.0 |  | Atom Framework |
| 2026-11-25 22:33:46 | [atom-fm/lucide](https://www.nuget.org/packages/atom-fm%2Flucide) | v0.1.0 |  | Lucide icon resolver for Atom Framework |
| 2026-11-25 22:36:49 | [atom-fm/starter](https://www.nuget.org/packages/atom-fm%2Fstarter) | v0.1.0 |  | A minimal Atom application with SQLite and Accounts |
| 2026-11-25 22:47:48 | [ghazali/epass-package](https://www.nuget.org/packages/ghazali%2Fepass-package) | v1.0.1 |  | Headless Laravel package for ePass authentication, passport verification, and P… |
| 2026-11-25 22:50:30 | [debuss-a/piccolo-container](https://www.nuget.org/packages/debuss-a%2Fpiccolo-container) | 0.1.0 | Alexandre Debusschère | A PSR-11 dependency injection container with singleton, scoped and transient li… |
| 2026-11-25 22:52:42 | [nr/emailservice](https://www.nuget.org/packages/nr%2Femailservice) | 3.0.0 |  | ProcessWire module for templated emails with CSS inlining and logging |
| 2026-11-25 23:12:40 | [debuss-a/piccolo-framework](https://www.nuget.org/packages/debuss-a%2Fpiccolo-framework) | 0.1.0 | Alexandre Debusschère | The framework of the Piccolo skeleton: a PSR-15 application built on Laminas St… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
