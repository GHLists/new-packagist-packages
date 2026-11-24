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

## Latest list — 2026-11-24 13:20 UTC

New packages created between 2026-11-24 12:21 UTC and 2026-11-24 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T13-20-37-499407Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 12:27:13 | [agent001/sylius-ai-assistant-plugin](https://www.nuget.org/packages/agent001%2Fsylius-ai-assistant-plugin) | 1.0.0 | Agent001 Team | Agent001 AI Customer Support Assistant for Sylius eCommerce. |
| 2026-11-24 12:32:51 | [globalxtreme/php-asa](https://www.nuget.org/packages/globalxtreme%2Fphp-asa) | 1.0.0 | Yuswa | GlobalXtreme ASA Automation Package for PHP Language |
| 2026-11-24 12:51:45 | [jacobdelcroix/ffbb-api-sdk](https://www.nuget.org/packages/jacobdelcroix%2Fffbb-api-sdk) | v0.1.1 | Jacob Delcroix | SDK PHP (Saloon) non officiel pour les données FFBB : clubs, compétitions, poul… |
| 2026-11-24 13:03:11 | [ifynx/gulf-e-invoicing](https://www.nuget.org/packages/ifynx%2Fgulf-e-invoicing) | v0.1.0 | iFynx Integrated Solutions P.… | Saudi ZATCA Phase 2 (Fatoora) signing, XAdES and QR plus UAE Peppol PINT AE e-i… |
| 2026-11-24 13:08:14 | [survos/omc](https://www.nuget.org/packages/survos%2Fomc) | 2.45.88 |  | MovieLabs OMC 2.8 DTOs, schema validation and production catalog JSON. |
| 2026-11-24 13:09:52 | [lessormq/laravel](https://www.nuget.org/packages/lessormq%2Flaravel) | v0.4.9 |  | Laravel queue driver for LessorMQ: the queue decides retries, backoff and dead-… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
