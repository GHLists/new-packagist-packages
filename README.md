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

## Latest list — 2026-11-24 22:19 UTC

New packages created between 2026-11-24 21:20 UTC and 2026-11-24 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T22-19-20-073177Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 21:30:59 | [coderstudios/do-interview](https://www.nuget.org/packages/coderstudios%2Fdo-interview) | 0.1.1 |  | Researched, voice-based practice interviews with written debriefs, as a Laravel… |
| 2026-11-24 21:41:53 | [psbits/episode-guide](https://www.nuget.org/packages/psbits%2Fepisode-guide) | 0.1.0-alpha | Daniel Ablass | Create your own episode guide library. |
| 2026-11-24 22:02:04 | [runio/easyadmin-ux](https://www.nuget.org/packages/runio%2Feasyadmin-ux) | v0.1.0 | Amer Malik Mohammed | Switchable layouts and a modern UX layer for EasyAdmin 5. |
| 2026-11-24 22:09:41 | [sattleme/module-payment](https://www.nuget.org/packages/sattleme%2Fmodule-payment) | 1.0.0 | sattle.me | sattle.me for Magento Open Source and Adobe Commerce: bitcoin payments, in Ligh… |
| 2026-11-24 22:09:44 | [marcin-orlowski/php-cs-fixer-extras](https://www.nuget.org/packages/marcin-orlowski%2Fphp-cs-fixer-extras) | 1.0.0 | Marcin Orlowski | Extra fixers for PHP CS Fixer. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
