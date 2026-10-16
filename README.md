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

## Latest list — 2026-10-16 10:19 UTC

New packages created between 2026-10-16 09:19 UTC and 2026-10-16 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T10-19-52-845018Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 09:42:10 | [futura/contao-dynamic-snippets](https://www.nuget.org/packages/futura%2Fcontao-dynamic-snippets) | v1.0.0 | Dinko Skopljak | HTML-Snippets mit Platzhaltern als wiederverwendbare Inhaltselemente für Contao… |
| 2026-10-16 09:45:15 | [teufels/tt3-wellknown](https://www.nuget.org/packages/teufels%2Ftt3-wellknown) | 1.0.0 | teufels GmbH | [teufels] well-known - Serve the well-known resources a TYPO3 site should provi… |
| 2026-10-16 09:46:16 | [everysize/checkout-woocommerce](https://www.nuget.org/packages/everysize%2Fcheckout-woocommerce) | v1.0.0 | everysize GmbH | everysize Checkout – Plugin für WooCommerce |
| 2026-10-16 09:52:26 | [php-forge/debug-core](https://www.nuget.org/packages/php-forge%2Fdebug-core) | 0.1.0 | Wilmer Arambula | Framework-agnostic snapshots, storage, and frontend for PHP debug adapters. |
| 2026-10-16 09:55:34 | [ithilbert/consentlaw-client](https://www.nuget.org/packages/ithilbert%2Fconsentlaw-client) | 1.0.0 | Jörg Hilbert | Client für die consentLaw-API – ruft Rechtstexte (Impressum, Datenschutz, AGB,… |
| 2026-10-16 09:56:12 | [balpom/types](https://www.nuget.org/packages/balpom%2Ftypes) | v1.0.0 | Mikhail (Balpom) | Library for PHP type checking and type casting. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
