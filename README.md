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

## Latest list — 2026-10-15 11:22 UTC

New packages created between 2026-10-15 10:23 UTC and 2026-10-15 11:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T11-22-25-361409Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 10:49:14 | [vielhuber/codechecker](https://www.nuget.org/packages/vielhuber%2Fcodechecker) | 1.0.0 |  | Read-only PHP and JavaScript code checks through a PHP API, CLI and MCP server. |
| 2026-10-15 11:01:08 | [postilio/postilio-php](https://www.nuget.org/packages/postilio%2Fpostilio-php) | v0.1.0-alpha.1 |  | The official PHP client for the Postilio API: European transactional email. |
| 2026-10-15 11:08:37 | [juststeveking/api-toolbox](https://www.nuget.org/packages/juststeveking%2Fapi-toolbox) | v0.1.0 | Steve McDougall | Standards-compliant APIs in Laravel, one RFC at a time. |
| 2026-10-15 11:18:21 | [systopic/relay](https://www.nuget.org/packages/systopic%2Frelay) | v1.0.1 |  | Live updates for the systopic packages: what a page rendered from, what a reque… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
