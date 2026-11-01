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

## Latest list — 2026-11-01 18:18 UTC

New packages created between 2026-11-01 17:18 UTC and 2026-11-01 18:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T18-18-41-452341Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 17:36:03 | [everrest/context-gate](https://www.nuget.org/packages/everrest%2Fcontext-gate) | v0.1.0 | EverRest | Secure MCP gateway for Laravel: the AI receives only what a contract allows. |
| 2026-11-01 17:37:34 | [arzcode/filament-head](https://www.nuget.org/packages/arzcode%2Ffilament-head) | 0.1.0 | Arzcode | Edit laravel/head metadata (title, description, Open Graph, canonical, robots)… |
| 2026-11-01 17:50:25 | [noldors/lighthouse-extensions](https://www.nuget.org/packages/noldors%2Flighthouse-extensions) | v0.1.0 |  | Reusable Laravel Lighthouse directives and scalars. |
| 2026-11-01 17:52:47 | [tacraft-sociality/flarum-onebot-notify](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-onebot-notify) | 1.0.3 | TaCraft-Sociality | Send OneBot (QQ) notifications about new discussions and posts from Flarum |
| 2026-11-01 17:53:52 | [noldors/lighthouse-idempotency](https://www.nuget.org/packages/noldors%2Flighthouse-idempotency) | v0.1.0 |  | Transactional PostgreSQL idempotency for Laravel Lighthouse mutations. |
| 2026-11-01 17:56:39 | [unlyx/unlyx-php](https://www.nuget.org/packages/unlyx%2Funlyx-php) | v1.0.0 | Unlyx | Official PHP SDK for the Unlyx REST API v1 (account, services, orders, webhooks… |
| 2026-11-01 18:06:00 | [tusharkhan/semantic-sec](https://www.nuget.org/packages/tusharkhan%2Fsemantic-sec) | v0.1.0 | Tushar Khan | LLM-assisted authorization and IDOR scanner for Laravel applications. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
