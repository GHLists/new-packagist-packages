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

## Latest list — 2026-10-20 10:21 UTC

New packages created between 2026-10-20 09:22 UTC and 2026-10-20 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T10-21-19-727678Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 09:22:39 | [systopia/de.systopia.selfservice](https://www.nuget.org/packages/systopia%2Fde.systopia.selfservice) | 1.1.0 | SYSTOPIA GmbH | Infrastructure for personalised and selfservice forms |
| 2026-10-20 09:26:43 | [silarhi/ux-icons-js-bundle](https://www.nuget.org/packages/silarhi%2Fux-icons-js-bundle) | v0.1.2 | Guillaume Sainthillier | Render Symfony UX Icons in JavaScript, React and Vue, with the same attributes… |
| 2026-10-20 09:30:09 | [wexample/symfony-remote-db-ip](https://www.nuget.org/packages/wexample%2Fsymfony-remote-db-ip) | 1.0.1 |  |  |
| 2026-10-20 09:30:12 | [amrosslee/global-prayer-times](https://www.nuget.org/packages/amrosslee%2Fglobal-prayer-times) | v1.0.0 |  | Offline, framework-independent Islamic prayer-time calculations |
| 2026-10-20 09:51:45 | [rabbitevents/deduplication](https://www.nuget.org/packages/rabbitevents%2Fdeduplication) | v1.0.0 | Eugene Kirdzei | Skips messages redelivered to RabbitEvents listeners, using a Laravel cache sto… |
| 2026-10-20 09:58:43 | [dmlab/module-typesafe-core](https://www.nuget.org/packages/dmlab%2Fmodule-typesafe-core) | 0.0.1 |  | TypeSafe (Jev) AI client for Magento 2: shared connection with your own encrypt… |
| 2026-10-20 09:58:44 | [dmlab/module-catalog-enrich](https://www.nuget.org/packages/dmlab%2Fmodule-catalog-enrich) | 0.0.1 |  | AI product attribute enrichment for Magento 2: fills empty select, multiselect… |
| 2026-10-20 10:12:25 | [devaction/ui](https://www.nuget.org/packages/devaction%2Fui) | v0.1.0 |  | DevAction UI: componentes Blade para Laravel/Livewire com Tailwind CSS v4 e íco… |
| 2026-10-20 10:16:04 | [ev-soft/clever-html-engine](https://www.nuget.org/packages/ev-soft%2Fclever-html-engine) | v1.7.6 | EV-soft | php2html: build HTML5 pages, forms, tables and cards with PHP 8 functions - tra… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
