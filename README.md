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

## Latest list — 2026-11-24 09:19 UTC

New packages created between 2026-11-24 08:19 UTC and 2026-11-24 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T09-19-19-325306Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 08:59:57 | [filefabrik/rfc9421](https://www.nuget.org/packages/filefabrik%2Frfc9421) | v1.10.6 | RT Filefabrik | Create and validate RFC 9421 HTTP Signatures for ActivityPub. |
| 2026-11-24 09:02:41 | [b2pweb/bdf-api](https://www.nuget.org/packages/b2pweb%2Fbdf-api) | v1.0.0 |  | Bdf Soap Api component |
| 2026-11-24 09:06:05 | [packstub/filament-saas-starter](https://www.nuget.org/packages/packstub%2Ffilament-saas-starter) | v1.0.0 | Packstub | A multi-tenant SaaS starter kit for Laravel and Filament: sign-up, workspaces,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
