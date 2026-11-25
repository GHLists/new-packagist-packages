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

## Latest list — 2026-11-25 07:20 UTC

New packages created between 2026-11-25 06:19 UTC and 2026-11-25 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T07-20-28-850242Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 06:27:33 | [allswap/statamic-crypto-validator](https://www.nuget.org/packages/allswap%2Fstatamic-crypto-validator) | 1.0.0 | AllSwap Protocol | Multi-chain cryptocurrency address validation for Statamic CMS forms and Antler… |
| 2026-11-25 06:39:13 | [jovishin/tron-api](https://www.nuget.org/packages/jovishin%2Ftron-api) | v4.0.1 | Shamsudin Serderov | PHP 7.4 的 TRON SDK，源自 iexbase/tron-api 4.0.1，隨附 Web3 2.0.1。 |
| 2026-11-25 06:47:27 | [bezicto/pdfparser](https://www.nuget.org/packages/bezicto%2Fpdfparser) | v1.0.0 | Khairul Asyrani bin Sulaiman;… | Standalone PHP PDF parser library to extract text, metadata, and page details w… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
