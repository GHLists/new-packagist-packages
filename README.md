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

## Latest list — 2026-10-01 09:22 UTC

New packages created between 2026-10-01 08:19 UTC and 2026-10-01 09:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T09-22-56-922305Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 08:32:01 | [crsl-admin/laravel-nuxt-ui-starter-kit](https://www.nuget.org/packages/crsl-admin%2Flaravel-nuxt-ui-starter-kit) | 0.0.1 |  | The NuxtUI application starter kit for CRSL team. |
| 2026-10-01 09:01:03 | [mage2kishan/module-eu-withdrawal](https://www.nuget.org/packages/mage2kishan%2Fmodule-eu-withdrawal) | 1.1.2 | Kishan Savaliya | Panth EU Withdrawal Button - a clear, accessible digital withdrawal (cancellati… |
| 2026-10-01 09:04:20 | [mage2kishan/module-faq](https://www.nuget.org/packages/mage2kishan%2Fmodule-faq) | 1.3.2 | Kishan Savaliya | Advanced FAQ Module with multi-level assignment capabilities |
| 2026-10-01 09:07:24 | [mage2kishan/module-testimonials](https://www.nuget.org/packages/mage2kishan%2Fmodule-testimonials) | 1.2.2 |  | Advanced Testimonials module with slider, individual pages, categories, SEO, an… |
| 2026-10-01 09:11:29 | [mage2kishan/module-blog](https://www.nuget.org/packages/mage2kishan%2Fmodule-blog) | 1.3.1 | Kishan Savaliya | Panth_Blog - SEO-grade blog module for Magento 2 with first-class AEO/AIO suppo… |
| 2026-10-01 09:17:05 | [mage2kishan/module-html-sitemap](https://www.nuget.org/packages/mage2kishan%2Fmodule-html-sitemap) | 1.0.15 |  | Theme-agnostic HTML sitemap page for Magento 2 (Hyva + Luma). Renders categorie… |
| 2026-10-01 09:21:08 | [mage2kishan/module-not-found-page](https://www.nuget.org/packages/mage2kishan%2Fmodule-not-found-page) | 1.0.12 | Kishan Savaliya | Custom 404 Not Found Page for Magento 2. Replaces the default CMS 404 page with… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
