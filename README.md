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

## Latest list — 2026-11-09 23:21 UTC

New packages created between 2026-11-09 22:19 UTC and 2026-11-09 23:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T23-21-19-071407Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 22:20:35 | [preflow/starter](https://www.nuget.org/packages/preflow%2Fstarter) | v0.63.0 |  | Preflow Jobs: a job board starter on SQLite, with a public site, employer accou… |
| 2026-11-09 22:20:35 | [preflow/starter-folio](https://www.nuget.org/packages/preflow%2Fstarter-folio) | v0.63.0 |  | Preflow Jobs with Folio: the job board starter with a content admin for staff,… |
| 2026-11-09 22:23:27 | [intragile/laravel-changelog](https://www.nuget.org/packages/intragile%2Flaravel-changelog) | v1.0.0 | IntrAgile Kft. | Serves a Laravel app's Keep a Changelog CHANGELOG.md, with per-locale translati… |
| 2026-11-09 22:43:40 | [x-multibyte/blatui-starter](https://www.nuget.org/packages/x-multibyte%2Fblatui-starter) | v0.0.2 |  | A Laravel starter kit pre-wired with BlatUI — shadcn/ui for the BLAT stack. |
| 2026-11-09 22:45:10 | [will-wright1/module-garage](https://www.nuget.org/packages/will-wright1%2Fmodule-garage) | 0.1.0-beta.1 |  | Customer vehicle garages, structured vehicle selection and product fitment for… |
| 2026-11-09 22:55:23 | [ernestdefoe/member-map](https://www.nuget.org/packages/ernestdefoe%2Fmember-map) | 1.0.0 | Ernest Defoe | Member Map: an opt-in map of where your community's members are, with a city se… |
| 2026-11-09 23:05:08 | [helpfalcon/helpfalcon-php](https://www.nuget.org/packages/helpfalcon%2Fhelpfalcon-php) | v1.0.0 |  | HelpFalcon API client for PHP, generated from the OpenAPI document. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
