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

## Latest list — 2026-10-19 20:22 UTC

New packages created between 2026-10-19 19:20 UTC and 2026-10-19 20:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T20-22-12-054642Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 19:22:10 | [moderndesktop/oauth-forgejo](https://www.nuget.org/packages/moderndesktop%2Foauth-forgejo) | v1.0.1 | Joshua Strobl | Log in to Flarum with one or more Forgejo instances, using FoF OAuth. |
| 2026-10-19 19:26:49 | [gosuccess/wordpress-org-api](https://www.nuget.org/packages/gosuccess%2Fwordpress-org-api) | 0.1.0 | GoSuccess GmbH | A modern, strongly-typed, dependency-free PHP client for the public wordpress.o… |
| 2026-10-19 19:27:23 | [yii2-extensions/skill](https://www.nuget.org/packages/yii2-extensions%2Fskill) | 0.1.0 | Wilmer Arambula | Agent skills for Yii 22 applications, framework subsystems, and Yii 2.0 upgrade… |
| 2026-10-19 19:34:09 | [automattic/jetpack-knowledge](https://www.nuget.org/packages/automattic%2Fjetpack-knowledge) | v0.1.0 |  | Knowledge runtime polyfill. |
| 2026-10-19 19:37:18 | [seviaflow/api](https://www.nuget.org/packages/seviaflow%2Fapi) | v0.1.0-beta.1 |  | SeviaFlow headless REST and OpenAPI adapter. |
| 2026-10-19 19:37:21 | [seviaflow/ui](https://www.nuget.org/packages/seviaflow%2Fui) | v0.1.0-beta.1 |  | SeviaFlow operator UI adapter for Laravel and Livewire. |
| 2026-10-19 19:37:25 | [seviaflow/devtools](https://www.nuget.org/packages/seviaflow%2Fdevtools) | v0.1.0-beta.1 |  | SeviaFlow discovery, generation and diagnostics tooling. |
| 2026-10-19 19:43:31 | [fixstacks/module-zero-product-attachments](https://www.nuget.org/packages/fixstacks%2Fmodule-zero-product-attachments) | 1.3.0 | Roman Pasichnyk | Zero for Magento Open Source: files on product pages (manuals, data sheets, cer… |
| 2026-10-19 19:43:31 | [fixstacks/module-zero-unit-price](https://www.nuget.org/packages/fixstacks%2Fmodule-zero-unit-price) | 1.3.0 | Roman Pasichnyk | Zero for Magento Open Source: the price per kilogram, litre, metre or piece und… |
| 2026-10-19 20:06:05 | [laravel-ops/connector](https://www.nuget.org/packages/laravel-ops%2Fconnector) | v1.0.0 | Olusegun, OP Virtual Technolo… | Lightweight connector for Laravel applications to connect to Laravel Ops |
| 2026-10-19 20:09:13 | [ffmpeg-micro/ffmpeg-micro-php](https://www.nuget.org/packages/ffmpeg-micro%2Fffmpeg-micro-php) | v0.1.0 | FFmpeg Micro | Official PHP client for the FFmpeg Micro API: video transcoding, transcription… |
| 2026-10-19 20:11:59 | [fatlum/nativephp-barcode-reader](https://www.nuget.org/packages/fatlum%2Fnativephp-barcode-reader) | 0.0.1 | Fatlum Gjinofci | Free QR code and barcode reading from image files for NativePHP Mobile v4: Appl… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
