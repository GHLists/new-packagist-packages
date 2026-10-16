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

## Latest list — 2026-10-16 18:20 UTC

New packages created between 2026-10-16 17:22 UTC and 2026-10-16 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T18-20-39-41947Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 17:30:55 | [coss/laravel](https://www.nuget.org/packages/coss%2Flaravel) | v0.1.0 | Cal.com, Inc. | Send Laravel mail through coss.com. |
| 2026-10-16 17:39:23 | [cartpauj/show-login](https://www.nuget.org/packages/cartpauj%2Fshow-login) | v1.1.0 | cartpauj | WordPress front-end login popup triggered by a URL parameter (?sl=1). |
| 2026-10-16 17:45:06 | [vipertecpro/data-rights-desk](https://www.nuget.org/packages/vipertecpro%2Fdata-rights-desk) | v1.0.0 | vipertecpro | Notices, consent records, data rights requests and breach reports for India's D… |
| 2026-10-16 17:50:57 | [e9li/kirby-seo](https://www.nuget.org/packages/e9li%2Fkirby-seo) | v0.1.0 | Rafael Egli | Lightweight SEO tab, meta tags, Open Graph, robots.txt and sitemap.xml for Kirby |
| 2026-10-16 17:58:48 | [ernestdefoe/recipes](https://www.nuget.org/packages/ernestdefoe%2Frecipes) | 1.0.0 | Ernest Defoe | Structured recipes in posts: ingredients that scale with servings, one-click st… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
