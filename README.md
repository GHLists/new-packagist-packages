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

## Latest list — 2026-10-25 08:21 UTC

New packages created between 2026-10-25 07:21 UTC and 2026-10-25 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T08-21-06-028958Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 07:23:48 | [teamones/tencentcloud-common](https://www.nuget.org/packages/teamones%2Ftencentcloud-common) | 3.0.0 | tencentcloudapi | TencentCloudApi php sdk |
| 2026-10-25 07:30:14 | [adamczykpiotr/laravel-ultimate-formatter](https://www.nuget.org/packages/adamczykpiotr%2Flaravel-ultimate-formatter) | v1.1.0 | Piotr Adamczyk | Ultimate code formatter for Laravel, taking care of everything |
| 2026-10-25 07:32:30 | [tacraft-sociality/flarum-onebot-notify](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-onebot-notify) | v1.0.0 | TaCraft-Sociality | Send OneBot (QQ) notifications about new discussions and posts from Flarum |
| 2026-10-25 07:42:48 | [t-labs-co/command-scheduler](https://www.nuget.org/packages/t-labs-co%2Fcommand-scheduler) | 1.0.0 | Ty Huynh | Code-first command scheduling framework for Laravel — discover schedulable comm… |
| 2026-10-25 07:46:18 | [rokastudio/racin](https://www.nuget.org/packages/rokastudio%2Fracin) | v1.2.1 | Roka Studio | A small, fast PHP 8.3+ framework for JSON APIs: Rails-style controllers and gen… |
| 2026-10-25 07:57:24 | [habeuk/symfony-starter](https://www.nuget.org/packages/habeuk%2Fsymfony-starter) | 1.0.1 |  | Starter Symfony 8.1 pour mes projets (API + JWT + Mailer + AI) |
| 2026-10-25 08:02:39 | [nextmail/sdk](https://www.nuget.org/packages/nextmail%2Fsdk) | v0.0.1 | Nextmail | The official PHP SDK for the Nextmail API. Send email and broadcasts, work with… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
