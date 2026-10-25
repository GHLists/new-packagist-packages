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

## Latest list — 2026-10-25 18:19 UTC

New packages created between 2026-10-25 17:22 UTC and 2026-10-25 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T18-19-14-914303Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 17:23:03 | [sergiynezbritskiy/magento2-translations-checker](https://www.nuget.org/packages/sergiynezbritskiy%2Fmagento2-translations-checker) | 1.0.0 |  | CLI tool to verify that every translatable phrase of a Magento 2 module is pres… |
| 2026-10-25 17:25:08 | [apiempresas/validar-cif](https://www.nuget.org/packages/apiempresas%2Fvalidar-cif) | v1.0.0 | APIEmpresas.es | Valida CIF, DNI y NIE españoles (formato y dígito de control). Sin dependencias. |
| 2026-10-25 17:42:43 | [bad_cluster/runway-queue-manager](https://www.nuget.org/packages/bad_cluster%2Frunway-queue-manager) | 1.0.0 | BaD ClusteR | Background job queue for Runway: the jobs in a database table, one worker at a… |
| 2026-10-25 17:45:45 | [edgeinfinity/flarum-dice](https://www.nuget.org/packages/edgeinfinity%2Fflarum-dice) | v0.1.0 | EdgeInfinity | Server-rolled inline dice for Flarum posts, with persistent results and configu… |
| 2026-10-25 17:55:11 | [teqnomaze/package-installer](https://www.nuget.org/packages/teqnomaze%2Fpackage-installer) | 1.0.0 |  | Installs packages of type custom-package into packages/<Name>/ |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
