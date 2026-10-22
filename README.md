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

## Latest list — 2026-10-22 19:20 UTC

New packages created between 2026-10-22 18:20 UTC and 2026-10-22 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T19-20-20-636478Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 18:23:34 | [pekral/test-redundancy](https://www.nuget.org/packages/pekral%2Ftest-redundancy) | 0.1 | Petr Král | Finds PHPUnit and Pest tests whose covered lines other tests already cover, and… |
| 2026-10-22 18:46:09 | [adonyarik/consistent-api](https://www.nuget.org/packages/adonyarik%2Fconsistent-api) | v1.0.0 | Yaroslav Tyrchenko | Laravel toolkit for lean, consistent REST APIs: a module generator, modular rou… |
| 2026-10-22 18:50:50 | [opensolr/typo3-opensolr-search](https://www.nuget.org/packages/opensolr%2Ftypo3-opensolr-search) | v1.0.0 | Opensolr | Opensolr Search for TYPO3: hybrid AI search (keyword + vector), faceted navigat… |
| 2026-10-22 19:00:38 | [sugarcommerce/cli](https://www.nuget.org/packages/sugarcommerce%2Fcli) | 1.0.0 | David Sherlock | Command-line plumbing for PHP apps: argument parsing with typed reads, aligned… |
| 2026-10-22 19:00:54 | [novo-connect/somali-phone](https://www.nuget.org/packages/novo-connect%2Fsomali-phone) | v1.0.0 | Zakaria Ibrahim; Novo Connect | Validate, normalize and identify Somali mobile numbers: operator, virtual netwo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
