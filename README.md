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

## Latest list — 2026-10-26 20:22 UTC

New packages created between 2026-10-26 19:19 UTC and 2026-10-26 20:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T20-22-21-643826Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 19:49:31 | [wilycode/filters](https://www.nuget.org/packages/wilycode%2Ffilters) | v0.1.0 | Simon Piter | Ready-to-use filters built on the wilycode/filter contract. |
| 2026-10-26 20:02:23 | [corpus/php-cs-fixer-config](https://www.nuget.org/packages/corpus%2Fphp-cs-fixer-config) | v0.1.0 | Jesse G. Donat | Shared PHP-CS-Fixer configuration for Corpus projects. |
| 2026-10-26 20:11:52 | [himelali/pdf-generator](https://www.nuget.org/packages/himelali%2Fpdf-generator) | v2.0.0 | Md. Himel Ali | One fluent, driver-independent PDF API for Laravel on top of DomPDF, Snappy (wk… |
| 2026-10-26 20:18:07 | [webx-ui/module-configurator](https://www.nuget.org/packages/webx-ui%2Fmodule-configurator) | v0.87.0 | WebX UI | A product configurator for the WebX UI admin panel: steps of options and sizes… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
