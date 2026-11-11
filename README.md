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

## Latest list — 2026-11-11 18:19 UTC

New packages created between 2026-11-11 17:19 UTC and 2026-11-11 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T18-19-55-54487Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 17:20:40 | [alibabacloud/ecdbiz-20240929](https://www.nuget.org/packages/alibabacloud%2Fecdbiz-20240929) | 1.0.0 | Alibaba Cloud SDK | Alibaba Cloud EcdBiz (20240929) SDK Library for PHP |
| 2026-11-11 17:25:33 | [marcelofecchio/vipp-php-sdk](https://www.nuget.org/packages/marcelofecchio%2Fvipp-php-sdk) | v0.1.0 | Marcelo Fecchio | SDK PHP 8.4 para o Web Service de Postagem do ViPP (VisualSet), com integração… |
| 2026-11-11 17:28:44 | [artaskynet/id](https://www.nuget.org/packages/artaskynet%2Fid) | 0.0.2 | Sergey Serov |  |
| 2026-11-11 17:31:54 | [mannydmorales/application](https://www.nuget.org/packages/mannydmorales%2Fapplication) | v2.0.0 | Manny Morales | PHP library for Applications. |
| 2026-11-11 17:43:13 | [citadel/wiki-plugin](https://www.nuget.org/packages/citadel%2Fwiki-plugin) | 1.0.0 | Oscar Ellis | Wiki plugin for forumify |
| 2026-11-11 17:52:15 | [pasak-dev/secure-monitor](https://www.nuget.org/packages/pasak-dev%2Fsecure-monitor) | v1.0.0 | Roby; pasak-dev | Pasak - enterprise-grade headless self-hosted WAF, threat detection engine, zer… |
| 2026-11-11 17:52:30 | [yurkovskiy/laravel-partitions](https://www.nuget.org/packages/yurkovskiy%2Flaravel-partitions) | v0.1.1 | Max Yurkovskiy | Flexible MySQL partition management for Laravel: RANGE partitions by day/week/m… |
| 2026-11-11 18:04:56 | [adachsoft/phpstan-runner-lib](https://www.nuget.org/packages/adachsoft%2Fphpstan-runner-lib) | v0.1.0 |  | Run PHPStan from PHP and parse its JSON output into structured result DTOs. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
