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

## Latest list — 2026-10-09 22:21 UTC

New packages created between 2026-10-09 21:20 UTC and 2026-10-09 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T22-21-23-734562Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 21:26:11 | [camindo/module-pdf](https://www.nuget.org/packages/camindo%2Fmodule-pdf) | v1.0.0 |  | camindo CMS module: PDF documents from frontend templates (CMS:PDF_* commands)… |
| 2026-10-09 21:35:17 | [nhanaz/libregrsp](https://www.nuget.org/packages/nhanaz%2Flibregrsp) | v1.0.5 |  | Resource pack compiler and registrar for Axolotl-PM plugins |
| 2026-10-09 21:36:21 | [onetracepro/onetrace-bitrix](https://www.nuget.org/packages/onetracepro%2Fonetrace-bitrix) | v1.1.0 |  | 1C-Bitrix module for the OneTrace.pro customer data platform: server-side order… |
| 2026-10-09 21:40:20 | [angrychimp/php-dkim](https://www.nuget.org/packages/angrychimp%2Fphp-dkim) | 0.4.0 | Randall Kahler | Finally, a PHP5 class for not just signing, but _verifying_ DKIM signatures. |
| 2026-10-09 21:48:23 | [polaris/passkey](https://www.nuget.org/packages/polaris%2Fpasskey) | v0.8.0 | 2am.tech | Passkeys for Polaris for PHP: WebAuthn registration and discoverable sign-in wi… |
| 2026-10-09 21:48:23 | [polaris/social](https://www.nuget.org/packages/polaris%2Fsocial) | v0.8.0 | 2am.tech | Social sign-in for Polaris for PHP: OAuth 2.0 and OpenID Connect providers (Goo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
