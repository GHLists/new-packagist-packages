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

## Latest list — 2026-11-27 07:20 UTC

New packages created between 2026-11-27 06:22 UTC and 2026-11-27 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T07-20-13-344962Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 06:23:47 | [longquan/easy-umspay](https://www.nuget.org/packages/longquan%2Feasy-umspay) | 1.0.0 | Lonquan | 银联商务UMS支付PHP SDK - 支持自助签约和新购物车支付 |
| 2026-11-27 06:25:23 | [qiick/laravel-mcp-oauth](https://www.nuget.org/packages/qiick%2Flaravel-mcp-oauth) | v1.0.0-beta.1 | Qiick | OAuth authorization server for laravel/mcp endpoints in qiick Laravel products. |
| 2026-11-27 06:44:10 | [longquan/easy-mqtt](https://www.nuget.org/packages/longquan%2Feasy-mqtt) | 1.0.0 | lonquan | 基于 php-mqtt/client 的 Laravel MQTT Factory |
| 2026-11-27 06:46:21 | [rapttor/yii2-glass](https://www.nuget.org/packages/rapttor%2Fyii2-glass) | v1.0.0 |  | The Rapttor glass UI for Yii2: refractive glass app shell, Vue components, pane… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
