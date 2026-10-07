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

## Latest list — 2026-10-07 14:19 UTC

New packages created between 2026-10-07 13:20 UTC and 2026-10-07 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T14-19-21-332539Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 13:38:55 | [chirpstack/chirpstack-api](https://www.nuget.org/packages/chirpstack%2Fchirpstack-api) | 4.19.2 |  | Chirpstack PHP API |
| 2026-10-07 13:40:58 | [cloud-castle/ocr](https://www.nuget.org/packages/cloud-castle%2Focr) | v0.1.0 | CloudCastle | Production-ready PHP 8.1+ package (CloudCastle OCR). |
| 2026-10-07 13:46:50 | [sympress/base-mu-plugin](https://www.nuget.org/packages/sympress%2Fbase-mu-plugin) | v1.0.0 |  | Shared WordPress must-use bootstrap and development utilities for SymPress webs… |
| 2026-10-07 13:56:04 | [achedon12/golem](https://www.nuget.org/packages/achedon12%2Fgolem) | v0 |  |  |
| 2026-10-07 13:57:32 | [ai-soft/laravel-scheduled-sequence](https://www.nuget.org/packages/ai-soft%2Flaravel-scheduled-sequence) | v0.1.0 | Goran Savkic | Persistent, state-aware scheduling sequences with irregular timing for Laravel… |
| 2026-10-07 13:57:39 | [andydefer/laravel-locationiq](https://www.nuget.org/packages/andydefer%2Flaravel-locationiq) | v0.1.0 | andydefer | Laravel SDK for integrating LocationIQ and Nominatim geospatial services (balan… |
| 2026-10-07 14:04:30 | [ontec/discrete-window-throttling](https://www.nuget.org/packages/ontec%2Fdiscrete-window-throttling) | v0.1.0 | EligiusSantori | Strict rate limiter with reasonable speed and memory usage for Redis 7+. |
| 2026-10-07 14:06:53 | [omega-mvc/gettext](https://www.nuget.org/packages/omega-mvc%2Fgettext) | 1.0.0 | Adriano Giovannini | GNU gettext-based localization and translation support for the Omega ecosystem,… |
| 2026-10-07 14:12:28 | [jeffersongoncalves/laravel-saml2](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-saml2) | v1.0.0 | Jefferson Gonçalves | Multi-tenant SAML2 Service Provider for Laravel. Connect any number of Identity… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
