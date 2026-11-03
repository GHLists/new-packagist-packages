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

## Latest list — 2026-11-03 17:21 UTC

New packages created between 2026-11-03 16:18 UTC and 2026-11-03 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T17-21-45-088842Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 16:18:50 | [microweber-packages/microweber-translation](https://www.nuget.org/packages/microweber-packages%2Fmicroweber-translation) | v1.0.0 | Microweber | Standalone Laravel package for managing translations with database storage, imp… |
| 2026-11-03 16:19:01 | [microweber-packages/microweber-user](https://www.nuget.org/packages/microweber-packages%2Fmicroweber-user) | v1.0.0 | Microweber | Microweber CMS. |
| 2026-11-03 16:32:17 | [rajtik76/nette-tailwind-starter-kit](https://www.nuget.org/packages/rajtik76%2Fnette-tailwind-starter-kit) | v0.1.0 |  | Nette starter kit with Tailwind CSS: authentication, dashboard and settings |
| 2026-11-03 16:35:03 | [gilles-g/db-anonymizer](https://www.nuget.org/packages/gilles-g%2Fdb-anonymizer) | V0.1.0 | gilles-g | Anonymizes application database columns through table-scoped SQL UPDATEs, befor… |
| 2026-11-03 16:41:13 | [denosyscore/support](https://www.nuget.org/packages/denosyscore%2Fsupport) | v0.1.0 |  | Reusable support types for DenoSysCore packages |
| 2026-11-03 16:52:08 | [siensis/kpcrudy](https://www.nuget.org/packages/siensis%2Fkpcrudy) | v1.0.0 |  | Generador automàtic de CRUD per a CodeIgniter 4 |
| 2026-11-03 16:52:43 | [siensis/kpapy](https://www.nuget.org/packages/siensis%2Fkpapy) | v1.0.0 |  | Generador automàtic d'API REST per a CodeIgniter 4 · Automatic REST API generat… |
| 2026-11-03 16:52:59 | [mwx/nextcloud-app](https://www.nuget.org/packages/mwx%2Fnextcloud-app) | 0.1.1 | Martin Rüegg | An app's own update command: reads the store, clears the fetcher's cache, and l… |
| 2026-11-03 16:54:25 | [dokaudit/drupal-dokaudit](https://www.nuget.org/packages/dokaudit%2Fdrupal-dokaudit) | v1.2.2 | DokAudit | DokAudit für Drupal: PDFs automatisch barrierefrei machen (PDF/UA-1, WCAG 2.2,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
