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

## Latest list — 2026-11-06 17:21 UTC

New packages created between 2026-11-06 16:21 UTC and 2026-11-06 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T17-21-48-510915Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 16:22:58 | [janalis/porta-phpunit](https://www.nuget.org/packages/janalis%2Fporta-phpunit) | v0.1.4 |  | Runs PHPUnit tests from the editor: the test at the caret, the file, the suite,… |
| 2026-11-06 16:44:12 | [uni-method/frame](https://www.nuget.org/packages/uni-method%2Fframe) | 1.0.0 | Alexander Kompaneytsev | Declarative REST API layer for PHP: a config describes models, relations and ac… |
| 2026-11-06 16:49:21 | [afropin/afropin-php](https://www.nuget.org/packages/afropin%2Fafropin-php) | v1.0.0 | AfroPin Software Limited | PHP library for the AfroPin gift card API: sell, top up and redeem PINs, quotes… |
| 2026-11-06 17:02:08 | [uni-method/symfony-lib](https://www.nuget.org/packages/uni-method%2Fsymfony-lib) | 1.0.0 | Alexander Kompaneytsev | Symfony bundle for UniMethod Frame: turns a declarative config into a REST API… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
