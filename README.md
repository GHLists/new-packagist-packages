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

## Latest list — 2026-10-15 10:23 UTC

New packages created between 2026-10-15 09:21 UTC and 2026-10-15 10:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T10-23-06-219188Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 09:25:41 | [zhangzhangzui/yii2-sms](https://www.nuget.org/packages/zhangzhangzui%2Fyii2-sms) | 1.0.0 | 张张嘴 | Yii2 多渠道短信组件 — 模板映射 + 自动 Failover + 回执回调 |
| 2026-10-15 09:37:51 | [testmonitor/eloquent-revisable](https://www.nuget.org/packages/testmonitor%2Feloquent-revisable) | v1.0.0 | Thijs Kok; Stephan Grootveld;… | A Laravel package to track revisions of Eloquent models, allowing you to easily… |
| 2026-10-15 09:38:49 | [deployecommerce/module-local-dev-tooling](https://www.nuget.org/packages/deployecommerce%2Fmodule-local-dev-tooling) | 0.0.1 |  | Local development tooling for Magento 2: admin auto-login, 2FA bypass and a fix… |
| 2026-10-15 09:52:48 | [multiplayer-gratis/api-client](https://www.nuget.org/packages/multiplayer-gratis%2Fapi-client) | v1.0.0 |  | PHP-Client für die REST-API von multiplayer.gratis – kostenloses Gameserver-Hos… |
| 2026-10-15 09:53:28 | [amrachraf6699/laravel-nplusone-scanner](https://www.nuget.org/packages/amrachraf6699%2Flaravel-nplusone-scanner) | v0.1.0 | Amr Achraf | A conservative static analyzer for potential Laravel N+1 query patterns. |
| 2026-10-15 09:59:02 | [confeature/confeature-php-sdk](https://www.nuget.org/packages/confeature%2Fconfeature-php-sdk) | v0.0.0 | MakerLabs | Name reserved for the Confeature PHP SDK (ConfigCat-compatible). The first real… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
