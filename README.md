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

## Latest list — 2026-10-25 13:20 UTC

New packages created between 2026-10-25 12:21 UTC and 2026-10-25 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T13-20-15-132484Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 12:34:07 | [marcosmarcolin/ixc-provedor-client](https://www.nuget.org/packages/marcosmarcolin%2Fixc-provedor-client) | v0.2.0 | Marcos Marcolin | PHP client for the IXC Provedor (IXCSoft) webservice API |
| 2026-10-25 13:00:08 | [scripthoodie/json-rpc](https://www.nuget.org/packages/scripthoodie%2Fjson-rpc) | v1.0.0 |  | Transport agnostic JSON-RPC 2.0 request and response components. |
| 2026-10-25 13:05:31 | [mischafierz/polyglot-cms](https://www.nuget.org/packages/mischafierz%2Fpolyglot-cms) | v1.0.0 |  | A CMS for websites: Go content API, PHP themes, TypeScript admin panel, SQLite… |
| 2026-10-25 13:06:48 | [garis-kode/adaptivecard-php](https://www.nuget.org/packages/garis-kode%2Fadaptivecard-php) | v1.0.1 | Garis Kode | Fluent PHP builder that programmatically constructs Adaptive Card (v1.6) JSON a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
