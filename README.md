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

## Latest list — 2026-11-17 21:21 UTC

New packages created between 2026-11-17 20:20 UTC and 2026-11-17 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T21-21-45-935034Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 20:28:16 | [thebeardedbear/urssaf-tierce-declaration-paje](https://www.nuget.org/packages/thebeardedbear%2Furssaf-tierce-declaration-paje) | v0.1.0 | The Bearded Bear | Client and domain model for the URSSAF "API Tierce Déclaration PAJE" (third-par… |
| 2026-11-17 20:49:11 | [z3l/fasthtmlparser](https://www.nuget.org/packages/z3l%2Ffasthtmlparser) | v0.1.0 | z3l | Fast HTML / XML parser for scraping, with XPath 1.0 and CSS selectors. PHP port… |
| 2026-11-17 21:08:39 | [backdrop-dev/attr](https://www.nuget.org/packages/backdrop-dev%2Fattr) | v1.0.0 | Benjamin Lu | Backdrop Attr provides devs a system for adding filterable attributes. This is… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
