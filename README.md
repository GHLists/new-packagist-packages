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

## Latest list — 2026-11-13 16:22 UTC

New packages created between 2026-11-13 15:19 UTC and 2026-11-13 16:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T16-22-20-502865Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 15:26:47 | [pharaonic/laravel-ratings](https://www.nuget.org/packages/pharaonic%2Flaravel-ratings) | 13.0.0 | Moamen Eltouny (Raggi) | Polymorphic ratings for Laravel Eloquent models: one rating per rater and targe… |
| 2026-11-13 15:26:49 | [tornado-engine/access](https://www.nuget.org/packages/tornado-engine%2Faccess) | v0.1.0 |  | Tornado Engine core-module: users, roles, and which pages each person can see. |
| 2026-11-13 15:47:45 | [ernestdefoe/homecoming](https://www.nuget.org/packages/ernestdefoe%2Fhomecoming) | 1.0.0 | Ernest Defoe | Homecoming: a welcome-back dashboard for your members. A greeting with the loca… |
| 2026-11-13 15:52:05 | [youvision/think-store](https://www.nuget.org/packages/youvision%2Fthink-store) | v1.2 | indiboy-create; AI | ThinkPHP 8 商店扩展：查询主项目中已安装的 think-store-* 发布包。 |
| 2026-11-13 15:54:33 | [wwwision/subscription-engine-worker](https://www.nuget.org/packages/wwwision%2Fsubscription-engine-worker) | 1.0.0 | Bastian Waidelich | Long-running worker loop for the wwwision/subscription-engine |
| 2026-11-13 16:01:06 | [hardcastle/ledger-direct-interledger](https://www.nuget.org/packages/hardcastle%2Fledger-direct-interledger) | 0.1.0 | Alexander Busse | LedgerDirect for Interledger - accepts Open Payments incoming payments as a Led… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
