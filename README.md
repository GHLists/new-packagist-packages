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

## Latest list — 2026-11-11 19:19 UTC

New packages created between 2026-11-11 18:19 UTC and 2026-11-11 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T19-19-05-739083Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 18:24:00 | [kirora/kirora-php](https://www.nuget.org/packages/kirora%2Fkirora-php) | v0.1.0 | Kirora and contributors | Kirora SDK for PHP. |
| 2026-11-11 18:37:29 | [hamdallah90/jsonfuse](https://www.nuget.org/packages/hamdallah90%2Fjsonfuse) | v1.0.0 |  | One-call NDJSON validate, filter and project pipeline for PHP, native and bound… |
| 2026-11-11 18:41:52 | [forumify/forumify-aurora-theme](https://www.nuget.org/packages/forumify%2Fforumify-aurora-theme) | 1.0.0 |  | Night sky glass: frosted panels floating over a slow aurora, with a dawn varian… |
| 2026-11-11 18:41:56 | [forumify/forumify-dossier-theme](https://www.nuget.org/packages/forumify%2Fforumify-dossier-theme) | 1.0.0 |  | A classified field file: stencilled headings, typewritten pages, rubber stamps… |
| 2026-11-11 18:42:00 | [forumify/forumify-gumdrop-theme](https://www.nuget.org/packages/forumify%2Fforumify-gumdrop-theme) | 1.0.0 |  | A cozy clay toybox: puffy pills, soft candy colours and squishy buttons. |
| 2026-11-11 18:42:04 | [forumify/forumify-recon-theme](https://www.nuget.org/packages/forumify%2Fforumify-recon-theme) | 1.0.0 |  | A tactical HUD for milsim units and clans: chamfered panels, signal amber and a… |
| 2026-11-11 18:42:08 | [forumify/forumify-riso-theme](https://www.nuget.org/packages/forumify%2Fforumify-riso-theme) | 1.0.0 |  | A risograph print zine: fluorescent inks, misregistered offset shadows and pape… |
| 2026-11-11 18:42:12 | [forumify/forumify-thermal-theme](https://www.nuget.org/packages/forumify%2Fforumify-thermal-theme) | 1.0.0 |  | Thermal targeting optics: ironbow heat gradients, a scope reticle and panels th… |
| 2026-11-11 18:46:19 | [wai-blue/hubleto-einvoice](https://www.nuget.org/packages/wai-blue%2Fhubleto-einvoice) | 2.0.0-alpha1 |  | Electronic invoicing and Peppol provider integration for Hubleto |
| 2026-11-11 18:57:20 | [marekmiklusek/laravel-slack-errors](https://www.nuget.org/packages/marekmiklusek%2Flaravel-slack-errors) | v1.0.0 | Marek Miklusek | Send every reported exception from your Laravel app to a Slack channel. |
| 2026-11-11 19:12:18 | [braskai/rask-sdk](https://www.nuget.org/packages/braskai%2Frask-sdk) | 3.0.0-alpha.0 |  | PHP SDK for the Rask API v3 (video and audio localization). |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
