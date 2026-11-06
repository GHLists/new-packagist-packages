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

## Latest list — 2026-11-06 08:21 UTC

New packages created between 2026-11-06 07:19 UTC and 2026-11-06 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T08-21-18-978658Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 07:27:53 | [adems/dapur-multiwebsite](https://www.nuget.org/packages/adems%2Fdapur-multiwebsite) | 1.0.0 | Ade M Saragih | Modul multi-website untuk Dapur AdeMS: satu inti Dapur melayani banyak website |
| 2026-11-06 07:34:51 | [tualo/pdfgear](https://www.nuget.org/packages/tualo%2Fpdfgear) | 1.0.1 |  | A PDF builder using HTML or DOCX templates. |
| 2026-11-06 07:37:15 | [intragile/php-text-extractor](https://www.nuget.org/packages/intragile%2Fphp-text-extractor) | v1.0.0 | IntrAgile Kft. | Extract plain text from PDF, DOCX, XLSX, PPTX, ODT, ODS, ODP, RTF, HTML, CSV an… |
| 2026-11-06 07:48:29 | [atannex/tenancy](https://www.nuget.org/packages/atannex%2Ftenancy) | v1.0.1 | Atangageih Leke Collins | Enterprise multi-tenancy for Laravel: tenant identification by domain, subdomai… |
| 2026-11-06 07:51:47 | [ichnois/ichnois](https://www.nuget.org/packages/ichnois%2Fichnois) | v1.0.0 | Ichnois | PHP SDK for Ichnois (https://ichnois-h2jw.onrender.com) |
| 2026-11-06 07:55:48 | [intragile/laravel-text-extractor](https://www.nuget.org/packages/intragile%2Flaravel-text-extractor) | v1.0.0 | IntrAgile Kft. | Laravel integration for intragile/php-text-extractor: extract text from PDF, Of… |
| 2026-11-06 07:58:00 | [xelqun/tables](https://www.nuget.org/packages/xelqun%2Ftables) | v0.1.0 | Jay-Are Ocero | PHP-defined, schema-driven tables for Laravel, Inertia and Vue. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
