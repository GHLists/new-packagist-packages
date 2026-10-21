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

## Latest list — 2026-10-21 13:21 UTC

New packages created between 2026-10-21 12:20 UTC and 2026-10-21 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T13-21-32-625549Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 12:22:53 | [esoul-cz/phpunit-test-evidence](https://www.nuget.org/packages/esoul-cz%2Fphpunit-test-evidence) | v0.1.1 | Tomáš Vojík | PHPUnit extension and CLI that turn a tagged group of tests into a Markdown evi… |
| 2026-10-21 12:25:02 | [nyumbani/daraja](https://www.nuget.org/packages/nyumbani%2Fdaraja) | v1.0.0 | Alvin Kaburu | A small Laravel client for Safaricom's Daraja API: STK push, C2B and Pull trans… |
| 2026-10-21 12:25:06 | [nyumbani/messaging](https://www.nuget.org/packages/nyumbani%2Fmessaging) | v1.0.0 | Alvin Kaburu | Queue SMS from any Nyumbani app through Nyumbani Connect: a message builder, ha… |
| 2026-10-21 12:33:38 | [amjadiqbal/laravel-gridjs](https://www.nuget.org/packages/amjadiqbal%2Flaravel-gridjs) | v1.0.0 | Amjad Iqbal | Grid.js datagrid for Laravel: turn any Eloquent query into a searchable, sortab… |
| 2026-10-21 12:34:56 | [amjadiqbal/laravel-mysql-advisor](https://www.nuget.org/packages/amjadiqbal%2Flaravel-mysql-advisor) | v0.1.0 | Amjad Iqbal | Read-only MySQL and MariaDB health advisor for Laravel: finds unused, redundant… |
| 2026-10-21 12:35:15 | [nyumbani/essentials](https://www.nuget.org/packages/nyumbani%2Fessentials) | v1.0.0 | Alvin Kaburu | Opinionated helpers, services, UIs, packages, and AI skills and rules that defi… |
| 2026-10-21 12:35:55 | [stero/shield](https://www.nuget.org/packages/stero%2Fshield) | v0.1.1 | Stero Tech Inc. | Framework-agnostic intrusion detection and prevention layer for PHP web apps. |
| 2026-10-21 12:39:55 | [ahmdrv/laravel-nav](https://www.nuget.org/packages/ahmdrv%2Flaravel-nav) | v0.1.1 | ahmdrv | Fluent navigation definitions and immutable request-aware navigation trees for… |
| 2026-10-21 12:49:18 | [victorio/filament-acceptance](https://www.nuget.org/packages/victorio%2Ffilament-acceptance) | v0.1.0 | Victorio | Send any Filament record for approval: sealed, tamper-evident versions and prov… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
