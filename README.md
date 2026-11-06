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

## Latest list — 2026-11-06 04:21 UTC

New packages created between 2026-11-06 03:20 UTC and 2026-11-06 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T04-21-15-238258Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 03:21:33 | [imbrett/laravel-api-query](https://www.nuget.org/packages/imbrett%2Flaravel-api-query) | v1.1.0 |  | Composable query scopes for searching, filtering, and sorting Eloquent models v… |
| 2026-11-06 03:21:33 | [imbrett/laravel-listener-attributes](https://www.nuget.org/packages/imbrett%2Flaravel-listener-attributes) | v1.1.0 |  | Attribute-driven event listener registration for Laravel. |
| 2026-11-06 03:28:52 | [volareinc/laravel-admin](https://www.nuget.org/packages/volareinc%2Flaravel-admin) | v1.9.0 | volareinc; zsong | laravel admin (fork of https://github.com/z-song/laravel-admin) |
| 2026-11-06 03:55:50 | [zubaer/laravel-zubquant](https://www.nuget.org/packages/zubaer%2Flaravel-zubquant) | v1.0.0 | Md. Zubaer Ahammed | Post-Quantum Cryptography for Laravel (Hybrid X-Wing ML-KEM-768 + X25519 Eloque… |
| 2026-11-06 03:55:50 | [zubaer/zubquant](https://www.nuget.org/packages/zubaer%2Fzubquant) | v1.0.0 | Md. Zubaer Ahammed | Zero-dependency Post-Quantum Cryptography SDK for PHP 8.1+ (NIST FIPS 203 ML-KE… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
