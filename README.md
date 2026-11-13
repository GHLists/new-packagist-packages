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

## Latest list — 2026-11-13 19:21 UTC

New packages created between 2026-11-13 18:19 UTC and 2026-11-13 19:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T19-21-06-078614Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 18:22:47 | [routewise/laravel](https://www.nuget.org/packages/routewise%2Flaravel) | v0.1.0 | Mohab Mamdouh | Turn a Laravel app into a safe MCP server: tools defined as data or generated f… |
| 2026-11-13 18:42:52 | [woomoza/mozesms-php](https://www.nuget.org/packages/woomoza%2Fmozesms-php) | v1.0.1 |  | SDK oficial PHP da API MozeSMS (SMS, OTP, saldo, webhooks) |
| 2026-11-13 18:53:48 | [youvision/think-store-weather](https://www.nuget.org/packages/youvision%2Fthink-store-weather) | v1.5 | Youvision | ThinkPHP 8 天气查询组件：省市联动、上游天气 JSON 接口与 8 小时缓存。 |
| 2026-11-13 18:53:49 | [ernestdefoe/helpdesk](https://www.nuget.org/packages/ernestdefoe%2Fhelpdesk) | 1.0.0 | Ernestdefoe | Help Desk — a search-first support theme for Flarum 2. A big search hero, topic… |
| 2026-11-13 19:01:40 | [jonatasfenske/cropper](https://www.nuget.org/packages/jonatasfenske%2Fcropper) | v1.0.0 | Robson V. Leite; Jonatas Fens… | Crop inteligente de imagens PHP 8.5 com Focal Point, suporte AVIF/WebP nativo,… |
| 2026-11-13 19:01:41 | [jonatasfenske/validator](https://www.nuget.org/packages/jonatasfenske%2Fvalidator) | v1.0.0 | Robson V. Leite; Jonatas Fens… | Validação declarativa PHP 8.5 com 30+ rules, mensagens em português, regras cus… |
| 2026-11-13 19:13:40 | [ernestdefoe/hearth](https://www.nuget.org/packages/ernestdefoe%2Fhearth) | 1.0.0 | Ernestdefoe | Hearth — a warm, cozy theme for small hobby communities on Flarum 2. Paper tone… |
| 2026-11-13 19:16:24 | [dotenvx/phpdotenvx](https://www.nuget.org/packages/dotenvx%2Fphpdotenvx) | v0.1.5 | dotenv | a secure dotenv—from the creator of `dotenv` |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
