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

## Latest list — 2026-11-14 04:18 UTC

New packages created between 2026-11-14 03:18 UTC and 2026-11-14 04:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T04-18-37-204709Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 03:27:59 | [ecuafact/sdk](https://www.nuget.org/packages/ecuafact%2Fsdk) | v1.0.0 | Ecuanexus | Cliente oficial de Ecuafact para PHP: emite y consulta los seis comprobantes el… |
| 2026-11-14 03:41:25 | [jimbo2150/php-css-typed-om](https://www.nuget.org/packages/jimbo2150%2Fphp-css-typed-om) | v1.1.0 | Jim Robinson | PHP implementation of the CSS Object Model and Typed Object Model (OM). |
| 2026-11-14 03:58:56 | [vairity/mautic-conversion-pages](https://www.nuget.org/packages/vairity%2Fmautic-conversion-pages) | v1.0.0 | Vairity | Vairity Build: Conversion Pages for Mautic. Landing pages and microsites built,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
