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

## Latest list — 2026-09-28 08:19 UTC

New packages created between 2026-09-28 07:23 UTC and 2026-09-28 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T08-19-27-209743Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 07:37:46 | [jigar-dhulla/swiggy-mcp](https://www.nuget.org/packages/jigar-dhulla%2Fswiggy-mcp) | v0.1.0 | Jigar Dhulla | A framework-agnostic PHP client for Swiggy's MCP servers: Food, Instamart, Dine… |
| 2026-09-28 07:38:36 | [michael-dev/identity_api](https://www.nuget.org/packages/michael-dev%2Fidentity_api) | 2.3 | michael-dev | Per-shop e-mail addresses (<prefix>-<shop>-<year>-<random>@domain) as Roundcube… |
| 2026-09-28 07:59:16 | [foxws/laravel-relatable](https://www.nuget.org/packages/foxws%2Flaravel-relatable) | v1.0.0 | francoism90 | Relate Eloquent models to other models, with a base score and boost to control… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
