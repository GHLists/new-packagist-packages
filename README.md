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

## Latest list — 2026-10-28 22:19 UTC

New packages created between 2026-10-28 21:20 UTC and 2026-10-28 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T22-19-00-31751Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 21:20:33 | [bahu90/mining-manager](https://www.nuget.org/packages/bahu90%2Fmining-manager) | v2.1.0 | Bahu90; Matt Falahe | Comprehensive mining management plugin for SeAT - Track mining activities, mana… |
| 2026-10-28 21:26:04 | [nexus-lab/nexus](https://www.nuget.org/packages/nexus-lab%2Fnexus) | v2.0.4 | Nexus Core Architecture Team | Nexus Shield v2 - Next.js-inspired, JSX-compiled, ultra-secure PHP micro-framew… |
| 2026-10-28 21:27:29 | [simp/price](https://www.nuget.org/packages/simp%2Fprice) | v1.0.0 | Chance Nyasulu | This is php package that works with numerical values as amount of entity |
| 2026-10-28 21:33:14 | [papercut/laravel](https://www.nuget.org/packages/papercut%2Flaravel) | v0.3.0 | One Learning Community | Blade components that compile to Papercut's PDF layout engine. |
| 2026-10-28 21:33:15 | [papercut/core](https://www.nuget.org/packages/papercut%2Fcore) | v0.3.0 | One Learning Community | Component-based, page-aware PDF layout engine for modern PHP. |
| 2026-10-28 21:33:28 | [papercut/docx](https://www.nuget.org/packages/papercut%2Fdocx) | v0.3.0 | One Learning Community | Word (.docx) export for Papercut documents. |
| 2026-10-28 21:38:02 | [warpsearch/warpsearch-for-woocommerce](https://www.nuget.org/packages/warpsearch%2Fwarpsearch-for-woocommerce) | 0.1.0 | WarpSearch by BigData Boutique | WarpSearch for WooCommerce: fast, relevant WooCommerce product search with as-y… |
| 2026-10-28 21:38:09 | [warpsearch/module-search](https://www.nuget.org/packages/warpsearch%2Fmodule-search) | 0.1.0 | WarpSearch by BigData Boutique | WarpSearch for Magento 2 / Adobe Commerce: instant, relevance-ranked product qu… |
| 2026-10-28 21:42:33 | [matthieuthuetdev/simple-ai](https://www.nuget.org/packages/matthieuthuetdev%2Fsimple-ai) | v1.0.0 |  | A simple PHP library to interact with OpenAI models. |
| 2026-10-28 22:11:35 | [softavis/turnstile-bundle](https://www.nuget.org/packages/softavis%2Fturnstile-bundle) | 1.0.0 |  | Symfony integration for softavis/turnstile |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
