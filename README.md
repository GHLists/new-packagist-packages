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

## Latest list — 2026-10-04 07:19 UTC

New packages created between 2026-10-04 06:22 UTC and 2026-10-04 07:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T07-19-40-773208Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 06:37:49 | [mage2kishan/module-image-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-image-seo) | 1.0.13 | Kishan Savaliya | Panth Image SEO — template-based alt/title generation for Magento 2 product ima… |
| 2026-10-04 06:44:38 | [codewiser/multilingual](https://www.nuget.org/packages/codewiser%2Fmultilingual) | v1.0.0 | pm | Multilingual Model Attributes for Laravel |
| 2026-10-04 06:45:29 | [softcreatr/json-payload-contract](https://www.nuget.org/packages/softcreatr%2Fjson-payload-contract) | 1.0.0 | Sascha Greuel | Extract stable, typed data from evolving JSON payloads |
| 2026-10-04 06:56:14 | [themusicdev/analytics](https://www.nuget.org/packages/themusicdev%2Fanalytics) | v1.0.0 | TheMusicDev | CakePHP 5 plugin: tracking tags (Google Analytics 4, Umami) and injected script… |
| 2026-10-04 07:16:49 | [mage2kishan/module-quickview](https://www.nuget.org/packages/mage2kishan%2Fmodule-quickview) | 1.0.20 | Kishan Savaliya | Smart Quick View & Compare module for Magento 2 with Hyva theme support. Featur… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
