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

## Latest list — 2026-11-09 05:20 UTC

New packages created between 2026-11-09 04:21 UTC and 2026-11-09 05:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T05-20-19-525977Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 04:25:33 | [grazulex/lardefset](https://www.nuget.org/packages/grazulex%2Flardefset) | v0.1.0 | Jean-Marc Strauven | Default settings for Laravel projects. |
| 2026-11-09 04:25:57 | [moztopia/access](https://www.nuget.org/packages/moztopia%2Faccess) | 0.9.1 |  | Explicit global and team-scoped roles and permissions for Laravel. |
| 2026-11-09 04:56:47 | [alan2k2/cna-framework](https://www.nuget.org/packages/alan2k2%2Fcna-framework) | v1.0.0 | Alan Shaju | CnA Framework - The Contract-Driven, High-Performance PHP 8.4+ Framework |
| 2026-11-09 04:59:55 | [jund-fauz/filament-kompact](https://www.nuget.org/packages/jund-fauz%2Ffilament-kompact) | v0.1.1 | jund-fauz | A set of helper functions and macros in building app using Filament in Laravel |
| 2026-11-09 05:00:35 | [atannex/panels](https://www.nuget.org/packages/atannex%2Fpanels) | v1.0.0 | Atanga Leke Collins | Many back-office panels in one Laravel app: one panel per system on its own hos… |
| 2026-11-09 05:01:40 | [sahanranasingha/sri-lanka-holidays](https://www.nuget.org/packages/sahanranasingha%2Fsri-lanka-holidays) | v1.1.1 | Sahan Ranasingha | Official Sri Lanka Public, Bank, and Mercantile holidays (including Full Moon P… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
