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

## Latest list — 2026-10-21 18:19 UTC

New packages created between 2026-10-21 17:20 UTC and 2026-10-21 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T18-19-53-708626Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 17:35:28 | [codex-team/kohana-aliases](https://www.nuget.org/packages/codex-team%2Fkohana-aliases) | v1.0.0 |  | This module allows you to make usefull and beautifull URLs for your service. |
| 2026-10-21 17:48:23 | [supseven/opinion](https://www.nuget.org/packages/supseven%2Fopinion) | v1.0.0 | Volker Kemeter | Collects feedback from editors including a screenshot and environment details a… |
| 2026-10-21 17:48:23 | [vkemeter/opinion](https://www.nuget.org/packages/vkemeter%2Fopinion) | v1.0.0 | Volker Kemeter | Collects feedback from editors including a screenshot and environment details a… |
| 2026-10-21 18:01:56 | [amjadiqbal/laravel-webpush-kit](https://www.nuget.org/packages/amjadiqbal%2Flaravel-webpush-kit) | v0.1.0 | Amjad Iqbal | The browser side of Laravel web push notifications for laravel-notification-cha… |
| 2026-10-21 18:12:34 | [amjadiqbal/laravel-redis-advisor](https://www.nuget.org/packages/amjadiqbal%2Flaravel-redis-advisor) | v0.1.0 | Amjad Iqbal | Read-only Redis and Valkey health advisor for Laravel: finds queues that can si… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
