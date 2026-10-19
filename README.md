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

## Latest list — 2026-10-19 16:19 UTC

New packages created between 2026-10-19 15:21 UTC and 2026-10-19 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T16-19-29-853128Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 15:36:02 | [gsu-cetloe/cetloelib-php](https://www.nuget.org/packages/gsu-cetloe%2Fcetloelib-php) | v1 |  | Shared PHP library for CETLOE applications: DI container, console, HTTP client,… |
| 2026-10-19 15:47:23 | [shire-studio/laravel-starter-kit-react](https://www.nuget.org/packages/shire-studio%2Flaravel-starter-kit-react) | v1.0.0 |  | An end-to-end type-safe Laravel 13 starter kit with auto-generated TypeScript t… |
| 2026-10-19 15:49:21 | [shire-studio/laravel-starter-kit-api](https://www.nuget.org/packages/shire-studio%2Flaravel-starter-kit-api) | v1.0.0 |  | A strict, fully tested Laravel 13 API starter kit with Sanctum token authentica… |
| 2026-10-19 15:52:13 | [shire-studio/laravel-starter-kit-livewire](https://www.nuget.org/packages/shire-studio%2Flaravel-starter-kit-livewire) | v1.0.0 |  | A strict, fully tested Laravel 13 starter kit with Livewire 4 and Flux componen… |
| 2026-10-19 15:55:46 | [shire-studio/laravel-starter-kit-blade](https://www.nuget.org/packages/shire-studio%2Flaravel-starter-kit-blade) | v1.0.0 |  | A strict, fully tested Laravel 13 starter kit with Blade views and Tailwind CSS |
| 2026-10-19 15:57:10 | [shire-studio/laravel-starter-kit-svelte](https://www.nuget.org/packages/shire-studio%2Flaravel-starter-kit-svelte) | v1.0.0 |  | An end-to-end type-safe Laravel 13 starter kit with auto-generated TypeScript t… |
| 2026-10-19 15:59:18 | [weft/ide-helper](https://www.nuget.org/packages/weft%2Fide-helper) | v0.1.0 |  | IDE stubs for the weft PHP extension: autocomplete and static analysis only, ne… |
| 2026-10-19 16:11:35 | [goletter/hyperf-adv-facebook](https://www.nuget.org/packages/goletter%2Fhyperf-adv-facebook) | v1.0.0 | goletter | Facebook Marketing API。由 goletter/hyperf-adv 拉取，并使用其工厂、Bundle、Token 轮询与异常。 |
| 2026-10-19 16:13:06 | [goletter/hyperf-adv-tiktok](https://www.nuget.org/packages/goletter%2Fhyperf-adv-tiktok) | v1.0.0 | goletter | TikTok Business API。由 goletter/hyperf-adv 拉取，并使用其工厂、Bundle、Token 轮询与异常。 |
| 2026-10-19 16:14:25 | [goletter/hyperf-adv-google](https://www.nuget.org/packages/goletter%2Fhyperf-adv-google) | v1.0.0 | goletter | Google Ads API。由 goletter/hyperf-adv 拉取，并使用其工厂、Bundle、Token 轮询与异常。 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
