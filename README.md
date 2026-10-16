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

## Latest list — 2026-10-16 17:22 UTC

New packages created between 2026-10-16 16:21 UTC and 2026-10-16 17:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T17-22-03-164758Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 16:22:44 | [webx-ui/module-notifications](https://www.nuget.org/packages/webx-ui%2Fmodule-notifications) | v0.76.0 | WebX UI | Notification channels for the WebX UI admin panel: Telegram and e-mail, message… |
| 2026-10-16 16:22:48 | [webx-ui/module-snippets](https://www.nuget.org/packages/webx-ui%2Fmodule-snippets) | v0.76.0 | WebX UI | Codes of outside services for the WebX UI admin panel: a tag manager, a counter… |
| 2026-10-16 16:27:54 | [nowo-tech/search-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fsearch-kit-bundle) | v1.0.1 | Héctor Franco Aceituno; Nowo.… | Global header search (command palette) for Symfony: a magnifier that stretches… |
| 2026-10-16 16:35:34 | [ahinest/laravel-permission-manager](https://www.nuget.org/packages/ahinest%2Flaravel-permission-manager) | 1.0.0 |  | Explicit, transactional role hierarchy and permission delegation for Laravel an… |
| 2026-10-16 16:44:34 | [elcreator/amount](https://www.nuget.org/packages/elcreator%2Famount) | 0.1.0 |  | aMount — mount cloud and remote storage (S3, Google Drive, Dropbox, OneDrive, S… |
| 2026-10-16 16:54:15 | [gvargas/atusan-agents](https://www.nuget.org/packages/gvargas%2Fatusan-agents) | v1.1 | Gabriel Vargas | Soporte para Agentes IA de desarrollo |
| 2026-10-16 17:19:51 | [angeo/module-agent-activity](https://www.nuget.org/packages/angeo%2Fmodule-agent-activity) | 1.0.0 |  | See what AI agents do in your Magento 2 store: UCP, MCP and WebMCP calls, AI cr… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
