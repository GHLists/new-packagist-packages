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

## Latest list — 2026-11-02 10:20 UTC

New packages created between 2026-11-02 09:22 UTC and 2026-11-02 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T10-20-19-695889Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 09:27:35 | [poli-page/laravel](https://www.nuget.org/packages/poli-page%2Flaravel) | v0.13.0 | Poli Page | Laravel package for the Poli Page PDF rendering API |
| 2026-11-02 09:27:38 | [poli-page/symfony](https://www.nuget.org/packages/poli-page%2Fsymfony) | v0.13.0 | Poli Page | Symfony bundle for the Poli Page PDF rendering API |
| 2026-11-02 09:36:46 | [actualizer/sulu-passkey](https://www.nuget.org/packages/actualizer%2Fsulu-passkey) | v0.1.0 |  | Passkey (WebAuthn) login for the Sulu admin, with management in the user profil… |
| 2026-11-02 09:45:50 | [neomasterr/php-cron-scheduler](https://www.nuget.org/packages/neomasterr%2Fphp-cron-scheduler) | v4.1 | Giuseppe Occhipinti; Carsten… | PHP Cron Job Scheduler |
| 2026-11-02 09:48:05 | [tomylana93/jcf](https://www.nuget.org/packages/tomylana93%2Fjcf) | v1.0.0 |  | A modern, modular starterkit for building simple, purposeful applications. |
| 2026-11-02 09:57:14 | [mage2kishan/module-error-monitor](https://www.nuget.org/packages/mage2kishan%2Fmodule-error-monitor) | 1.8.1 | Kishan Savaliya | Panth Error Monitor - smart, secure error management for Magento 2. Captures PH… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
