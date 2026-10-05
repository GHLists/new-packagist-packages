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

## Latest list — 2026-10-05 00:19 UTC

New packages created between 2026-10-04 23:19 UTC and 2026-10-05 00:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T00-19-38-614447Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 23:21:23 | [edulazaro/larablog](https://www.nuget.org/packages/edulazaro%2Flarablog) | 1.0.0 | Edu Lazaro | Markdown blogs for Laravel in several languages, each with its own URL: one fol… |
| 2026-10-04 23:33:49 | [mage2kishan/module-llms-txt](https://www.nuget.org/packages/mage2kishan%2Fmodule-llms-txt) | 1.5.5 | Kishan Savaliya | Panth LLMs.txt — AI Indexing Engine for Magento 2. Serves structured /llms.txt,… |
| 2026-10-04 23:35:30 | [sattorware/elephant](https://www.nuget.org/packages/sattorware%2Felephant) | v1.0.0 | sattorware | Async PHP on fibers: write concurrent code that reads like plain PHP — tasks, t… |
| 2026-10-05 00:12:51 | [foxws/laravel-media](https://www.nuget.org/packages/foxws%2Flaravel-media) | 0.1.0 | foxws | Probe, encode, package and stream media in Laravel with ffmpeg. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
