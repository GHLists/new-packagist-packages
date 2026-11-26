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

## Latest list — 2026-11-26 10:22 UTC

New packages created between 2026-11-26 09:22 UTC and 2026-11-26 10:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T10-22-26-476264Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 09:31:10 | [amc/openlibrary-php](https://www.nuget.org/packages/amc%2Fopenlibrary-php) | v1.0.0 |  | An object-oriented PHP client for the Open Library API with typed search result… |
| 2026-11-26 09:31:44 | [rllngr/kirby-doczer](https://www.nuget.org/packages/rllngr%2Fkirby-doczer) | 0.1 | Nicolas Rollinger | Read-only connector that exposes the public content of a Kirby site to a doczer… |
| 2026-11-26 09:37:39 | [darkwood/darkwood-bundle](https://www.nuget.org/packages/darkwood%2Fdarkwood-bundle) | v0.1.0 |  | Shared Darkwood Identity templates and design assets for Symfony applications. |
| 2026-11-26 09:42:49 | [klsoft/yii3-cms](https://www.nuget.org/packages/klsoft%2Fyii3-cms) | 1.0.0 |  | A content management system based on the Yii 3 framework and uses the Doctrine… |
| 2026-11-26 09:45:43 | [itmosoft/laravel-health](https://www.nuget.org/packages/itmosoft%2Flaravel-health) | v1.0.0 |  | Extensible health checks for Laravel applications. |
| 2026-11-26 09:47:58 | [gunner91/site-ai-assistant](https://www.nuget.org/packages/gunner91%2Fsite-ai-assistant) | v1.0.0 | Vladyslav Koshelyev | Drop-in AI chat assistant for any PHP website: answers from your Markdown knowl… |
| 2026-11-26 10:03:21 | [pixelperfectat/magento2-module-newsletter-signup-hyva-checkout](https://www.nuget.org/packages/pixelperfectat%2Fmagento2-module-newsletter-signup-hyva-checkout) | 0.1.0 |  | Newsletter sign-up for Hyvä Checkout: a sign-up line with a short benefit, show… |
| 2026-11-26 10:06:08 | [storedo/client](https://www.nuget.org/packages/storedo%2Fclient) | v0.1.0 | ma-kom agentur UG | STOREDO-Client für PHP: Bewertung, Ampel und Aufgaben je Domain in eigene Softw… |
| 2026-11-26 10:07:26 | [pactivasign/pactivasign-php](https://www.nuget.org/packages/pactivasign%2Fpactivasign-php) | v0.1.1 |  | Official PHP client for the PactivaSign e-signature API: envelopes, documents,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
