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

## Latest list — 2026-10-06 10:22 UTC

New packages created between 2026-10-06 09:21 UTC and 2026-10-06 10:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T10-22-58-143023Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 09:33:36 | [stanislas-poisson/kmark](https://www.nuget.org/packages/stanislas-poisson%2Fkmark) | 1.0.0 | Stanislas Poisson | A Markdown-like text to HTML converter that lets you set an id and CSS classes… |
| 2026-10-06 09:42:16 | [maxcode/module-sitemap-exclude-cms](https://www.nuget.org/packages/maxcode%2Fmodule-sitemap-exclude-cms) | v1.0.2 |  | EN: Adds an “Exclude from XML sitemap” checkbox to the SEO tab of each Magento… |
| 2026-10-06 09:44:13 | [anis-ly/partners](https://www.nuget.org/packages/anis-ly%2Fpartners) | v1.0.0 | Aniscom for Technical Service… | The PHP SDK for the Anis Partner API — signed requests, verified responses, typ… |
| 2026-10-06 09:51:12 | [mage2kishan/module-order-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-order-attachments) | 1.1.8 |  | Allows customers to attach files to order items |
| 2026-10-06 09:57:37 | [vivutio/touring-module](https://www.nuget.org/packages/vivutio%2Ftouring-module) | v0.1.0 | Ezekiel Mjema | Tours for vivutio: itineraries day by day through the destinations, where each… |
| 2026-10-06 10:00:05 | [lintkit/mago-config](https://www.nuget.org/packages/lintkit%2Fmago-config) | 1.0.0 | Mike Street | Liquid Light base configuration for Mago |
| 2026-10-06 10:01:54 | [pphp/pphp](https://www.nuget.org/packages/pphp%2Fpphp) | v1.0.1 | Junior Nyemeck | Un préprocesseur PHP avec typage statique obligatoire, exécuté à la volée. |
| 2026-10-06 10:12:17 | [volkmann-design-code/kirby-upload-images](https://www.nuget.org/packages/volkmann-design-code%2Fkirby-upload-images) | 0.1.0 | Enzo Volkmann | Uploaded images made web-ready: HEIC converted, big photos shrunk without runni… |
| 2026-10-06 10:17:28 | [crushjs/mini-pdf](https://www.nuget.org/packages/crushjs%2Fmini-pdf) | v1.0.0 | Crushjs | A lightweight PDF generator for Laravel with built-in Khmer (Unicode) support |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
