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

## Latest list — 2026-10-30 11:21 UTC

New packages created between 2026-10-30 10:20 UTC and 2026-10-30 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T11-21-56-682185Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 10:26:17 | [konradmichalik/typo3-letterbox](https://www.nuget.org/packages/konradmichalik%2Ftypo3-letterbox) | 0.1.0 | Konrad Michalik; Armin Vieweg | Letterbox - Catches TYPO3 mails in an mbox file and shows them in the backend,… |
| 2026-10-30 10:27:31 | [realzone22/nativeblade](https://www.nuget.org/packages/realzone22%2Fnativeblade) | 0.1.0 | RealZone22 | Native-feeling Blade components for Laravel with Material Design 3 and iOS them… |
| 2026-10-30 10:36:39 | [quioteframework/dev-overlay](https://www.nuget.org/packages/quioteframework%2Fdev-overlay) | v1.0.0 | Quiote Contributors | In-browser developer overlay for Quiote: a floating badge injected into HTML pa… |
| 2026-10-30 10:39:03 | [glue-agency/laravel-glue-backoffice](https://www.nuget.org/packages/glue-agency%2Flaravel-glue-backoffice) | 1.0.0 |  | Reports a Laravel app to the Glue Dashboard after each deploy |
| 2026-10-30 10:45:27 | [dud/contao-wartung-client](https://www.nuget.org/packages/dud%2Fcontao-wartung-client) | 1.1.0 | Gunnar Haeuschkel | Client-Bundle für den Wartomat (Contao-Wartungssystem von Drum und Dran) |
| 2026-10-30 10:57:24 | [enabel/permission-bundle](https://www.nuget.org/packages/enabel%2Fpermission-bundle) | v1.0.0 | Damien LAGAE | Permission enums for Symfony: roles, relations and rules declared on each case,… |
| 2026-10-30 11:02:31 | [ismailnakkar/laravel-money](https://www.nuget.org/packages/ismailnakkar%2Flaravel-money) | v0.1.0 | Ismail Nakkar | Money as an exact decimal string in Laravel: check it, cut it, print it. No flo… |
| 2026-10-30 11:06:51 | [crystoline/xpsr-lock](https://www.nuget.org/packages/crystoline%2Fxpsr-lock) | v0.5.0 | Adekunle | Locks for XPSR applications on Symfony Lock: files, Redis, Redlock across sever… |
| 2026-10-30 11:06:51 | [crystoline/xpsr-notifications](https://www.nuget.org/packages/crystoline%2Fxpsr-notifications) | v0.5.0 | Adekunle | Notifications for XPSR applications: email, SMS through Symfony Notifier's prov… |
| 2026-10-30 11:08:46 | [digiwerft/contao-er24-custom-sections](https://www.nuget.org/packages/digiwerft%2Fcontao-er24-custom-sections) | 1.0.0 | DIGIWERFT GmbH | Eigene Abschnitte an frei wählbarer Stelle in eRecht24-Rechtstexte einfügen, oh… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
