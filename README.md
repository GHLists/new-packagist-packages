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

## Latest list — 2026-11-19 19:19 UTC

New packages created between 2026-11-19 18:21 UTC and 2026-11-19 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T19-19-50-12171Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 18:25:17 | [brunasebold/module-sales-transfer](https://www.nuget.org/packages/brunasebold%2Fmodule-sales-transfer) | 1.0.0 | Bruna Sebold | Copy Magento orders, invoices, shipments and credit memos between installations… |
| 2026-11-19 18:53:54 | [letterncms/wilgendaal](https://www.nuget.org/packages/letterncms%2Fwilgendaal) | 0.2.0 |  | A Flemish city's website, in Dutch, built for accessibility: a home page that o… |
| 2026-11-19 18:54:40 | [letterncms/lindenhof](https://www.nuget.org/packages/letterncms%2Flindenhof) | 0.2.0 |  | A complete website for a Flemish hospital, in Dutch: care and care providers fr… |
| 2026-11-19 19:13:49 | [noid-oss/authz](https://www.nuget.org/packages/noid-oss%2Fauthz) | v0.1.0 |  | PHP SDK for the noid authz contract: token verification, claim hints, live Keto… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
