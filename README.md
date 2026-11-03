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

## Latest list — 2026-11-03 13:19 UTC

New packages created between 2026-11-03 12:20 UTC and 2026-11-03 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T13-19-55-484173Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 12:42:19 | [helgesverre/laravel-slackcache](https://www.nuget.org/packages/helgesverre%2Flaravel-slackcache) | v0.1.0 | Helge Sverre | A Laravel cache store persisted to a Slack channel. One message per key. Evicti… |
| 2026-11-03 12:51:27 | [rowbird/laravel-safe-url](https://www.nuget.org/packages/rowbird%2Flaravel-safe-url) | 0.1.0 | Fabio Selau | Laravel validation rules that block adult, malware, phishing and gambling URLs… |
| 2026-11-03 13:17:38 | [goletter/hyperf-openapi](https://www.nuget.org/packages/goletter%2Fhyperf-openapi) | 1.0.0 | goletter | Hyperf OpenAPI 3：自动扫描分发 Controller 生成文档，可直接导入 Apifox（无需注解）。 |
| 2026-11-03 13:18:26 | [woutersf/mautic-openapi-bundle](https://www.nuget.org/packages/woutersf%2Fmautic-openapi-bundle) | 7.0.0 | Dropsolid | Exposes a public OpenAPI 3.1.0 specification endpoint and Swagger UI viewer for… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
