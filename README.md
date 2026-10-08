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

## Latest list — 2026-10-08 00:21 UTC

New packages created between 2026-10-07 23:20 UTC and 2026-10-08 00:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T00-21-55-124986Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 23:29:35 | [skunkwerkx/hypertabular](https://www.nuget.org/packages/skunkwerkx%2Fhypertabular) | v0.7.0 | Brian Buvinghausen | Delimited text (CSV, TSV) and workbooks (XLSX, ODS) read a batch at a time into… |
| 2026-10-07 23:53:30 | [opensolr/chat-bot-client](https://www.nuget.org/packages/opensolr%2Fchat-bot-client) | v0.1.3 |  | A chatbot for any website whose content is in an Opensolr Index: mounted on one… |
| 2026-10-08 00:19:34 | [jeffersongoncalves/filament-translation-manager](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-translation-manager) | 3.0.0 | Jefferson Gonçalves | Translation manager for Filament: edit app, JSON and vendor package translation… |
| 2026-10-08 00:19:34 | [jeffersongoncalves/laravel-translation-manager](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-translation-manager) | 1.0.0 | Jefferson Gonçalves | Database overrides for Laravel translations: edit any key - app, JSON or vendor… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
