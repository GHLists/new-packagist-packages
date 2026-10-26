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

## Latest list — 2026-10-26 00:19 UTC

New packages created between 2026-10-25 23:20 UTC and 2026-10-26 00:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T00-19-36-713651Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 23:45:34 | [crustum/ai-nexus](https://www.nuget.org/packages/crustum%2Fai-nexus) | 1.0.0 | Evgeny Tomenko | AiNexus plugin for CakePHP |
| 2026-10-25 23:59:34 | [wilycode/filter](https://www.nuget.org/packages/wilycode%2Ffilter) | v0.1.0 | Simon Piter | Small filter contract for reusable value normalization. |
| 2026-10-26 00:11:01 | [wilycode/validator](https://www.nuget.org/packages/wilycode%2Fvalidator) | v0.1.0 | Simon Piter | Framework-independent PHP validation contract with reusable validators and stru… |
| 2026-10-26 00:12:39 | [claviron/symfony](https://www.nuget.org/packages/claviron%2Fsymfony) | v0.1.0 |  | Symfony HttpKernel adapter for Claviron's persistent PHP application runtime |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
