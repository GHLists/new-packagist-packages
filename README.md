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

## Latest list — 2026-10-10 14:22 UTC

New packages created between 2026-10-10 13:19 UTC and 2026-10-10 14:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T14-22-07-426371Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 13:32:21 | [hasan-deeba/larasaas](https://www.nuget.org/packages/hasan-deeba%2Flarasaas) | v1.0.0 |  | Drop-in SaaS engine for Laravel + React: Stripe billing (Cashier), config-drive… |
| 2026-10-10 13:33:53 | [avando/ave](https://www.nuget.org/packages/avando%2Fave) | 1.0.0 | Ulrich Braun | Avando AVE — theme framework for Contao 5.7 LTS and Contao 6 |
| 2026-10-10 13:42:07 | [trk/sulu-preline-blocks-bundle](https://www.nuget.org/packages/trk%2Fsulu-preline-blocks-bundle) | 1.0.0 | Iskender TOTOGLU | Preline UI component blocks and responsive templates for Sulu CMS |
| 2026-10-10 13:50:39 | [maxcuso/flarum-roleplay](https://www.nuget.org/packages/maxcuso%2Fflarum-roleplay) | v0.1.0 | maxcuso | Roleplaying characters and character applications for Flarum |
| 2026-10-10 13:53:19 | [tobento/app-backup](https://www.nuget.org/packages/tobento%2Fapp-backup) | 2.0 | Tobias Strub | A flexible backup and restore system with a web interface for Tobento applicati… |
| 2026-10-10 14:03:36 | [pivotphp/http](https://www.nuget.org/packages/pivotphp%2Fhttp) | v1.0.0 | Caio Alberto Fernandes | HTTP foundation for PivotPHP - PSR-7/PSR-17 messages built on nyholm/psr7 with… |
| 2026-10-10 14:05:23 | [roadrunner/lock](https://www.nuget.org/packages/roadrunner%2Flock) | 1.2.0 | Anton Titov; Pavel Buchnev; A… | Distributed locks for PHP applications backed by the RoadRunner lock plugin: ac… |
| 2026-10-10 14:08:17 | [roadrunner/grpc](https://www.nuget.org/packages/roadrunner%2Fgrpc) | 3.8.0 | Anton Titov; Pavel Buchnev; A… | gRPC server for PHP: serve gRPC services from RoadRunner PHP workers |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
