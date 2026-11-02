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

## Latest list — 2026-11-02 02:19 UTC

New packages created between 2026-11-02 01:20 UTC and 2026-11-02 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T02-19-05-194515Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 01:42:45 | [trevol/trevol-php](https://www.nuget.org/packages/trevol%2Ftrevol-php) | v0.1.0 | Joshua Montclair (Trevol) | SDK de PHP para la API de Trevol (facturación electrónica y demás documentos an… |
| 2026-11-02 01:51:13 | [omacy/ledgerbeetle](https://www.nuget.org/packages/omacy%2Fledgerbeetle) | v0.1.1 | Shamsuddeen | Double-entry ledger for Laravel, backed by TigerBeetle. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
