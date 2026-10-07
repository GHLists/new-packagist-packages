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

## Latest list — 2026-10-07 07:20 UTC

New packages created between 2026-10-07 06:22 UTC and 2026-10-07 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T07-20-52-767359Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 06:28:50 | [mathsgod/light-oauth2](https://www.nuget.org/packages/mathsgod%2Flight-oauth2) | v1.0.0 |  | OAuth 2.0 integration for the Light framework |
| 2026-10-07 06:40:09 | [dolismartmaker/dolinews-client](https://www.nuget.org/packages/dolismartmaker%2Fdolinews-client) | v1.0.0 |  | Command line client to submit Dolibarr module announcements and project sheets… |
| 2026-10-07 06:48:41 | [mage2kishan/module-quickview](https://www.nuget.org/packages/mage2kishan%2Fmodule-quickview) | 1.0.22 | Kishan Savaliya | Smart Quick View & Compare module for Magento 2 with Hyva theme support. Featur… |
| 2026-10-07 06:52:42 | [mage2kishan/module-eu-withdrawal](https://www.nuget.org/packages/mage2kishan%2Fmodule-eu-withdrawal) | 1.1.12 | Kishan Savaliya | Panth EU Withdrawal Button - a clear, accessible digital withdrawal (cancellati… |
| 2026-10-07 06:56:23 | [mage2kishan/module-html-sitemap](https://www.nuget.org/packages/mage2kishan%2Fmodule-html-sitemap) | 1.0.19 |  | Theme-agnostic HTML sitemap page for Magento 2 (Hyva + Luma). Renders categorie… |
| 2026-10-07 07:00:01 | [mage2kishan/module-producttabs](https://www.nuget.org/packages/mage2kishan%2Fmodule-producttabs) | 1.1.8 | Kishan Savaliya | Product detail page tab customization for Magento 2. Supports horizontal/vertic… |
| 2026-10-07 07:03:42 | [mage2kishan/module-productgallery](https://www.nuget.org/packages/mage2kishan%2Fmodule-productgallery) | 1.0.16 | Kishan Savaliya | Custom product image gallery for Magento 2 product detail pages. Features confi… |
| 2026-10-07 07:08:01 | [mage2kishan/module-product-attachments](https://www.nuget.org/packages/mage2kishan%2Fmodule-product-attachments) | 1.1.9 |  | Product Attachments module for Magento 2 - attach files, links, and documents t… |
| 2026-10-07 07:18:07 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.18 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
