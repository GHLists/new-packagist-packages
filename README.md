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

## Latest list — 2026-09-28 03:19 UTC

New packages created between 2026-09-28 02:22 UTC and 2026-09-28 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T03-19-22-06574Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 02:56:59 | [yukazakiri/lepton-agent](https://www.nuget.org/packages/yukazakiri%2Flepton-agent) | v1.0.1 | yukazakiri | Laravel bridge for Lepton Agents (Circle Agent Stack + Arc). No hardcoded CLI s… |
| 2026-09-28 03:13:33 | [adscrawl/adscrawl](https://www.nuget.org/packages/adscrawl%2Fadscrawl) | v0.1.0 | AdsCrawl | Official PHP SDK for the AdsCrawl browser, extraction, screenshot, CDP, and clo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
