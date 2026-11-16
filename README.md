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

## Latest list — 2026-11-16 20:20 UTC

New packages created between 2026-11-16 19:19 UTC and 2026-11-16 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T20-20-25-570456Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 19:22:00 | [starbug/imports-admin](https://www.nuget.org/packages/starbug%2Fimports-admin) | v0.9.0 | Ali Gangji | Admin screens for imports. |
| 2026-11-16 19:43:59 | [intragile/einvoicing-rules-en16931](https://www.nuget.org/packages/intragile%2Feinvoicing-rules-en16931) | v1.0.0 | IntrAgile Kft. | The official CEN EN 16931 validation rules (UBL and CII, artefacts 1.3.17 and 1… |
| 2026-11-16 19:43:59 | [intragile/einvoicing-rules-facturx](https://www.nuget.org/packages/intragile%2Feinvoicing-rules-facturx) | v1.0.0 | IntrAgile Kft. | The Factur-X 1.09.2 (ZUGFeRD) validation rules of the five profiles compiled to… |
| 2026-11-16 19:43:59 | [intragile/einvoicing-rules-xrechnung](https://www.nuget.org/packages/intragile%2Feinvoicing-rules-xrechnung) | v1.0.0 | IntrAgile Kft. | The KoSIT XRechnung 2.6.0 validation rules compiled to PHP arrays, the scenario… |
| 2026-11-16 19:43:59 | [intragile/laravel-einvoicing](https://www.nuget.org/packages/intragile%2Flaravel-einvoicing) | v1.0.0 | IntrAgile Kft. | Laravel bridge for intragile/php-einvoicing: send and receive EN 16931 invoices… |
| 2026-11-16 19:43:59 | [intragile/laravel-xrechnung](https://www.nuget.org/packages/intragile%2Flaravel-xrechnung) | v1.0.0 | IntrAgile Kft. | Laravel XRechnung: create, validate and send German XRechnung 3.0 e-invoices (U… |
| 2026-11-16 19:44:00 | [intragile/laravel-peppol](https://www.nuget.org/packages/intragile%2Flaravel-peppol) | v1.0.0 | IntrAgile Kft. | Laravel Peppol: send and receive Peppol BIS Billing 3.0 e-invoices through an a… |
| 2026-11-16 19:44:00 | [intragile/laravel-zugferd](https://www.nuget.org/packages/intragile%2Flaravel-zugferd) | v1.0.0 | IntrAgile Kft. | Laravel ZUGFeRD and Factur-X: write, read and validate hybrid PDF/A-3 e-invoice… |
| 2026-11-16 19:48:40 | [jeffersongoncalves/laravel-lgpd-dsar](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-lgpd-dsar) | 1.0.0 | Jefferson Gonçalves | LGPD data subject requests (art. 18) for Laravel: request tracking with legal d… |
| 2026-11-16 19:58:44 | [gabrieldav1108/laravel-server-analytics](https://www.nuget.org/packages/gabrieldav1108%2Flaravel-server-analytics) | v0.1.0 | Gabriel Davila | Server-side usage analytics for Laravel: records page views, logins and busines… |
| 2026-11-16 20:00:01 | [intragile/php-einvoicing](https://www.nuget.org/packages/intragile%2Fphp-einvoicing) | v1.0.0 | IntrAgile Kft. | Framework-agnostic EN 16931 e-invoicing core for PHP: invoice model, exact deci… |
| 2026-11-16 20:06:58 | [starbug/intl-admin](https://www.nuget.org/packages/starbug%2Fintl-admin) | v0.9.1 | Ali Gangji | Admin screens for countries and provinces. |
| 2026-11-16 20:08:43 | [jeffersongoncalves/laravel-lgpd-retention](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-lgpd-retention) | 1.0.0 | Jefferson Gonçalves | LGPD data retention for Laravel: anonymize personal data when its retention per… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
