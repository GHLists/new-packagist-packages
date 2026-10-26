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

## Latest list — 2026-10-26 16:20 UTC

New packages created between 2026-10-26 15:21 UTC and 2026-10-26 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T16-20-43-337127Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 15:43:26 | [luinuxscl/openrouter](https://www.nuget.org/packages/luinuxscl%2Fopenrouter) | v1.0.0 | Luis Sepulveda | Paquete para integrar el servicio de conexión con OpenRouter |
| 2026-10-26 15:43:30 | [luinuxscl/ai-posts](https://www.nuget.org/packages/luinuxscl%2Fai-posts) | v1.0.0 | Luis Sepulveda | Laravel package para la creación secuencial de posts para WordPress con estados… |
| 2026-10-26 15:43:34 | [luinuxscl/seo-content-seeds](https://www.nuget.org/packages/luinuxscl%2Fseo-content-seeds) | v1.1.0 | LuinuxSCL | Paquete Laravel para obtener ideas para la creación de contenido SEO desde dive… |
| 2026-10-26 15:43:34 | [luinuxscl/seo-contents-seeds](https://www.nuget.org/packages/luinuxscl%2Fseo-contents-seeds) | v1.1.0 | LuinuxSCL | Paquete Laravel para obtener ideas para la creación de contenido SEO desde dive… |
| 2026-10-26 15:43:39 | [luinuxscl/post-pilot](https://www.nuget.org/packages/luinuxscl%2Fpost-pilot) | v1.0.0 | Luis Sepulveda | Automatiza la creación de contenido con agentes escritores inteligentes en Lara… |
| 2026-10-26 15:43:43 | [luinuxscl/laravel-api-key-manager](https://www.nuget.org/packages/luinuxscl%2Flaravel-api-key-manager) | v1.0.0 |  | Package para gestionar API Keys de servicios externos en Laravel. |
| 2026-10-26 15:43:47 | [luinuxscl/laravel-jetstream-translate](https://www.nuget.org/packages/luinuxscl%2Flaravel-jetstream-translate) | v1.1.0 | Luis Sepúlveda | Paquete de traduccion de eng/esp LikePlatform. |
| 2026-10-26 15:43:51 | [luinuxscl/wordpress-laravel-integration](https://www.nuget.org/packages/luinuxscl%2Fwordpress-laravel-integration) | v1.0.0 | Luis Sepulveda | Package para integrar WordPress con Laravel |
| 2026-10-26 15:52:11 | [phpstats/juphyter](https://www.nuget.org/packages/phpstats%2Fjuphyter) | v0.1.0 | Erik Westlund | A Jupyter and Quarto kernel for PHP, built for statistical work with the phpsta… |
| 2026-10-26 15:56:02 | [n1co/epay](https://www.nuget.org/packages/n1co%2Fepay) | v0.1.0 | n1co | Server-side SDK for the n1co ePay API (PHP). |
| 2026-10-26 16:12:58 | [usman-ahmed/crud-engine](https://www.nuget.org/packages/usman-ahmed%2Fcrud-engine) | v1.0.0 | Usman Ahmed | Generic CRUD services, file lifecycle management, nested relation synchronizati… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
