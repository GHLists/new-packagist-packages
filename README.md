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

## Latest list — 2026-11-23 18:20 UTC

New packages created between 2026-11-23 17:20 UTC and 2026-11-23 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T18-20-57-912973Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 17:30:15 | [klsoft/yii3-doctrine-app](https://www.nuget.org/packages/klsoft%2Fyii3-doctrine-app) | 1.0.0 |  | A Yii 3 web application template that supports the Doctrine ORM |
| 2026-11-23 17:39:17 | [ernestdefoe/duskline](https://www.nuget.org/packages/ernestdefoe%2Fduskline) | 1.0.0 | Ernestdefoe | Duskline: a gaming theme for Flarum 2. An illustrated neon coastal skyline whos… |
| 2026-11-23 17:45:16 | [creativefactoryrv/openai-conversions-api](https://www.nuget.org/packages/creativefactoryrv%2Fopenai-conversions-api) | v1.0.0 |  | Client PHP (PSR-18) per la Conversions API di OpenAI Ads: invio di eventi di co… |
| 2026-11-23 17:51:07 | [ismailnakkar/laravel-mail-content](https://www.nuget.org/packages/ismailnakkar%2Flaravel-mail-content) | v1.0.0 | Ismail Nakkar | The shared contract for package mail in Laravel: what a mail says, as ordered p… |
| 2026-11-23 18:05:45 | [adachsoft/codegen-file-list](https://www.nuget.org/packages/adachsoft%2Fcodegen-file-list) | v0.1.1 | Arkadiusz Adach | Execute ordered code-generation file operations with optional AI-assisted edits… |
| 2026-11-23 18:18:30 | [alibabacloud/qwenb2bchat-20261121](https://www.nuget.org/packages/alibabacloud%2Fqwenb2bchat-20261121) | 1.0.0 | Alibaba Cloud SDK | Alibaba Cloud QwenB2BChat (20261121) SDK Library for PHP |
| 2026-11-23 18:18:41 | [alibabacloud/qwenb2bmed-20261121](https://www.nuget.org/packages/alibabacloud%2Fqwenb2bmed-20261121) | 1.0.0 | Alibaba Cloud SDK | Alibaba Cloud QwenB2BMed (20261121) SDK Library for PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
