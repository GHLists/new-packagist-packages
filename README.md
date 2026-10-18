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

## Latest list — 2026-10-18 17:19 UTC

New packages created between 2026-10-18 16:21 UTC and 2026-10-18 17:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T17-19-44-267873Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 16:22:47 | [phoenix1331/filament-headroom](https://www.nuget.org/packages/phoenix1331%2Ffilament-headroom) | v0.1.0 | Darren Williams | A Filament dashboard for AI token usage, cost and context limits, powered by He… |
| 2026-10-18 16:23:23 | [bytespulse-oe/pulse](https://www.nuget.org/packages/bytespulse-oe%2Fpulse) | v1.0.1 | BytespulseOE; PStoreGR | Lightweight Blade components for Laravel and Livewire apps. |
| 2026-10-18 16:35:20 | [devshaded/laravel-sanctum-starter-kit](https://www.nuget.org/packages/devshaded%2Flaravel-sanctum-starter-kit) | v1.0.0 |  | An API-only Laravel starter kit with Sanctum bearer tokens and Docker developme… |
| 2026-10-18 16:44:34 | [mrpc/xscraper](https://www.nuget.org/packages/mrpc%2Fxscraper) | v1.0.0 | mrpc | Read x.com posts and their replies from PHP without the official API. Request-f… |
| 2026-10-18 16:52:24 | [1994/reviews-core](https://www.nuget.org/packages/1994%2Freviews-core) | v1.0.0 | 1994 | The framework-free core shared by Reviews for Craft CMS and Statamic: averages… |
| 2026-10-18 16:53:12 | [abolaradev/navix](https://www.nuget.org/packages/abolaradev%2Fnavix) | v1.0.0 | abolaradev | A lightweight PHP package for building and managing hierarchical menu structure… |
| 2026-10-18 16:54:25 | [vezolabs/pimcore-sso-login-bundle](https://www.nuget.org/packages/vezolabs%2Fpimcore-sso-login-bundle) | v1.0.0 | VezoLabs | Production-Ready Single Sign-On (SSO) bundle for Pimcore 12 Studio with Microso… |
| 2026-10-18 17:04:09 | [vezolabs/pimcore-cloud-storage-bundle](https://www.nuget.org/packages/vezolabs%2Fpimcore-cloud-storage-bundle) | v1.0.0 | VezoLabs | Production-Ready Cloud Storage Manager for Pimcore 12 Studio supporting Amazon… |
| 2026-10-18 17:04:43 | [vezolabs/pimcore-login-tracker-bundle](https://www.nuget.org/packages/vezolabs%2Fpimcore-login-tracker-bundle) | v1.0.0 | VezoLabs | Production-Ready Login Tracker Plugin for Pimcore 12 Studio with comprehensive… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
