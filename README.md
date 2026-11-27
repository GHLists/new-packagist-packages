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

## Latest list — 2026-11-27 12:21 UTC

New packages created between 2026-11-27 11:19 UTC and 2026-11-27 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T12-21-55-128534Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 11:22:35 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.55.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-27 11:26:04 | [sendrail/laravel](https://www.nuget.org/packages/sendrail%2Flaravel) | v0.1.0 | Sendrail | Laravel integration for Sendrail, the Czech SMS API: facade, notification chann… |
| 2026-11-27 11:26:04 | [sendrail/nette](https://www.nuget.org/packages/sendrail%2Fnette) | v0.1.0 | Sendrail | Nette DI extension for Sendrail, the Czech SMS API: the client and the webhook… |
| 2026-11-27 11:26:04 | [sendrail/sendrail-php](https://www.nuget.org/packages/sendrail%2Fsendrail-php) | v0.1.0 | Sendrail | Official PHP SDK for Sendrail, the Czech SMS API: send SMS and verification cod… |
| 2026-11-27 11:27:28 | [dskripchenko/laravel-standards](https://www.nuget.org/packages/dskripchenko%2Flaravel-standards) | v1.0.0 | Denis Skripchenko | Source of truth for PHP, Laravel and Vue projects: coding style, architecture,… |
| 2026-11-27 11:42:46 | [mindvoice-pro/sdk](https://www.nuget.org/packages/mindvoice-pro%2Fsdk) | v0.1.0 |  | PHP-клиент публичного API MindVoice для API-ключей Workspace. |
| 2026-11-27 11:47:48 | [mignuti/typo3-chatbot](https://www.nuget.org/packages/mignuti%2Ftypo3-chatbot) | v1.1.2 | Mignuti Media | Mignuti Chatbot - AI chatbot for TYPO3, trained on your own content. Adds the c… |
| 2026-11-27 11:48:45 | [yii2-extensions/soft-delete](https://www.nuget.org/packages/yii2-extensions%2Fsoft-delete) | 0.1.0 |  | Soft deletion and restoration for Yii2 ActiveRecord |
| 2026-11-27 12:00:59 | [presentkim/library-name](https://www.nuget.org/packages/presentkim%2Flibrary-name) | 0.1.0 |  | Virtual inventory menus (entity containers) for axolotl-pm/PocketMine-MP |
| 2026-11-27 12:17:13 | [yireo/magento2-clean-admin-menu](https://www.nuget.org/packages/yireo%2Fmagento2-clean-admin-menu) | 1.0.0 |  | N/A |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
