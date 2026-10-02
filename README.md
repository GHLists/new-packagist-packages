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

## Latest list — 2026-10-02 02:21 UTC

New packages created between 2026-10-02 01:20 UTC and 2026-10-02 02:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T02-21-45-607734Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 01:31:08 | [clicalmani/notification](https://www.nuget.org/packages/clicalmani%2Fnotification) | v1.0.0 | clicalmani | A notification package for Tonka |
| 2026-10-02 01:44:56 | [clicalmani/queue](https://www.nuget.org/packages/clicalmani%2Fqueue) | v1.0.0-alpha | clicalmani | Queue package for Tonka framework |
| 2026-10-02 01:50:24 | [leopoletto/robots-txt-parser](https://www.nuget.org/packages/leopoletto%2Frobots-txt-parser) | v1.0.0 | Leonardo Poletto | A comprehensive PHP package for parsing robots.txt files, including support for… |
| 2026-10-02 01:52:54 | [marque/marque](https://www.nuget.org/packages/marque%2Fmarque) | v1.0.0 | Letter Of Marque Software | The Marque installer — one require, then `php artisan marque:install` wires a w… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
