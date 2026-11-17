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

## Latest list — 2026-11-17 23:21 UTC

New packages created between 2026-11-17 22:21 UTC and 2026-11-17 23:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T23-21-18-850913Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 22:24:24 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.33.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-17 22:31:55 | [samjuk/dev-standards](https://www.nuget.org/packages/samjuk%2Fdev-standards) | v1.0.0 |  | Shared git hooks, commit rules and QA config for Magento, Laravel, Node and oth… |
| 2026-11-17 22:32:08 | [sirthxalot/symfoniq](https://www.nuget.org/packages/sirthxalot%2Fsymfoniq) | v1.0.1 | Alexander Bösch | A demonstration web application based on the Symfony PHP framework following be… |
| 2026-11-17 22:38:16 | [nubo-db/dynoxide-laravel](https://www.nuget.org/packages/nubo-db%2Fdynoxide-laravel) | v1.0.1 |  | Run Laravel's DynamoDB cache, sessions and failed jobs against Dynoxide in test… |
| 2026-11-17 22:46:48 | [xefi/faker-php-locales-de-ch](https://www.nuget.org/packages/xefi%2Ffaker-php-locales-de-ch) | v1.0.0 | Martin Soenen | Faker extension to include de_CH locale |
| 2026-11-17 22:50:31 | [orboni/orboni-php](https://www.nuget.org/packages/orboni%2Forboni-php) | v1.0.0 | Orboni | Orboni's API for PHP: crypto payments (USDT, USDC, BTC and more) paid straight… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
