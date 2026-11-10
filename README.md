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

## Latest list — 2026-11-10 13:21 UTC

New packages created between 2026-11-10 12:20 UTC and 2026-11-10 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T13-21-34-568733Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 12:26:10 | [gunsnprices/gunsnprices](https://www.nuget.org/packages/gunsnprices%2Fgunsnprices) | v0.1.0 | GunsNPrices | Parse firearm and ammunition product titles: brand, model, caliber, magazine ca… |
| 2026-11-10 12:26:30 | [ulsyairil/transactional-outbox](https://www.nuget.org/packages/ulsyairil%2Ftransactional-outbox) | v1.0.0 |  | Transactional Outbox pattern for PHP: store events in the same database transac… |
| 2026-11-10 12:32:21 | [bladeknigt89/yii2-dd](https://www.nuget.org/packages/bladeknigt89%2Fyii2-dd) | v1.0.0 | Bánfalvi Gábor | Laravel-compatible dd() and dump() for Yii2. |
| 2026-11-10 12:46:59 | [apxcde/laravel-telltale](https://www.nuget.org/packages/apxcde%2Flaravel-telltale) | v0.0.1 | Spatie; apxcde | Send Laravel errors, logs and traces to Telltale. A fork of spatie/laravel-flar… |
| 2026-11-10 12:47:10 | [jokerov/oauth2-yandex](https://www.nuget.org/packages/jokerov%2Foauth2-yandex) | v1.0.0 | Eugene Jokerov; Alexey Rakeev | Yandex OAuth2 Client Provider for The PHP League OAuth2-Client |
| 2026-11-10 12:47:17 | [gesflow/sender-laravel](https://www.nuget.org/packages/gesflow%2Fsender-laravel) | v1.0.0 | GESFLOW | SDK Laravel officiel de GESFLOW SENDER : SMS, WhatsApp, codes OTP et webhooks. |
| 2026-11-10 12:58:14 | [intragile/laravel-spreadsheet](https://www.nuget.org/packages/intragile%2Flaravel-spreadsheet) | v1.0.0 | IntrAgile Kft. | Streaming spreadsheet export and guided import for Laravel, built on intragile/… |
| 2026-11-10 13:02:57 | [intragile/php-spreadsheet](https://www.nuget.org/packages/intragile%2Fphp-spreadsheet) | v1.0.0 | IntrAgile Kft. | Streaming XLSX, ODS and CSV reader and writer for PHP with no Composer dependen… |
| 2026-11-10 13:07:02 | [peopleinside/flarum-restricted-visibility](https://www.nuget.org/packages/peopleinside%2Fflarum-restricted-visibility) | 1.0.1 |  | Limita la visibilità di singoli post o intere discussioni a gruppi o utenti sce… |
| 2026-11-10 13:11:36 | [3neti/form-handler-document](https://www.nuget.org/packages/3neti%2Fform-handler-document) | v1.0.0 |  | Private document upload handler for form-flow |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
