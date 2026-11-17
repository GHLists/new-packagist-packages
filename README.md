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

## Latest list — 2026-11-17 15:21 UTC

New packages created between 2026-11-17 14:20 UTC and 2026-11-17 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T15-21-51-787436Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 14:27:20 | [papi-ai/mcp](https://www.nuget.org/packages/papi-ai%2Fmcp) | v0.15.0 | Marcello Duarte | Model Context Protocol client for PapiAI: hands an MCP server's tools to the Ag… |
| 2026-11-17 14:34:45 | [gunner42/laravel-eet-module](https://www.nuget.org/packages/gunner42%2Flaravel-eet-module) | v1.0.1 | GuNNeR42 | Laravel client for the Czech electronic registration of sales (EET 2.0) |
| 2026-11-17 14:36:46 | [webservco/auth](https://www.nuget.org/packages/webservco%2Fauth) | v0.0.2 | Radu Maier | A PHP component/library. Password authentication and authenticated sessions for… |
| 2026-11-17 14:48:02 | [osaris-uk/click-and-drop](https://www.nuget.org/packages/osaris-uk%2Fclick-and-drop) | v1.0.1 | Osaris | Laravel client for the Royal Mail Click & Drop API (orders, labels, manifests,… |
| 2026-11-17 14:52:30 | [klass8s/k8schema-generator](https://www.nuget.org/packages/klass8s%2Fk8schema-generator) | v0.1.0 |  | Generates PHP classes from Kubernetes API schema definitions |
| 2026-11-17 14:56:59 | [klass8s/klass8s](https://www.nuget.org/packages/klass8s%2Fklass8s) | v0.1.0 | Petr Buchin | Define Kubernetes manifests as PHP classes |
| 2026-11-17 15:01:11 | [xefi/faker-php-bank](https://www.nuget.org/packages/xefi%2Ffaker-php-bank) | v1.0.0 | Lucas GOSGNACH | Faker extension to generate banking and credit card data |
| 2026-11-17 15:05:14 | [ombimo/laravel-html-cache](https://www.nuget.org/packages/ombimo%2Flaravel-html-cache) | 0.1.0 | Bimo Aji Pamungkas | Route-based full page HTML cache for Laravel, with resolve and write middleware |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
