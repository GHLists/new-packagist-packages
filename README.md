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

## Latest list — 2026-09-28 17:22 UTC

New packages created between 2026-09-28 16:19 UTC and 2026-09-28 17:22 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T17-22-18-361416Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 16:19:35 | [tcgunel/omniship-navlungo](https://www.nuget.org/packages/tcgunel%2Fomniship-navlungo) | v0.0.2 |  | Navlungo Domestic carrier for Omniship shipping library |
| 2026-09-28 16:26:10 | [spora-ai/spora-plugin-staan](https://www.nuget.org/packages/spora-ai%2Fspora-plugin-staan) | v0.1.0 |  | EU-hosted web search via Staan — ranked results, or relevance-scored page excer… |
| 2026-09-28 16:28:11 | [polunich/wp-jsonapi](https://www.nuget.org/packages/polunich%2Fwp-jsonapi) | v1.0.0 |  | JSON:API 1.1 on the WordPress REST API |
| 2026-09-28 16:29:29 | [dirthara/messaging](https://www.nuget.org/packages/dirthara%2Fmessaging) | 0.1.0 | Dirthara | Transport-neutral, one-way message publishing for PHP and the Dirthara framework |
| 2026-09-28 16:31:31 | [altirs/sdk](https://www.nuget.org/packages/altirs%2Fsdk) | v0.1.0 |  | PHP SDK for Altirs — Guardrails-as-a-Service API |
| 2026-09-28 16:59:55 | [orbis-cms/mcp](https://www.nuget.org/packages/orbis-cms%2Fmcp) | 0.0.4 |  | MCP server integration for Orbis CMS. |
| 2026-09-28 17:04:23 | [skyyware/stage-cms](https://www.nuget.org/packages/skyyware%2Fstage-cms) | v0.1.0 |  | A CMS for people and agents, built on Stage. |
| 2026-09-28 17:14:15 | [payloadshield/laravelps](https://www.nuget.org/packages/payloadshield%2Flaravelps) | 1.0.0 | Ganesh Kandu | Pluggable Laravel middleware for encrypting/decrypting request and response pay… |
| 2026-09-28 17:15:32 | [jblab/wide-events-bundle](https://www.nuget.org/packages/jblab%2Fwide-events-bundle) | 0.1.0 |  | Safe, structured canonical wide events bundle for Symfony applications. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
