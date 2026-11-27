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

## Latest list — 2026-11-27 20:19 UTC

New packages created between 2026-11-27 19:19 UTC and 2026-11-27 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T20-19-35-943385Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 19:28:21 | [mphpmaster/laravel-nova-sanadwa-whatsapp](https://www.nuget.org/packages/mphpmaster%2Flaravel-nova-sanadwa-whatsapp) | v1.0.0 | mPhpMaster | WhatsApp for Laravel and Nova: SanadWA / UltraMsg drivers, notification channel… |
| 2026-11-27 19:42:37 | [pfrenssen/drupal-sniffs](https://www.nuget.org/packages/pfrenssen%2Fdrupal-sniffs) | 1.0.0 |  | PHP_CodeSniffer sniffs that align Drupal projects with the conventions of Drupa… |
| 2026-11-27 19:45:20 | [lopescte/nfse-nacional-php](https://www.nuget.org/packages/lopescte%2Fnfse-nacional-php) | 1.0.0 | Marcelo Lopes | SDK PHP independente para integração com a NFS-e Nacional. |
| 2026-11-27 19:45:41 | [lopescte/bb-api-php](https://www.nuget.org/packages/lopescte%2Fbb-api-php) | 1.0.0 | Marcelo Lopes | Integração com a API de cobrança do Banco do Brasil |
| 2026-11-27 20:03:12 | [kariricode/eventloop](https://www.nuget.org/packages/kariricode%2Feventloop) | v4.2.0 | Walmir Silva | Event loop for PHP 8.4: timers, stream readiness, signals, deferred callbacks a… |
| 2026-11-27 20:12:03 | [lindesbs/contao-well-known-bundle](https://www.nuget.org/packages/lindesbs%2Fcontao-well-known-bundle) | 0.5 | Stefan Lindecke | Pflege und Auslieferung von /.well-known/-Endpunkten (security.txt, change-pass… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
