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

## Latest list — 2026-10-03 14:19 UTC

New packages created between 2026-10-03 13:21 UTC and 2026-10-03 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T14-19-46-471541Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 13:27:42 | [benargo/saloon-graphql](https://www.nuget.org/packages/benargo%2Fsaloon-graphql) | v0.1.0 | Ben Argo | API-agnostic GraphQL layer for Saloon |
| 2026-10-03 13:41:29 | [mage2kishan/module-custom-options](https://www.nuget.org/packages/mage2kishan%2Fmodule-custom-options) | 1.0.11 | Kishan Savaliya | Panth Custom Options — beautifully styled product custom options for Hyva-based… |
| 2026-10-03 13:58:08 | [lodestone/lodestone](https://www.nuget.org/packages/lodestone%2Flodestone) | v0.1.0-alpha.1 | James Lomax | Server-driven UI for Laravel admin panels. Build pages, tables, forms and butto… |
| 2026-10-03 13:58:27 | [rondeto/jscontact](https://www.nuget.org/packages/rondeto%2Fjscontact) | v0.1.0 | Olivier Dolbeau | JSContact (RFC 9553) for PHP: a typed contact model with JSON reading, writing… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
