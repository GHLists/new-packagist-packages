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

## Latest list — 2026-10-27 13:20 UTC

New packages created between 2026-10-27 12:21 UTC and 2026-10-27 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T13-20-23-972656Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 12:28:08 | [infaris/monitoring](https://www.nuget.org/packages/infaris%2Fmonitoring) | v1.0.0 |  | Guard by Infaris App Monitoring for PHP: requests per route, cache hit/miss, da… |
| 2026-10-27 12:50:32 | [st-all-one/blake3](https://www.nuget.org/packages/st-all-one%2Fblake3) | v0.1.0 | St-all-one | Pure PHP BLAKE3 implementation for PHP 8.4+ with hash, keyed hash, key derivati… |
| 2026-10-27 12:50:35 | [packstub/account-switcher](https://www.nuget.org/packages/packstub%2Faccount-switcher) | v1.0.0 | Ion Caliman; Packstub | Switch between accounts in a Laravel app without signing out: user impersonatio… |
| 2026-10-27 12:58:15 | [grupofixit/mpesa](https://www.nuget.org/packages/grupofixit%2Fmpesa) | v1.0.0 | Grupo FixIT Limitada | SDK oficial do Grupo FixIT para integracao segura com M-Pesa Mocambique (Vodaco… |
| 2026-10-27 13:01:25 | [michaelkaefer/admin-ui-bundle](https://www.nuget.org/packages/michaelkaefer%2Fadmin-ui-bundle) | 0.1.0 | Project Contributors | Autogenerate an admin web interface for entities |
| 2026-10-27 13:17:01 | [veasin/ff-cli](https://www.nuget.org/packages/veasin%2Fff-cli) | 0.0.1 |  | CLI capability layer for ff: input/output/routing via ext system. |
| 2026-10-27 13:17:08 | [wilycode/form-csrf](https://www.nuget.org/packages/wilycode%2Fform-csrf) | v0.1.0 | Simon Piter | Optional session-backed CSRF token field and validator for WilyCode Form. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
