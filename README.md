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

## Latest list — 2026-09-30 17:22 UTC

New packages created between 2026-09-30 16:19 UTC and 2026-09-30 17:22 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T17-22-31-2546Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 16:31:21 | [monty7352/quick-activity-log](https://www.nuget.org/packages/monty7352%2Fquick-activity-log) | v1.0.0 | Your Name | A lightweight activity logger for Laravel Eloquent models. |
| 2026-09-30 16:33:33 | [arnauddelgerie/tfs-app-bundle](https://www.nuget.org/packages/arnauddelgerie%2Ftfs-app-bundle) | v0.1.0 | Arnaud Delgerie | Symfony bundle for apps run by TFSAppHub, a host that installs and runs Symfony… |
| 2026-09-30 16:34:08 | [webx-ui/module-catalog-properties](https://www.nuget.org/packages/webx-ui%2Fmodule-catalog-properties) | v0.54.0 | WebX UI | Properties of products for the WebX UI catalogue: reference books, numbers, tex… |
| 2026-09-30 16:50:33 | [alies-dev/psalm-plugin-pest](https://www.nuget.org/packages/alies-dev%2Fpsalm-plugin-pest) | 0.1.0 | Alies Lapatsin | Psalm plugin for Pest: types $this in test closures as the configured TestCase… |
| 2026-09-30 16:58:19 | [webware/webware-phpdb](https://www.nuget.org/packages/webware%2Fwebware-phpdb) | 1.0.0-alpha.1 | Joey Smith | PhpDb bridge for the Webware stack: shadows the PhpDb root namespace so package… |
| 2026-09-30 17:03:51 | [heyosseus/phpstan-sloppy](https://www.nuget.org/packages/heyosseus%2Fphpstan-sloppy) | v1.0.0 | heyosseus | Sloppy's rules inside your PHPStan run: swallowed exceptions, god methods, N+1… |
| 2026-09-30 17:06:16 | [pokerprovide/sdk](https://www.nuget.org/packages/pokerprovide%2Fsdk) | v1.0.0 |  | Official PokerProvide Poker-as-a-Service SDK for PHP |
| 2026-09-30 17:11:51 | [sympress/qa](https://www.nuget.org/packages/sympress%2Fqa) | 0.1.0 | Brian Schaffner | Shared QA tooling for SymPress packages. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
