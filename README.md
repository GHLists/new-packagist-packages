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

## Latest list — 2026-11-18 20:19 UTC

New packages created between 2026-11-18 19:22 UTC and 2026-11-18 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T20-19-34-51543Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 19:27:23 | [absolutoffice/geo-locator](https://www.nuget.org/packages/absolutoffice%2Fgeo-locator) | v1.0.1 | Absolut Office | PHP IP geolocation library with MaxMind lookup, authenticated visitor cache, tr… |
| 2026-11-18 19:28:12 | [beromir/neos-backend-comments](https://www.nuget.org/packages/beromir%2Fneos-backend-comments) | v1.0.0 | Henrik Reißig | For Neos Studio: Figma-like comments on content nodes in the backend, as notes… |
| 2026-11-18 19:58:53 | [hryvinskyi/magento2-catalog-sorting](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting) | 1.0.0 | Volodymyr Hryvinskyi | Sorting of storefront catalog listings in the search engine: leading sort rules… |
| 2026-11-18 19:58:53 | [hryvinskyi/magento2-catalog-sorting-bestsellers](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-bestsellers) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sort option Best Sellers: the products with the most units ordered in a… |
| 2026-11-18 19:58:53 | [hryvinskyi/magento2-catalog-sorting-metrics](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-metrics) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sorting capability: per-store product metrics that sort methods define… |
| 2026-11-18 19:58:53 | [hryvinskyi/magento2-catalog-sorting-most-viewed](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-most-viewed) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sort option Most Viewed: the products whose page was viewed most in a r… |
| 2026-11-18 19:58:53 | [hryvinskyi/magento2-catalog-sorting-newest](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-newest) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sort option New: the most recently created products first, ordered by a… |
| 2026-11-18 19:58:54 | [hryvinskyi/magento2-catalog-sorting-no-image](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-no-image) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sorting rule: products with a listing image before products without one… |
| 2026-11-18 19:58:54 | [hryvinskyi/magento2-catalog-sorting-options](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-options) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sort options per store: hide, rename and reorder the options of the sto… |
| 2026-11-18 19:58:54 | [hryvinskyi/magento2-catalog-sorting-out-of-stock](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-out-of-stock) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sorting rule: in-stock products before out-of-stock ones in category li… |
| 2026-11-18 19:58:54 | [hryvinskyi/magento2-catalog-sorting-reviews-count](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-reviews-count) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sort option Reviews Count: the products with the most customer reviews… |
| 2026-11-18 19:58:54 | [hryvinskyi/magento2-catalog-sorting-saving](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-saving) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sort option Biggest Saving: products with the largest discount from the… |
| 2026-11-18 19:58:54 | [hryvinskyi/magento2-catalog-sorting-top-rated](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-top-rated) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sort option Top Rated: the products with the highest customer rating fi… |
| 2026-11-18 19:58:54 | [hryvinskyi/magento2-catalog-sorting-wishlist](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-catalog-sorting-wishlist) | 1.0.0 | Volodymyr Hryvinskyi | Catalog sort option Now in Wishlists: the products that sit in the most wishlis… |
| 2026-11-18 20:04:46 | [webservco/discogs-authentication](https://www.nuget.org/packages/webservco%2Fdiscogs-authentication) | v0.0.1 | Radu Maier | A PHP component/library. Logs a user in with Discogs (OAuth 1.0a: request token… |
| 2026-11-18 20:12:20 | [osaris-uk/discogs](https://www.nuget.org/packages/osaris-uk%2Fdiscogs) | v1.0.0 | Osaris | Laravel client for the Discogs API (v2). Authenticated requests only. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
