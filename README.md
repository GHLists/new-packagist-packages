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

## Latest list — 2026-11-15 16:22 UTC

New packages created between 2026-11-15 15:19 UTC and 2026-11-15 16:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T16-22-01-653715Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 15:21:44 | [miraqceed/laravel-foundation](https://www.nuget.org/packages/miraqceed%2Flaravel-foundation) | v0.1.1 | MIRAQCEED | どの Laravel のアプリにも要る部品（テストの守り・CSV・ログインのロック・CSP・見張り） |
| 2026-11-15 15:32:25 | [samuel-olavo/laravel-xibo](https://www.nuget.org/packages/samuel-olavo%2Flaravel-xibo) | v0.1.0 |  | Laravel 13 client for the Xibo CMS API with multiple versioned connections |
| 2026-11-15 15:42:00 | [voku/agent-decision](https://www.nuget.org/packages/voku%2Fagent-decision) | 0.1.0 |  | Provider-neutral bounded decision advice with explicit human authority and priv… |
| 2026-11-15 15:48:33 | [mahoke/mijn-afvalwijzer](https://www.nuget.org/packages/mahoke%2Fmijn-afvalwijzer) | v0.1.0 |  | Dependency-free PHP scraper for MijnAfvalwijzer collection calendars. |
| 2026-11-15 16:07:24 | [ichinese/open-sdk](https://www.nuget.org/packages/ichinese%2Fopen-sdk) | v1.0.0-rc.8 |  | iChinese 开放平台 PHP 服务端 SDK |
| 2026-11-15 16:10:31 | [runconvert/runconvert-php](https://www.nuget.org/packages/runconvert%2Frunconvert-php) | v0.1.0 |  | Official RunConvert SDK for PHP: convert files between 240+ formats |
| 2026-11-15 16:11:28 | [runconvert/runconvert-laravel](https://www.nuget.org/packages/runconvert%2Frunconvert-laravel) | v0.1.0 |  | Official RunConvert SDK for Laravel: convert files between 240+ formats |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
