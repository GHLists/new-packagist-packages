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

## Latest list — 2026-11-09 13:20 UTC

New packages created between 2026-11-09 12:18 UTC and 2026-11-09 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T13-20-03-862551Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 12:26:09 | [brandejt/dresscode-standard](https://www.nuget.org/packages/brandejt%2Fdresscode-standard) | v1.0.0 | Tomáš Brandejs | Coding standard for DressCode: twenty rules and two presets, PER Coding Style w… |
| 2026-11-09 12:30:20 | [omaresmael/thread](https://www.nuget.org/packages/omaresmael%2Fthread) | v1.0.0 |  | Run Laravel closures on a pool of pre-booted ext-parallel threads |
| 2026-11-09 12:31:27 | [euginepj/laravel-api-specs](https://www.nuget.org/packages/euginepj%2Flaravel-api-specs) | v1.0.0 | Eugine | Interactive, modern 2-column REST API documentation portal for Laravel applicat… |
| 2026-11-09 12:55:28 | [anjan011/roles-and-permissions](https://www.nuget.org/packages/anjan011%2Froles-and-permissions) | v1.0.0 | Anjan | A simple and easy-to-use way to manage roles and permissions in Laravel applica… |
| 2026-11-09 13:02:11 | [teufels/tt3-stackmonitor](https://www.nuget.org/packages/teufels%2Ftt3-stackmonitor) | 1.0.0 | teufels GmbH | [teufels] stackmonitor - Secret-protected /stackmonitor endpoint that reports C… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
