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

## Latest list — 2026-11-01 17:18 UTC

New packages created between 2026-11-01 16:20 UTC and 2026-11-01 17:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T17-18-58-313411Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 16:33:25 | [zinxan/native-core](https://www.nuget.org/packages/zinxan%2Fnative-core) | v0.2.1 |  | The shared NativeWatch client that zinxan/native-desktop and zinxan/native-mobi… |
| 2026-11-01 16:35:38 | [zinxan/native-desktop](https://www.nuget.org/packages/zinxan%2Fnative-desktop) | v0.2.0 |  | Error tracking for NativePHP desktop apps, reported to NativeWatch. |
| 2026-11-01 16:35:39 | [zinxan/native-mobile](https://www.nuget.org/packages/zinxan%2Fnative-mobile) | v0.2.0 |  | Error tracking for NativePHP iOS and Android apps, reported to NativeWatch. |
| 2026-11-01 17:06:30 | [rapttor/yii2-feedback](https://www.nuget.org/packages/rapttor%2Fyii2-feedback) | v0.1.1 | Rapttor | Yii2 extension: a feedback widget (closable floating button, menu trigger) with… |
| 2026-11-01 17:16:18 | [awengan/hyperf-admin](https://www.nuget.org/packages/awengan%2Fhyperf-admin) | v0.0.1 | Awengan | Hyperf 3.1 后台面板组件：Vue 3 + Naive UI，原生 ESM 无构建，自带登录、RBAC、CRUD、审计日志 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
