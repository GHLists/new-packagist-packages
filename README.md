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

## Latest list — 2026-11-21 08:21 UTC

New packages created between 2026-11-21 07:21 UTC and 2026-11-21 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T08-21-13-185445Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 07:22:54 | [particle-academy/prism-agent-docs](https://www.nuget.org/packages/particle-academy%2Fprism-agent-docs) | v0.1.2 | Wish Born | A Word-document subagent for prism-harness: edits an existing .docx or creates… |
| 2026-11-21 07:27:35 | [formbridge/formbridge-bundle](https://www.nuget.org/packages/formbridge%2Fformbridge-bundle) | v0.1.1 |  | Symfony forms as MCP tools, as forms a person completes inside the conversation… |
| 2026-11-21 07:45:41 | [clesson-de/silverstripe-elemental-essentials](https://www.nuget.org/packages/clesson-de%2Fsilverstripe-elemental-essentials) | 1.0.1 |  | Essential text, image, video and audio content elements for Silverstripe Elemen… |
| 2026-11-21 08:00:38 | [adnane1deev/laravel-charipay](https://www.nuget.org/packages/adnane1deev%2Flaravel-charipay) | v1.0.0 |  | A Laravel integration for the ChariPay payment API. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
