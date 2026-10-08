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

## Latest list — 2026-10-08 09:20 UTC

New packages created between 2026-10-08 08:22 UTC and 2026-10-08 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T09-20-51-892813Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 08:23:17 | [andronewille/sluis](https://www.nuget.org/packages/andronewille%2Fsluis) | v0.1.0 |  | Masks personal data in Dutch text on its way into an AI system, and puts it bac… |
| 2026-10-08 08:23:17 | [andronewille/sluis-onnx](https://www.nuget.org/packages/andronewille%2Fsluis-onnx) | v0.1.0 |  | A local ONNX model as a Sluis recogniser: the names, streets and towns that no… |
| 2026-10-08 08:27:26 | [hwkdo/llama-parse-laravel](https://www.nuget.org/packages/hwkdo%2Fllama-parse-laravel) | v0.1.0 | hwkdo | LlamaParse-Client für Laravel |
| 2026-10-08 09:06:05 | [wpstarter/o-workbench](https://www.nuget.org/packages/wpstarter%2Fo-workbench) | v2.0 |  | Workbench Companion for Laravel Packages Development |
| 2026-10-08 09:08:10 | [webatvantage/guzzle-log-middleware](https://www.nuget.org/packages/webatvantage%2Fguzzle-log-middleware) | 2.3.1 | George Mponos; Webatvantage | A Guzzle middleware to log request and responses automatically |
| 2026-10-08 09:11:13 | [parisek/lint-kit](https://www.nuget.org/packages/parisek%2Flint-kit) | v0.1.0 |  | Twig and PHPStan lint rules for WordPress and Drupal projects: a CMS-neutral co… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
