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

## Latest list — 2026-10-15 04:23 UTC

New packages created between 2026-10-15 03:22 UTC and 2026-10-15 04:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T04-23-11-708505Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 03:27:06 | [pieceofcake2/docs](https://www.nuget.org/packages/pieceofcake2%2Fdocs) | v2.0.0 |  | Markdown documentation of pieceofcake2/cakephp (CakePHP 2 fork), for reading lo… |
| 2026-10-15 03:42:31 | [ernestdefoe/depot](https://www.nuget.org/packages/ernestdefoe%2Fdepot) | v1.0.1 | Ernest Defoe | Depot — a downloads section for Flarum 2: files with versions and changelogs, c… |
| 2026-10-15 03:49:22 | [gold-api/sdk-php](https://www.nuget.org/packages/gold-api%2Fsdk-php) | v1.1.0 | GoldAPI | GoldAPI (gold-api.cn) 贵金属行情 PHP SDK —— 黄金/白银/铂金/钯金等 70+ 品种实时行情，一次请求最多批量 50 个品种 |
| 2026-10-15 03:49:40 | [magezon/module-simple-builder](https://www.nuget.org/packages/magezon%2Fmodule-simple-builder) | 1.0.7 |  |  |
| 2026-10-15 04:11:29 | [envoylope/amqp-sqs-driver](https://www.nuget.org/packages/envoylope%2Famqp-sqs-driver) | v0.1.0 |  | AWS SQS driver for PHP AMQP-Compat |
| 2026-10-15 04:19:16 | [filagora/filagora-messages](https://www.nuget.org/packages/filagora%2Ffilagora-messages) | v0.1.0 |  | Private conversations between members, with folders, read state and trash, for… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
