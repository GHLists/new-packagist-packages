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

## Latest list — 2026-11-09 19:19 UTC

New packages created between 2026-11-09 17:21 UTC and 2026-11-09 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T19-19-33-616419Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 17:28:31 | [infinitetoken/lumber](https://www.nuget.org/packages/infinitetoken%2Flumber) | v1.0.0 | Jay Deaton | PHP client for Lumber: end-to-end encrypted cloud logging, with a PSR-3 logger,… |
| 2026-11-09 17:29:28 | [trk/processwire-inertia](https://www.nuget.org/packages/trk%2Fprocesswire-inertia) | v0.1.1 | Iskender TOTOGLU | Standalone Inertia.js v3 server-side protocol adapter for ProcessWire with Defe… |
| 2026-11-09 17:35:03 | [ee-forge/craft-recurrence](https://www.nuget.org/packages/ee-forge%2Fcraft-recurrence) | 1.0.0 | EE Forge | Recurring dates for native Craft entries, with indexed occurrences, dated URLs,… |
| 2026-11-09 17:37:04 | [peopleinside/flarum-restricted-visibility](https://www.nuget.org/packages/peopleinside%2Fflarum-restricted-visibility) | 1.0.4 |  | Restrict visibility of individual posts or entire discussions to specific group… |
| 2026-11-09 17:42:00 | [semhoun/slim-session](https://www.nuget.org/packages/semhoun%2Fslim-session) | 1.0.0 |  | Server-backed sessions with atomic lifecycle guarantees |
| 2026-11-09 17:44:21 | [martincodes-de/php-ftp-deploy-kit](https://www.nuget.org/packages/martincodes-de%2Fphp-ftp-deploy-kit) | v0.3.0 |  | PHP FTP Deploy Kit: thin layer over dg/ftp-deployment for FTP-only hosting: pre… |
| 2026-11-09 17:46:54 | [hapipay/php-client](https://www.nuget.org/packages/hapipay%2Fphp-client) | v1.0.1 |  | Client PHP de l'API HapiPay : paiements mobile money, carte et PayPal, transfer… |
| 2026-11-09 18:26:58 | [juaniquillo/input-component-action](https://www.nuget.org/packages/juaniquillo%2Finput-component-action) | v0.1.0 | Juaniquillo | Form input component creation and management action for Crud Assistant |
| 2026-11-09 18:31:39 | [packstub/filament-coedit](https://www.nuget.org/packages/packstub%2Ffilament-coedit) | v1.0.0-beta.1 | Ion Caliman; Packstub | Edit Filament records together without locks: live presence down to the field s… |
| 2026-11-09 18:46:40 | [solophp/vite](https://www.nuget.org/packages/solophp%2Fvite) | v1.0.0 | Vitaliy Olos | Vite for PHP without a framework: the tags that load entries from the dev serve… |
| 2026-11-09 18:56:11 | [yacoubalhaidari/provider-payments-sa](https://www.nuget.org/packages/yacoubalhaidari%2Fprovider-payments-sa) | v1.0.0 | Yacoub Al-Haidari | Standalone Laravel payment integrations extracted from audited provider flows. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
