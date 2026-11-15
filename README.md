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

## Latest list — 2026-11-15 15:19 UTC

New packages created between 2026-11-15 14:19 UTC and 2026-11-15 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T15-19-14-033888Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 14:27:01 | [abdulwahhabkhan/device-auth](https://www.nuget.org/packages/abdulwahhabkhan%2Fdevice-auth) | v0.0.1 |  | Device-key (WebAuthn) authentication for Laravel + Inertia React: only approved… |
| 2026-11-15 14:29:50 | [otaqq/search-in-box](https://www.nuget.org/packages/otaqq%2Fsearch-in-box) | v0.1.0 | otaqq | Full-text search inside your own database, no search server: a small index tabl… |
| 2026-11-15 14:49:46 | [serendipity_hq/component-fattura-elettronica](https://www.nuget.org/packages/serendipity_hq%2Fcomponent-fattura-elettronica) | 0.1.0 | Adamo Aerendir Crespi | Manage electronic invoices in Italy. |
| 2026-11-15 14:52:59 | [iltuostudiodigitale/coworking-connector](https://www.nuget.org/packages/iltuostudiodigitale%2Fcoworking-connector) | v1.0.0 |  | Il contratto del coworking di Il tuo studio digitale in forma di codice: DTO, c… |
| 2026-11-15 15:03:07 | [thebeardedbear/urssaf-attestations-verification-code-securite](https://www.nuget.org/packages/thebeardedbear%2Furssaf-attestations-verification-code-securite) | v0.1.0 | TheBeardedBear | Client and domain model for the URSSAF "API Attestations Vérification Code Sécu… |
| 2026-11-15 15:15:29 | [filafly/filament-bootstrap-icons](https://www.nuget.org/packages/filafly%2Ffilament-bootstrap-icons) | v1.0.0 | Nolan Nordlund | Bootstrap Icons pack for Filament Icons: replaces every Filament UI icon with B… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
