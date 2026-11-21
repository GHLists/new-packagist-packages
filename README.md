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

## Latest list — 2026-11-21 14:21 UTC

New packages created between 2026-11-21 13:18 UTC and 2026-11-21 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T14-21-32-135601Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 13:22:35 | [karrieremag/contao-ausbildungsbetrieb-um-die-ecke](https://www.nuget.org/packages/karrieremag%2Fcontao-ausbildungsbetrieb-um-die-ecke) | 1.0.0 | Karrieremag GmbH | Ausbildungsbetrieb um die Ecke: kostenloses Azubi-Siegel und Widget mit Karte (… |
| 2026-11-21 13:22:35 | [karrieremag/typo3-ausbildungsbetrieb-um-die-ecke](https://www.nuget.org/packages/karrieremag%2Ftypo3-ausbildungsbetrieb-um-die-ecke) | 1.0.0 | Karrieremag GmbH | Ausbildungsbetrieb um die Ecke: kostenloses Azubi-Siegel und Widget mit Karte (… |
| 2026-11-21 13:37:40 | [parasoled/getopt](https://www.nuget.org/packages/parasoled%2Fgetopt) | v1.0.0 |  | A POSIX command-line parser with typed values, validation and generated help. |
| 2026-11-21 13:46:06 | [glofora/gsend-transport](https://www.nuget.org/packages/glofora%2Fgsend-transport) | v1.0.0 | Glofora Solutions | gSend mail transport driver and client for Laravel and PHP |
| 2026-11-21 13:48:07 | [webservco/access-control](https://www.nuget.org/packages/webservco%2Faccess-control) | v0.0.1 | Radu Maier | A PHP component/library. Roles, feature flags and usage limits per user, with a… |
| 2026-11-21 13:48:32 | [nwnuyhs/flarum-user-manager](https://www.nuget.org/packages/nwnuyhs%2Fflarum-user-manager) | v1.1.0 | X Theme | A better user admin for Flarum 2: email-confirmation status, sorting and filter… |
| 2026-11-21 13:55:56 | [nguyenthuan2412/outbox-pattern](https://www.nuget.org/packages/nguyenthuan2412%2Foutbox-pattern) | v0.1.0 | nguyenthuan2412 | Framework-agnostic Transactional Outbox abstractions for PHP: contracts + relay… |
| 2026-11-21 13:59:46 | [gosuccess/iso3166-2](https://www.nuget.org/packages/gosuccess%2Fiso3166-2) | 0.1.0 | GoSuccess GmbH | Dependency-free ISO 3166-2 country subdivisions with English and German names f… |
| 2026-11-21 14:03:05 | [gosuccess/byteplant-api](https://www.nuget.org/packages/gosuccess%2Fbyteplant-api) | 0.1.0 | GoSuccess GmbH | A modern, strongly-typed, dependency-free PHP client for the real-time email ve… |
| 2026-11-21 14:18:58 | [empiricompany/maho-omnibus](https://www.nuget.org/packages/empiricompany%2Fmaho-omnibus) | 1.0.0 |  | EU Omnibus Directive (2019/2161) compliance for Maho: records the price history… |
| 2026-11-21 14:19:13 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.41.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
