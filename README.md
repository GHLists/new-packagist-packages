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

## Latest list — 2026-11-18 16:19 UTC

New packages created between 2026-11-18 15:22 UTC and 2026-11-18 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T16-19-46-023152Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 15:26:37 | [bannerstop/mention-api-client-bundle](https://www.nuget.org/packages/bannerstop%2Fmention-api-client-bundle) | v1.0.0 | bannerstop GmbH | Symfony integration of bannerstop/mention-api-client: configuration, an autowir… |
| 2026-11-18 15:26:39 | [bannerstop/mention-api-client-laravel](https://www.nuget.org/packages/bannerstop%2Fmention-api-client-laravel) | v1.0.0 | bannerstop GmbH | Laravel integration of bannerstop/mention-api-client: configuration, a containe… |
| 2026-11-18 15:34:23 | [kirbydesk/kirbyblock-stats](https://www.nuget.org/packages/kirbydesk%2Fkirbyblock-stats) | 1.0.0 | Christian Fickinger | Stats Block for Kirby CMS |
| 2026-11-18 15:36:10 | [thebeardedbear/urssaf-tierce-declaration-auto-entrepreneur](https://www.nuget.org/packages/thebeardedbear%2Furssaf-tierce-declaration-auto-entrepreneur) | v0.1.0 | The Bearded Bear | Client and domain model for the URSSAF "API Tierce Déclaration auto-entrepreneu… |
| 2026-11-18 15:46:09 | [dbravoan/dbcms-installer](https://www.nuget.org/packages/dbravoan%2Fdbcms-installer) | v0.1.1 |  | Instalador CLI de aplicaciones Laravel con dbCMS y extensiones Composer indepen… |
| 2026-11-18 15:48:46 | [webwizardsusa/laravel-image-cache](https://www.nuget.org/packages/webwizardsusa%2Flaravel-image-cache) | v0.1.0 | Jamie Holly | Drupal-style image styles for Laravel: Variants generated on demand, when an Im… |
| 2026-11-18 15:50:43 | [teu/stack-monitor](https://www.nuget.org/packages/teu%2Fstack-monitor) | 1.0.0 | Andreas Hafner; teufels GmbH | Endpoint for stack information |
| 2026-11-18 15:57:54 | [gesnovasalud/environment-indicator](https://www.nuget.org/packages/gesnovasalud%2Fenvironment-indicator) | v1.0.0 | Alvaro Torres | Filament plugin that shows a colored bar and badge with the current environment… |
| 2026-11-18 16:12:15 | [ngsoft/cronicle-tasks-client](https://www.nuget.org/packages/ngsoft%2Fcronicle-tasks-client) | v1.0.0 | Aymeric Anger | PHP HTTP client for the Cronicle JSON REST API, with typed DTOs and OpenAPI sch… |
| 2026-11-18 16:17:59 | [packstub/filament-holler](https://www.nuget.org/packages/packstub%2Ffilament-holler) | v1.0.0 | Ion Caliman; Packstub | Audio, video and screen-share calls inside a Filament panel, 1-on-1 or in group… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
