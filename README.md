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

## Latest list — 2026-11-03 21:19 UTC

New packages created between 2026-11-03 20:21 UTC and 2026-11-03 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T21-19-51-419566Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 20:26:12 | [tamino-gateway/sdk](https://www.nuget.org/packages/tamino-gateway%2Fsdk) | v1.0.0 | Tamino | Official PHP SDK for the Tamino payments API (/v1): Pix, boleto, cards, payouts… |
| 2026-11-03 20:28:56 | [sandritsch91/php-science](https://www.nuget.org/packages/sandritsch91%2Fphp-science) | 1.0.0 |  | Exact, dimension-aware physical quantities and SI units for PHP |
| 2026-11-03 20:39:52 | [r2soft/nfse-nacional](https://www.nuget.org/packages/r2soft%2Fnfse-nacional) | v1.0.0 |  | Emissão de NFS-e pelo padrão nacional (API Sefin Nacional): DPS 1.01 assinada,… |
| 2026-11-03 21:02:45 | [phpoffice/phpdatabase](https://www.nuget.org/packages/phpoffice%2Fphpdatabase) | 0.1.0 | Franck Lefevre | PhpOffice\PhpDatabase - Read, Create and Write database documents (ACCDB, ODB,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
