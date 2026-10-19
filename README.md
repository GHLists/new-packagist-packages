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

## Latest list — 2026-10-19 08:22 UTC

New packages created between 2026-10-19 07:23 UTC and 2026-10-19 08:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T08-22-16-592355Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 07:32:06 | [sgoranov/oauth2-openid-connect-server](https://www.nuget.org/packages/sgoranov%2Foauth2-openid-connect-server) | 1.0.2 | Goranov; Steve Rhoades | An OpenID Connect Server built on The PHP League's OAuth2 Server |
| 2026-10-19 07:36:21 | [hideinmatrix/flarum-telegram-upload](https://www.nuget.org/packages/hideinmatrix%2Fflarum-telegram-upload) | v0.1.0 | HideInMatrix | Telegram attachment storage for Flarum 2.x through FoF Upload and tg-disk. |
| 2026-10-19 07:37:04 | [guavas/guavas](https://www.nuget.org/packages/guavas%2Fguavas) | v0.1.0 |  | Kerangka proyek aplikasi Guavas |
| 2026-10-19 07:38:46 | [programmernomad/laracorekit](https://www.nuget.org/packages/programmernomad%2Flaracorekit) | v0.1.0 | ProgrammerNomad | Modular Laravel application foundation with Filament administration, authentica… |
| 2026-10-19 07:48:51 | [amarenkov/laravel-mutable-content-ai](https://www.nuget.org/packages/amarenkov%2Flaravel-mutable-content-ai) | v0.1.0 | Alexey Marenkov | AI agents for laravel-mutable-content apps: long-term memory and a run journal… |
| 2026-10-19 07:49:00 | [darvis/bullhorn-api](https://www.nuget.org/packages/darvis%2Fbullhorn-api) | v1.1.0 | Arvid de Jong | PHP client for the Bullhorn REST API (staffing and recruitment CRM): OAuth logi… |
| 2026-10-19 08:12:52 | [wexample/symfony-analytics](https://www.nuget.org/packages/wexample%2Fsymfony-analytics) | 1.0.1 |  |  |
| 2026-10-19 08:13:53 | [wexample/symfony-analytics-ds](https://www.nuget.org/packages/wexample%2Fsymfony-analytics-ds) | 1.0.1 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
