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

## Latest list — 2026-11-19 18:21 UTC

New packages created between 2026-11-19 17:19 UTC and 2026-11-19 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T18-21-14-568765Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 17:20:19 | [braesident/cipherpdo](https://www.nuget.org/packages/braesident%2Fcipherpdo) | 1.0.0 | Sebastian Braesicke | PDO-Erweiterung mit feldweiser Verschlüsselung und erweiterten Statements. |
| 2026-11-19 17:22:19 | [aranxo/netinfo](https://www.nuget.org/packages/aranxo%2Fnetinfo) | v0.1.0 | Andreas Hofmann | Static helpers for IPv4/IPv6 CIDR calculations, bogon detection, allow-list loa… |
| 2026-11-19 17:26:23 | [simply-digital/laravel-rich-editor](https://www.nuget.org/packages/simply-digital%2Flaravel-rich-editor) | v0.1.0 | Yusaini Usulludin | A lightweight rich-text HTML editor for Laravel and Livewire with image uploads |
| 2026-11-19 17:30:45 | [empiricompany/maho-product-labels](https://www.nuget.org/packages/empiricompany%2Fmaho-product-labels) | 1.0.0 |  | Rule-driven product labels (badges) for category listings, product pages, widge… |
| 2026-11-19 17:36:46 | [gboquizosanchez/phpstan-code-limits](https://www.nuget.org/packages/gboquizosanchez%2Fphpstan-code-limits) | 1.3.0 | Germán Boquizo Sánchez | PHPStan rules that enforce size, layout and expression limits on PHP code |
| 2026-11-19 17:43:58 | [braesident/dialectsql](https://www.nuget.org/packages/braesident%2Fdialectsql) | 1.0.0 | Sebastian Braesicke | SQL-Builder für MySQL, MariaDB und Microsoft SQL Server. |
| 2026-11-19 17:53:49 | [mputkowski/laravel-discord-alerts](https://www.nuget.org/packages/mputkowski%2Flaravel-discord-alerts) | v1.0 |  | Post exception reports and custom messages to a Discord channel through a bot. |
| 2026-11-19 17:57:38 | [darory/whatsapp](https://www.nuget.org/packages/darory%2Fwhatsapp) | v1.0.1 | Darory | PHP and Laravel client for the Darory WhatsApp API: send messages and files, ch… |
| 2026-11-19 18:12:57 | [brocode/module-poppy](https://www.nuget.org/packages/brocode%2Fmodule-poppy) | 1.0.0 | Benjamin Rosenberger | Personal Agent Protocol (Poppy) discovery for Magento 2: publishes /.well-known… |
| 2026-11-19 18:15:10 | [brunasebold/module-magento-csp](https://www.nuget.org/packages/brunasebold%2Fmodule-magento-csp) | 1.0.0 | Bruna Sebold | Manage Magento Content Security Policy hosts from the admin and send them on th… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
