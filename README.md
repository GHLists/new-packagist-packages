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

## Latest list — 2026-11-06 06:19 UTC

New packages created between 2026-11-06 05:19 UTC and 2026-11-06 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T06-19-55-004396Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 05:23:48 | [shafqatjan/laravel-amp-mail](https://www.nuget.org/packages/shafqatjan%2Flaravel-amp-mail) | v1.0.0 | Shafqat Jan | Send interactive AMP emails (Gmail, Yahoo Mail, Mail.ru) from Laravel mailables |
| 2026-11-06 05:49:00 | [sunrice/commerce](https://www.nuget.org/packages/sunrice%2Fcommerce) | v0.1.0 |  | An e-commerce package for Sunrice CMS: catalog, cart, checkout, orders, payment… |
| 2026-11-06 05:58:21 | [ibraheem-ghazi/laravel-ai-flow](https://www.nuget.org/packages/ibraheem-ghazi%2Flaravel-ai-flow) | 1.0 |  | Composable queued AI workflows for Laravel with steps, tasks, structured genera… |
| 2026-11-06 06:12:00 | [stateforge/scenario-ai](https://www.nuget.org/packages/stateforge%2Fscenario-ai) | 1.0 | Christina Koenig | AI-assisted generation of Scenarios, Parameter Types, and coding agent skills. |
| 2026-11-06 06:14:55 | [stateforge/scenario-laravel-ai](https://www.nuget.org/packages/stateforge%2Fscenario-laravel-ai) | 1.0 | Christina Koenig | Laravel adapter for Stateforge Scenario AI - AI-assisted generation of Scenario… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
