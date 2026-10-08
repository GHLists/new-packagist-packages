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

## Latest list — 2026-10-08 23:19 UTC

New packages created between 2026-10-08 22:20 UTC and 2026-10-08 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T23-19-46-009607Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 22:56:20 | [jeffersongoncalves/laravel-cloudflare-web-analytics](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-cloudflare-web-analytics) | 1.0.0 | Jefferson Gonçalves | Cloudflare Web Analytics for Laravel: inject the tracking script in your Blade… |
| 2026-10-08 22:56:57 | [jeffersongoncalves/laravel-simple-analytics](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-simple-analytics) | 1.0.0 | Jefferson Gonçalves | Simple Analytics for Laravel: inject the tracking script in your Blade layouts,… |
| 2026-10-08 22:57:27 | [jeffersongoncalves/laravel-goatcounter](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-goatcounter) | 1.0.0 | Jefferson Gonçalves | GoatCounter for Laravel: inject the tracking script in your Blade layouts, with… |
| 2026-10-08 22:57:35 | [jeffersongoncalves/laravel-pirsch](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-pirsch) | 1.0.0 | Jefferson Gonçalves | Pirsch for Laravel: inject the tracking script in your Blade layouts, with the… |
| 2026-10-08 22:58:04 | [jeffersongoncalves/laravel-crisp](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-crisp) | 1.0.0 | Jefferson Gonçalves | Crisp for Laravel: render the live chat widget in your Blade layouts, with the… |
| 2026-10-08 22:58:42 | [jeffersongoncalves/laravel-tawk-to](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-tawk-to) | 1.0.0 | Jefferson Gonçalves | Tawk.to for Laravel: render the live chat widget in your Blade layouts, with th… |
| 2026-10-08 22:59:23 | [jeffersongoncalves/filament-cloudflare-web-analytics](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-cloudflare-web-analytics) | 3.0.0 | Jefferson Gonçalves | Filament plugin for Cloudflare Web Analytics: injects the tracking script into… |
| 2026-10-08 23:02:21 | [jeffersongoncalves/filament-simple-analytics](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-simple-analytics) | 3.0.0 | Jefferson Gonçalves | Filament plugin for Simple Analytics: injects the tracking script into your pan… |
| 2026-10-08 23:02:46 | [jeffersongoncalves/filament-pirsch](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-pirsch) | 3.0.0 | Jefferson Gonçalves | Filament plugin for Pirsch: injects the tracking script into your panels and ad… |
| 2026-10-08 23:03:18 | [jeffersongoncalves/filament-goatcounter](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-goatcounter) | 3.0.0 | Jefferson Gonçalves | Filament plugin for GoatCounter: injects the tracking script into your panels a… |
| 2026-10-08 23:03:59 | [jeffersongoncalves/filament-crisp](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-crisp) | 3.0.0 | Jefferson Gonçalves | Filament plugin for Crisp: renders the live chat widget in your panels and adds… |
| 2026-10-08 23:05:12 | [jeffersongoncalves/filament-tawk-to](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-tawk-to) | 3.0.0 | Jefferson Gonçalves | Filament plugin for Tawk.to: renders the live chat widget in your panels and ad… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
