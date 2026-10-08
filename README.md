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

## Latest list — 2026-10-08 15:21 UTC

New packages created between 2026-10-08 14:22 UTC and 2026-10-08 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T15-21-22-526536Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 14:22:42 | [itxshakil/cpanel-whm](https://www.nuget.org/packages/itxshakil%2Fcpanel-whm) | v0.1.0 | Shakil Alam | A typed, token-only, fakeable cPanel WHM API 1 client for Laravel, with UAPI th… |
| 2026-10-08 14:32:01 | [ymwl/think8-mcp](https://www.nuget.org/packages/ymwl%2Fthink8-mcp) | v1.0.0 | ymwl | MCP (Model Context Protocol) server for ThinkPHP 8.x — let AI tools (Claude Cod… |
| 2026-10-08 14:39:02 | [fomvasss/laravel-notification-channel-gronosync](https://www.nuget.org/packages/fomvasss%2Flaravel-notification-channel-gronosync) | 0.1.1 | Fomin Vasil | Laravel notification channel for GronoSync — send messages via Telegram, WhatsA… |
| 2026-10-08 14:40:53 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.4.2 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-08 14:40:53 | [astral-php/astral-extend-orm](https://www.nuget.org/packages/astral-php%2Fastral-extend-orm) | 0.1.1 | astral-php | Extension ORM pour Astral — Fillable, Casts, Accessors, Hidden, Relations décla… |
| 2026-10-08 14:42:57 | [astral-php/astral-debug](https://www.nuget.org/packages/astral-php%2Fastral-debug) | 0.1.0 | astral-php | Barre de debug Astral — temps, mémoire, SQL, messages (dev uniquement) |
| 2026-10-08 14:45:24 | [astral-php/astral-payment](https://www.nuget.org/packages/astral-php%2Fastral-payment) | 0.1.1 | astral-php | Intégration Stripe pour Astral — PaymentIntent, webhooks, events, remboursements |
| 2026-10-08 14:49:18 | [novay/minios](https://www.nuget.org/packages/novay%2Fminios) | 0.0.5 | Noviyanto Rahmadi | MiniOS Desktop Environment for Laravel |
| 2026-10-08 14:56:04 | [dniccum/linear-sdk](https://www.nuget.org/packages/dniccum%2Flinear-sdk) | v0.2.1 | Doug Niccum | A Laravel SDK for creating Linear issues from Eloquent models, with an optional… |
| 2026-10-08 15:04:01 | [floxum/spam-prevention](https://www.nuget.org/packages/floxum%2Fspam-prevention) | 0.1.2 | Team Floxum | Spam prevention for your Flarum community. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
