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

## Latest list — 2026-10-09 11:21 UTC

New packages created between 2026-10-09 10:18 UTC and 2026-10-09 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T11-21-39-933051Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 10:26:58 | [osw3/wp-site-core](https://www.nuget.org/packages/osw3%2Fwp-site-core) | 0.0.1 | OSW3 | . |
| 2026-10-09 10:36:09 | [oguzhanbayirli/laravel-turkiye](https://www.nuget.org/packages/oguzhanbayirli%2Flaravel-turkiye) | v1.0.0 | Oğuzhan Bayırlı | Turkish identity number (TCKN), tax number (VKN) and IBAN validation, amounts i… |
| 2026-10-09 10:44:45 | [abdulkadiragoliya/content-intelligence](https://www.nuget.org/packages/abdulkadiragoliya%2Fcontent-intelligence) | 1.0.0 | Abdulkadir Agoliya | AI-powered Content & SEO Intelligence for Craft CMS. Audits, scoring, semantic… |
| 2026-10-09 10:59:43 | [merkushin/wpplugin](https://www.nuget.org/packages/merkushin%2Fwpplugin) | v1.0.0 | Dmitry Merkushin | Template for a new WordPress plugin |
| 2026-10-09 11:02:50 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.4.4 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-09 11:06:56 | [limegreentangerine/theme_kit](https://www.nuget.org/packages/limegreentangerine%2Ftheme_kit) | 1.0.0 | Lee Jones | Theme building tools. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
