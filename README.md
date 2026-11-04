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

## Latest list — 2026-11-04 19:20 UTC

New packages created between 2026-11-04 18:21 UTC and 2026-11-04 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T19-20-03-241497Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 18:26:12 | [beziworld/laravel-edoreczenia](https://www.nuget.org/packages/beziworld%2Flaravel-edoreczenia) | v1.0.0 | Kamil Ćwiertnia | Laravel client for Polish e-Doręczenia: UA API mailbox (send, receive, attachme… |
| 2026-11-04 18:31:16 | [rmb32/barn-paths](https://www.nuget.org/packages/rmb32%2Fbarn-paths) | v2.0.0 | Roger Barnfather | Finds a barn (the nearest .barn/barn.json) and says where each tool's files liv… |
| 2026-11-04 18:36:59 | [beziworld/laravel-teryt](https://www.nuget.org/packages/beziworld%2Flaravel-teryt) | v1.0.0 | Kamil Ćwiertnia | Laravel integration of the Polish TERYT register (GUS): TERC/SIMC/ULIC import i… |
| 2026-11-04 18:38:50 | [beziworld/laravel-jpk](https://www.nuget.org/packages/beziworld%2Flaravel-jpk) | v1.0.0 | Kamil Ćwiertnia | Polish JPK (SAF-T) for Laravel: JPK_V7M(3)/JPK_V7K(3), JPK_FA(4) and JPK_MAG bu… |
| 2026-11-04 18:50:19 | [spkm/topdesk](https://www.nuget.org/packages/spkm%2Ftopdesk) | v1.0.0 | Simon Mitchell | Integrate with the TOPdesk API using SaloonPHP |
| 2026-11-04 18:51:44 | [greenfieldr/golb_events](https://www.nuget.org/packages/greenfieldr%2Fgolb_events) | 14.0.0 | Marcel Küpper | Golb Events - Events The Page Way! An add-on to the TYPO3 blog extension Golb t… |
| 2026-11-04 18:53:57 | [beziworld/laravel-inpost-pay](https://www.nuget.org/packages/beziworld%2Flaravel-inpost-pay) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the InPost Pay merchant API: basket binding, orders, refunds… |
| 2026-11-04 18:54:15 | [beziworld/laravel-saldeo](https://www.nuget.org/packages/beziworld%2Flaravel-saldeo) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the SaldeoSMART API-XML: companies, contractors, documents,… |
| 2026-11-04 18:54:33 | [beziworld/laravel-erli](https://www.nuget.org/packages/beziworld%2Flaravel-erli) | v1.0.0 | Kamil Ćwiertnia | Laravel client for the Erli.pl marketplace Shop API: products, stock and prices… |
| 2026-11-04 18:55:43 | [leestratman/wp-content-bundle](https://www.nuget.org/packages/leestratman%2Fwp-content-bundle) | v1.0.0 |  | Export and import WordPress content bundles: portable slices of content with th… |
| 2026-11-04 18:58:03 | [maco-studios/corsair](https://www.nuget.org/packages/maco-studios%2Fcorsair) | v0.0.1 | Marcos "Marcão" Aurelio | Docker-powered local dev environment for Magento 1, Magento 2, OpenMage, Mage-O… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
