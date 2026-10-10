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

## Latest list — 2026-10-10 21:19 UTC

New packages created between 2026-10-10 20:20 UTC and 2026-10-10 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T21-19-38-067718Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 20:20:52 | [danielm/laravel-simple-audit](https://www.nuget.org/packages/danielm%2Flaravel-simple-audit) | v0.1.0 | Daniel Morales | Scalable, queueable audit event logging for Laravel apps, with a fluent builder… |
| 2026-10-10 20:21:06 | [chuckbe/ponto-connect-laravel-sdk](https://www.nuget.org/packages/chuckbe%2Fponto-connect-laravel-sdk) | v1.0.0 | Karel Brijs | Laravel SDK for the Ponto Connect API v2 (Isabel Group / Ibanity) |
| 2026-10-10 20:21:22 | [singraworks/br-fields](https://www.nuget.org/packages/singraworks%2Fbr-fields) | v1.0.0 | Lucas Vasconcelos | Validate, format, and redact Brazilian CPF and CNPJ numbers. Pure PHP, no Compo… |
| 2026-10-10 20:27:18 | [roadrunner/centrifugo](https://www.nuget.org/packages/roadrunner%2Fcentrifugo) | 2.5.0 | Anton Titov; Pavel Buchnev; A… | Centrifugo bridge for RoadRunner: handle Centrifugo proxy events in PHP workers… |
| 2026-10-10 20:44:37 | [nitro/nitro](https://www.nuget.org/packages/nitro%2Fnitro) | v2.0.0 | Zeeshan Ali | A full-stack framework for Laravel. Write components in PHP and Blade; Nitro co… |
| 2026-10-10 20:55:24 | [singraworks/laravel-br-fields](https://www.nuget.org/packages/singraworks%2Flaravel-br-fields) | v1.0.0 | Lucas Vasconcelos | Laravel validation rules and Eloquent casts for Brazilian CPF and CNPJ numbers,… |
| 2026-10-10 20:56:08 | [astromool/astromool-php](https://www.nuget.org/packages/astromool%2Fastromool-php) | v1.0.0 | AstroMool | Official client for the AstroMool Vedic astrology API (Swiss Ephemeris charts,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
