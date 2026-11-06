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

## Latest list — 2026-11-06 19:19 UTC

New packages created between 2026-11-06 18:21 UTC and 2026-11-06 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T19-19-48-898709Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 18:24:43 | [goletter/hyperf-observability](https://www.nuget.org/packages/goletter%2Fhyperf-observability) | v1.0.0 | goletter | Hyperf ECS 日志管道与 OpenTelemetry 链路上下文。 |
| 2026-11-06 18:25:17 | [cheevauva/uua](https://www.nuget.org/packages/cheevauva%2Fuua) | v0.1.1 | cheevauva | Universal Unit Architecture for PHP |
| 2026-11-06 18:42:02 | [mithridatem/mvc-script-generator](https://www.nuget.org/packages/mithridatem%2Fmvc-script-generator) | v1.0.3 |  | Generateur Bash de projets MVC PHP (basic, advanced web et API JWT) |
| 2026-11-06 18:52:21 | [totalcrm/cdek-php-sdk](https://www.nuget.org/packages/totalcrm%2Fcdek-php-sdk) | v1.0.0 | Aleksandr Romanenko; TotalCRM | CDEK 2.0 SDK PHP by TotalCRM |
| 2026-11-06 19:07:30 | [1994/flatpack-statamic](https://www.nuget.org/packages/1994%2Fflatpack-statamic) | v1.0.0 | 1994 | Compile Statamic's flat-file content at deploy into PHP files OPcache serves fr… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
