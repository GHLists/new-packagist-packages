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

## Latest list — 2026-10-09 15:23 UTC

New packages created between 2026-10-09 14:19 UTC and 2026-10-09 15:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T15-23-14-899962Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 14:21:20 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.4.8 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-09 14:31:38 | [survos/workflow-async-bundle](https://www.nuget.org/packages/survos%2Fworkflow-async-bundle) | 2.36.0 |  | Queued native Symfony workflow transitions through Messenger |
| 2026-10-09 14:31:44 | [survos/workflow-extras-bundle](https://www.nuget.org/packages/survos%2Fworkflow-extras-bundle) | 2.36.0 |  | Metadata conveniences and next-transition selection for native Symfony workflows |
| 2026-10-09 14:33:45 | [spits-online/laravel-options](https://www.nuget.org/packages/spits-online%2Flaravel-options) | V1.0.0 | Spits | Cached database options for Laravel |
| 2026-10-09 14:34:28 | [afaztech/reactor-broadcast](https://www.nuget.org/packages/afaztech%2Freactor-broadcast) | v0.1.0 | Abolfazl Majidi (Afaz) | Broadcast (send / copy / forward) with progress statistics for Reactor bots. |
| 2026-10-09 14:36:14 | [webx-ui/themes](https://www.nuget.org/packages/webx-ui%2Fthemes) | v0.66.0 | WebX UI | Site themes as layers: a local theme over a packaged one over the modules, reso… |
| 2026-10-09 14:53:51 | [webx-ui/widgets](https://www.nuget.org/packages/webx-ui%2Fwidgets) | v0.66.0 | WebX UI | The interactive pieces every site repeats — menus, dialogs, tabs, accordions, c… |
| 2026-10-09 14:54:28 | [medienreaktor/neos-api-mcp](https://www.nuget.org/packages/medienreaktor%2Fneos-api-mcp) | 0.1.0 |  | An MCP server for Neos 9 on top of the Neos API: Claude and other MCP clients w… |
| 2026-10-09 14:54:34 | [webx-ui/theme-default](https://www.nuget.org/packages/webx-ui%2Ftheme-default) | v0.66.0 | WebX UI | The theme every new WebX UI site stands on: a value for every site token, the p… |
| 2026-10-09 14:57:28 | [rafathomas/laravel-architecture-guard](https://www.nuget.org/packages/rafathomas%2Flaravel-architecture-guard) | v0.1.0 |  | AST-based architectural dependency checks for Laravel and PHP projects. |
| 2026-10-09 14:57:32 | [jengo/search](https://www.nuget.org/packages/jengo%2Fsearch) | v0.1.0 | Ian Ochieng | Enterprise-grade, multi-driver full-text and semantic search engine subsystem f… |
| 2026-10-09 15:19:25 | [osw3/wp-feat-analytics](https://www.nuget.org/packages/osw3%2Fwp-feat-analytics) | 0.0.1 | OSW3 | . |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
