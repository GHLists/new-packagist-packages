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

## Latest list — 2026-10-16 13:20 UTC

New packages created between 2026-10-16 12:21 UTC and 2026-10-16 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T13-20-50-429586Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 12:31:24 | [winter/wn-octane-plugin](https://www.nuget.org/packages/winter%2Fwn-octane-plugin) | v1.0.0 | Derrick Austin | Serves Winter CMS from a persistent application server (FrankenPHP, Swoole or R… |
| 2026-10-16 12:32:54 | [rathauslotse/bayernportal-api](https://www.nuget.org/packages/rathauslotse%2Fbayernportal-api) | v1.0.0 | Michael Firlus | Laravel client for the BayernPortal REST API v3 (agencies, authorities, contact… |
| 2026-10-16 12:45:45 | [ske-io/laravel-bridge](https://www.nuget.org/packages/ske-io%2Flaravel-bridge) | v0.1.0 |  | Runs a Laravel application on SKE: HTTP, queue and console |
| 2026-10-16 12:50:25 | [dskripchenko/php-pdf-cryptopro](https://www.nuget.org/packages/dskripchenko%2Fphp-pdf-cryptopro) | v0.1.0 | Denis Skripchenko | CryptoPro CSP signer for dskripchenko/php-pdf: sign PDFs (PAdES, GOST R 34.10-2… |
| 2026-10-16 12:56:42 | [arzcode/filament-docs](https://www.nuget.org/packages/arzcode%2Ffilament-docs) | 1.0.0 | arzcode | An in-panel user manual for Filament: one markdown file per screen, laid out li… |
| 2026-10-16 13:08:01 | [mavisland/laravel-translator](https://www.nuget.org/packages/mavisland%2Flaravel-translator) | v1.0.0 | Tanju Yildiz | Synchronize missing Laravel PHP and JSON translation keys |
| 2026-10-16 13:11:30 | [gatovel/session](https://www.nuget.org/packages/gatovel%2Fsession) | v1.0.0 |  | Sistema modular e independente de gerenciamento de sessoes para aplicacoes PHP. |
| 2026-10-16 13:12:42 | [ahmedessawy/log-insight](https://www.nuget.org/packages/ahmedessawy%2Flog-insight) | v1.0.0 |  | Secure Laravel log viewer with tags, rich filtering, error grouping, metrics da… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
