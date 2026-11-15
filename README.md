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

## Latest list — 2026-11-15 09:19 UTC

New packages created between 2026-11-15 08:21 UTC and 2026-11-15 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T09-19-49-783844Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 08:30:05 | [bymdigital/whatsapp-automation-india](https://www.nuget.org/packages/bymdigital%2Fwhatsapp-automation-india) | v1.0.0 | BYM Digital | Enterprise PHP client for Meta WhatsApp Cloud API (v26.0+) with native WhatsApp… |
| 2026-11-15 08:38:35 | [eii/laravel-web-suite](https://www.nuget.org/packages/eii%2Flaravel-web-suite) | v1.0.0 |  | A modular business website backend companion for Laravel, with optional Filamen… |
| 2026-11-15 08:46:37 | [transcriptdock/transcriptdock](https://www.nuget.org/packages/transcriptdock%2Ftranscriptdock) | v0.1.0 | Transcript Dock | PHP client for the Transcript Dock video transcription API |
| 2026-11-15 08:52:16 | [stolt/config-cartographer](https://www.nuget.org/packages/stolt%2Fconfig-cartographer) | v0.1.0 |  | A PHP library and CLI for discovering, tracing, and visualizing application con… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
