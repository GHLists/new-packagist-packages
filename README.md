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

## Latest list — 2026-09-28 14:20 UTC

New packages created between 2026-09-28 13:21 UTC and 2026-09-28 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T14-20-58-101177Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 13:25:41 | [tobimori/kirby-agents](https://www.nuget.org/packages/tobimori%2Fkirby-agents) | 0.1.0 | Tobias Möritz | Stateless MCP server for Kirby CMS with OAuth, blueprint-aware editing, and pag… |
| 2026-09-28 13:33:44 | [wexample/symfony-remote-demo](https://www.nuget.org/packages/wexample%2Fsymfony-remote-demo) | 1.0.1 |  |  |
| 2026-09-28 13:39:47 | [shannonllc/webhookadmin](https://www.nuget.org/packages/shannonllc%2Fwebhookadmin) | v0.1.0 | SHANNON LIMITED LIABILITY COM… | PHP SDK for Webhook Admin: send webhooks, manage endpoints and verify signature… |
| 2026-09-28 13:48:50 | [ayangzy/real-seed](https://www.nuget.org/packages/ayangzy%2Freal-seed) | v0.1.0 | ayangzy | Generate realistic, relational, temporally coherent synthetic data for non-prod… |
| 2026-09-28 13:56:48 | [christianjbrown/etsy-open-api-sdk](https://www.nuget.org/packages/christianjbrown%2Fetsy-open-api-sdk) | v1.0.0 | Christian Brown | A strongly-typed PHP 8.5+ client for the Etsy Open API v3 that returns typed mo… |
| 2026-09-28 13:58:19 | [hauerheinrich/hh-readable-anchor](https://www.nuget.org/packages/hauerheinrich%2Fhh-readable-anchor) | 1.0.0 | Christian Hackl | Lesbare Sprungmarken (Anker-IDs) für alle Inhaltselemente – aus der Überschrift… |
| 2026-09-28 14:15:24 | [featvalue/contao](https://www.nuget.org/packages/featvalue%2Fcontao) | 1.0.0 | FeatValue | Embeds the FeatValue client portal in a Contao website. |
| 2026-09-28 14:16:27 | [wexample/symfony-remote-rocket-chat](https://www.nuget.org/packages/wexample%2Fsymfony-remote-rocket-chat) | 1.0.1 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
