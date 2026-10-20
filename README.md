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

## Latest list — 2026-10-20 04:22 UTC

New packages created between 2026-10-20 03:19 UTC and 2026-10-20 04:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T04-22-18-056131Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 03:31:53 | [tyto-php/router](https://www.nuget.org/packages/tyto-php%2Frouter) | v0.0.1 | Viktor Leite | Roteador minimalista de alta performance em PHP puro com suporte a atributos, m… |
| 2026-10-20 03:44:42 | [hallmark/hallmark](https://www.nuget.org/packages/hallmark%2Fhallmark) | v1.0.0 | Luciano Federico Pereira | A modern, fully-typed PSR-3 logging library for PHP 8.3+ — the handler/formatte… |
| 2026-10-20 03:56:43 | [tsumiki-labs/extension-builder](https://www.nuget.org/packages/tsumiki-labs%2Fextension-builder) | 1.0.1 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
