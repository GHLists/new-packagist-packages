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

## Latest list — 2026-11-04 21:22 UTC

New packages created between 2026-11-04 20:21 UTC and 2026-11-04 21:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T21-22-14-183481Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 20:23:02 | [bode/module-metrics](https://www.nuget.org/packages/bode%2Fmodule-metrics) | v1.2.0 |  | OpenTelemetry metrics for Magento 2 with a hard low-cardinality contract: HTTP,… |
| 2026-11-04 20:23:02 | [bode/module-tracing](https://www.nuget.org/packages/bode%2Fmodule-tracing) | v1.2.0 |  | OpenTelemetry traces for Magento 2: HTTP, cron, CLI, indexers, cache, queues, o… |
| 2026-11-04 20:33:17 | [cgarciagl/ragnos](https://www.nuget.org/packages/cgarciagl%2Fragnos) | v1.0.2 | Carlos García Trujillo | Ragnos Framework - Declarative admin/CRUD framework for PHP built on CodeIgnite… |
| 2026-11-04 20:40:23 | [hosmelq/laravel-message-preview](https://www.nuget.org/packages/hosmelq%2Flaravel-message-preview) | v1.0.0 | Hosmel Quintana | Preview Laravel mailables and mail notifications in the browser. |
| 2026-11-04 20:42:59 | [bode/module-logs](https://www.nuget.org/packages/bode%2Fmodule-logs) | v1.2.0 |  | Structured JSON logs for Magento 2: every log record and exception as one OpenT… |
| 2026-11-04 20:48:11 | [beziworld/laravel-firmao](https://www.nuget.org/packages/beziworld%2Flaravel-firmao) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the Firmao CRM/ERP REST API: customers, products, invoices,… |
| 2026-11-04 20:54:21 | [beziworld/laravel-nfz](https://www.nuget.org/packages/beziworld%2Flaravel-nfz) | v1.0.1 | Kamil Ćwiertnia | Laravel integration with the Polish National Health Fund (NFZ): waiting times,… |
| 2026-11-04 21:08:01 | [beziworld/laravel-gus-bdl](https://www.nuget.org/packages/beziworld%2Flaravel-gus-bdl) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the GUS Local Data Bank (Bank Danych Lokalnych, BDL) API: su… |
| 2026-11-04 21:08:18 | [beziworld/laravel-dane-gov](https://www.nuget.org/packages/beziworld%2Flaravel-dane-gov) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the dane.gov.pl open data API: datasets, resources, institut… |
| 2026-11-04 21:09:44 | [spkm/duo-security](https://www.nuget.org/packages/spkm%2Fduo-security) | v1.0.1 | Simon Mitchell | Integrate with the Duo Security Admin and Auth APIs using SaloonPHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
