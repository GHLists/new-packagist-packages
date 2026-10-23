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

## Latest list — 2026-10-23 04:21 UTC

New packages created between 2026-10-23 03:20 UTC and 2026-10-23 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T04-21-42-448072Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 03:41:34 | [morisawa_kana/laravel-repository](https://www.nuget.org/packages/morisawa_kana%2Flaravel-repository) | v1.0.0 | morisawa_kana | Laravel - Repositories to the database layer |
| 2026-10-23 03:47:51 | [fast-cmf/vue-admin-starter](https://www.nuget.org/packages/fast-cmf%2Fvue-admin-starter) | v1.0.0 |  | Laravel 13 + Vue 3 后台管理启动模板：RBAC 权限、菜单管理、媒体中心、操作日志开箱即用。 |
| 2026-10-23 03:57:54 | [larva/laravel-ai-volc](https://www.nuget.org/packages/larva%2Flaravel-ai-volc) | 1.0.0 | Larva Team | Volcengine Ark (火山方舟) provider for Laravel AI: text, embeddings, TTS, Seedream… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
