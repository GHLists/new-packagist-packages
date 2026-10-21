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

## Latest list — 2026-10-21 14:22 UTC

New packages created between 2026-10-21 13:21 UTC and 2026-10-21 14:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T14-22-54-405421Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 13:25:18 | [etfusion/vari-php-sdk](https://www.nuget.org/packages/etfusion%2Fvari-php-sdk) | v1.0.2 |  | PHP SDK for the V-ARI Stable API (mutual TLS): identity, certificate rotation,… |
| 2026-10-21 13:26:04 | [contenir-extension/formbuilder](https://www.nuget.org/packages/contenir-extension%2Fformbuilder) | v0.1.0 |  | The form builder module for Contenir CMS: the Forms area, with forms, fields, n… |
| 2026-10-21 13:32:57 | [kolossusai/chat-laravel](https://www.nuget.org/packages/kolossusai%2Fchat-laravel) | v1.0.0 | Kolossus AI | Add a KolossusAI chat assistant to your Laravel site with one command. |
| 2026-10-21 13:56:56 | [besnovatyj/yii2-cms-quicktickets](https://www.nuget.org/packages/besnovatyj%2Fyii2-cms-quicktickets) | v1.0.0 | Besnovatyj | Интеграция с API Афиша сервиса Quick Tickets для Yii2 CMS: кеш ответов, журнал… |
| 2026-10-21 14:10:41 | [keel/framework](https://www.nuget.org/packages/keel%2Fframework) | v0.1.0 |  | Worker-first PHP micro-framework: PSR stack, attribute routing, compiled contai… |
| 2026-10-21 14:14:02 | [ernestdefoe/pigeonhole](https://www.nuget.org/packages/ernestdefoe%2Fpigeonhole) | v1.0.0 | Ernest Defoe | Folders for Flarum's private messages. Each member files their own conversation… |
| 2026-10-21 14:16:22 | [ernestdefoe/detour](https://www.nuget.org/packages/ernestdefoe%2Fdetour) | 1.0.0 | Ernest Defoe | A 404 log and redirect manager for Flarum: see which addresses visitors hit tha… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
