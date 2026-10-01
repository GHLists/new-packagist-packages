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

## Latest list — 2026-10-01 12:22 UTC

New packages created between 2026-10-01 11:21 UTC and 2026-10-01 12:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T12-22-00-877289Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 11:21:22 | [mage2kishan/module-not-found-page](https://www.nuget.org/packages/mage2kishan%2Fmodule-not-found-page) | 1.0.13 | Kishan Savaliya | Custom 404 Not Found Page for Magento 2. Replaces the default CMS 404 page with… |
| 2026-10-01 11:25:13 | [mage2kishan/module-eu-withdrawal](https://www.nuget.org/packages/mage2kishan%2Fmodule-eu-withdrawal) | 1.1.3 | Kishan Savaliya | Panth EU Withdrawal Button - a clear, accessible digital withdrawal (cancellati… |
| 2026-10-01 11:29:42 | [mage2kishan/module-blog](https://www.nuget.org/packages/mage2kishan%2Fmodule-blog) | 1.3.2 | Kishan Savaliya | Panth_Blog - SEO-grade blog module for Magento 2 with first-class AEO/AIO suppo… |
| 2026-10-01 11:30:25 | [osumionline/plugin-updater](https://www.nuget.org/packages/osumionline%2Fplugin-updater) | 1.0.1 |  | Osumi Framework Composer plugin to run core migrations after framework updates. |
| 2026-10-01 11:31:11 | [yatmo/laravel](https://www.nuget.org/packages/yatmo%2Flaravel) | v1.0.0 | Yatmo | Real estate maps, points of interest and neighbourhood data for Laravel: Blade… |
| 2026-10-01 11:34:08 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.4 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |
| 2026-10-01 11:37:37 | [reza-satya/stylist](https://www.nuget.org/packages/reza-satya%2Fstylist) | 1.2.0 | Reza Satyawijaya | Laravel theming package. Forked for personal use |
| 2026-10-01 11:46:37 | [marrow/warden](https://www.nuget.org/packages/marrow%2Fwarden) | v1.0.0 | Aure Dulvresse | Account security scaffolding for Marrow — login, registration, password reset,… |
| 2026-10-01 11:47:52 | [synergizeflow/laravel-onboarding](https://www.nuget.org/packages/synergizeflow%2Flaravel-onboarding) | v1.0.10 |  | SynergizeFlow core client and onboarding package for Laravel |
| 2026-10-01 12:01:58 | [pollora/meilifacets](https://www.nuget.org/packages/pollora%2Fmeilifacets) | 0.1.0 | AmphiBee; Louis Boulanger | Faceted search, filtering and suggestions powered by Meilisearch for Pollora pr… |
| 2026-10-01 12:03:19 | [timmit/phpstan-framework-rules](https://www.nuget.org/packages/timmit%2Fphpstan-framework-rules) | 1.0.0 |  | PHPStan rules shared by aItem applications. |
| 2026-10-01 12:03:24 | [synergitech/laravel-docblocks](https://www.nuget.org/packages/synergitech%2Flaravel-docblocks) | v1.0.0 |  | Automatically generate PHPDoc types for various elements within Laravel project. |
| 2026-10-01 12:12:10 | [gingerminds/symfony-multisite](https://www.nuget.org/packages/gingerminds%2Fsymfony-multisite) | 0.1.0 | Gingerminds | Multisite and multi-language functionalities for Gingerminds Symfony projects |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
