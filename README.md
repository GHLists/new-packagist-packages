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

## Latest list — 2026-11-09 01:22 UTC

New packages created between 2026-11-09 00:21 UTC and 2026-11-09 01:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T01-22-03-396156Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 00:29:25 | [laraxgram/armada](https://www.nuget.org/packages/laraxgram%2Farmada) | v0.1.0 | AmirHkrg | Docker files for running and deploying LaraGram applications and Telegram Bot A… |
| 2026-11-09 01:11:47 | [shopproof/compliance](https://www.nuget.org/packages/shopproof%2Fcompliance) | 0.5.0 | Apex Point Consulting GmbH | EU compliance help for Shopware shops: withdrawal button, product safety (GPSR)… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
