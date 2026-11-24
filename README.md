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

## Latest list — 2026-11-24 11:18 UTC

New packages created between 2026-11-24 10:21 UTC and 2026-11-24 11:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T11-18-56-775356Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 10:27:53 | [jeffersongoncalves/laravel-scanner-guard-caddy](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-scanner-guard-caddy) | 1.0.0 | Jefferson Gonçalves | Caddy denylist sink for laravel-scanner-guard: writes banned IPs as an imported… |
| 2026-11-24 10:28:09 | [jeffersongoncalves/laravel-scanner-guard-apache](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-scanner-guard-apache) | 1.0.0 | Jefferson Gonçalves | Apache denylist sink for laravel-scanner-guard: writes banned IPs as an include… |
| 2026-11-24 10:31:54 | [iperstudio/impersonate-plugin](https://www.nuget.org/packages/iperstudio%2Fimpersonate-plugin) | v1.0.1 | Iperstudio | Admin-only, request-scoped account impersonation for Kirby websites. |
| 2026-11-24 10:32:10 | [jeffersongoncalves/laravel-scanner-guard-frankenphp](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-scanner-guard-frankenphp) | 1.0.0 | Jefferson Gonçalves | FrankenPHP denylist sink for laravel-scanner-guard: writes banned IPs as an imp… |
| 2026-11-24 10:41:26 | [wrdev/minimax-php-client](https://www.nuget.org/packages/wrdev%2Fminimax-php-client) | v0.9.0 | Vlad G. | Framework-agnostic PHP client for the Minimax accounting API. |
| 2026-11-24 10:42:00 | [mygeocode/mygeocode](https://www.nuget.org/packages/mygeocode%2Fmygeocode) | v1.1.1 | My Geocode | Official PHP client for the My Geocode API: forward and reverse geocoding, addr… |
| 2026-11-24 10:43:48 | [vinworld/vinmail](https://www.nuget.org/packages/vinworld%2Fvinmail) | v0.1.0 | Vinworld | Official PHP and Laravel SDK for the VinMail transactional email API. |
| 2026-11-24 10:52:50 | [bunowave/recloud-laravel](https://www.nuget.org/packages/bunowave%2Frecloud-laravel) | v1.0.0 |  | ReCloud Turnstile bot protection for Laravel: Blade component, validation rule,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
