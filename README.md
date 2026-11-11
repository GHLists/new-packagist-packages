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

## Latest list — 2026-11-11 16:20 UTC

New packages created between 2026-11-11 15:19 UTC and 2026-11-11 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T16-20-33-60459Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 15:29:25 | [logipro/system-learning-php](https://www.nuget.org/packages/logipro%2Fsystem-learning-php) | v0.1.0 | Frédéric Royet | PHP client for the System Learning REST API (`/api/system`) |
| 2026-11-11 15:32:34 | [logipro/idcommerce-php](https://www.nuget.org/packages/logipro%2Fidcommerce-php) | v0.1.0 | Frédéric Royet | PHP client for the ID-Commerce REST API (`/api/idcommerce`) |
| 2026-11-11 15:34:58 | [sandermuller/rector-preset](https://www.nuget.org/packages/sandermuller%2Frector-preset) | v2.8.0 | Sander Muller | Shared Rector presets for apps and packages, versioned with Rector. |
| 2026-11-11 15:35:06 | [netresearch/typo3-ai-edition](https://www.nuget.org/packages/netresearch%2Ftypo3-ai-edition) | v1.0.0 | Netresearch DTT GmbH | TYPO3 AI Edition: installs the Netresearch AI extensions for TYPO3 in versions… |
| 2026-11-11 15:43:37 | [nowo-tech/api-token-bundle](https://www.nuget.org/packages/nowo-tech%2Fapi-token-bundle) | v0.1.0 | Héctor Franco Aceituno; Nowo.… | Personal API tokens for Symfony: hashed lookup tokens with per-module grants, a… |
| 2026-11-11 15:44:45 | [bastihilger/simple-statamic-translations](https://www.nuget.org/packages/bastihilger%2Fsimple-statamic-translations) | v0.1.0 | Sebastian Hilger | Translate Statamic content without multi-site: a "Translated" field that wraps… |
| 2026-11-11 15:47:54 | [owlframework/core](https://www.nuget.org/packages/owlframework%2Fcore) | v1.0.0 | Emmanuel Austin | A lightweight custom PHP MVC framework |
| 2026-11-11 16:08:18 | [zero1/optimization-metapackage](https://www.nuget.org/packages/zero1%2Foptimization-metapackage) | 1.0.0 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
