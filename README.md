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

## Latest list — 2026-11-01 19:19 UTC

New packages created between 2026-11-01 18:18 UTC and 2026-11-01 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T19-19-55-873449Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 18:22:59 | [tacraft-sociality/flarum-auto-dpr](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-auto-dpr) | 1.0.0 | Tacraft Sociality | Automatically and permanently delete user-deleted (hidden) discussions and post… |
| 2026-11-01 19:15:46 | [wssolutions/contao-web-content-access](https://www.nuget.org/packages/wssolutions%2Fcontao-web-content-access) | v1.0.0 | WS SOLUTIONS LLC | Accessibility for Contao sites (BFSG / European Accessibility Act): accessibili… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
