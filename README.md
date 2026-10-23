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

## Latest list — 2026-10-23 08:19 UTC

New packages created between 2026-10-23 07:20 UTC and 2026-10-23 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T08-19-58-293783Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 07:36:11 | [phasync/hooked](https://www.nuget.org/packages/phasync%2Fhooked) | v0.1.0 |  | Cooperative blocking PHP function replacements for phasync |
| 2026-10-23 07:39:44 | [phasync/plug](https://www.nuget.org/packages/phasync%2Fplug) | v0.1.0 |  | Translate whole PHP applications with phasync/babel so their blocking calls go… |
| 2026-10-23 07:49:59 | [symfony/ai-decision-platform](https://www.nuget.org/packages/symfony%2Fai-decision-platform) | v0.15.0 | Yoan Bernabeu; Symfony Commun… | Decision platform bridge for Symfony AI |
| 2026-10-23 08:03:21 | [digicademy/typo3-sentry-logs-writer](https://www.nuget.org/packages/digicademy%2Ftypo3-sentry-logs-writer) | 1.0.0 | Frodo Podschwadek | TYPO3 log writer that sends log Sentry Logs API. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
