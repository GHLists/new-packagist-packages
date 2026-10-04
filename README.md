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

## Latest list — 2026-10-04 19:19 UTC

New packages created between 2026-10-04 18:19 UTC and 2026-10-04 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T19-19-03-653479Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 18:24:27 | [ghostwriter/serializer](https://www.nuget.org/packages/ghostwriter%2Fserializer) | 0.1.0 | Nathanael Esayeas | Serialize and Deserialize PHP objects to JSON |
| 2026-10-04 18:25:52 | [cyberxgh/ghana-sms](https://www.nuget.org/packages/cyberxgh%2Fghana-sms) | v0.1.0 |  | Unified SMS interface for Ghanaian providers (Arkesel, mNotify, Hubtel) for PHP… |
| 2026-10-04 18:26:20 | [mylekha/record-api](https://www.nuget.org/packages/mylekha%2Frecord-api) | 1.0.2 |  | Config-driven generic CRUD API engine for Laravel: list/fetch/create/update/del… |
| 2026-10-04 18:32:17 | [bentools/url-pattern](https://www.nuget.org/packages/bentools%2Furl-pattern) | 1.0 | Beno!t POLASZEK | WHATWG URLPattern implementation for PHP |
| 2026-10-04 18:46:02 | [mage2kishan/module-product-slider](https://www.nuget.org/packages/mage2kishan%2Fmodule-product-slider) | 1.1.5 |  | Advanced Product Slider widget with extensive customization options for Magento… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
