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

## Latest list — 2026-10-09 03:18 UTC

New packages created between 2026-10-09 02:19 UTC and 2026-10-09 03:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T03-18-53-555197Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 02:42:41 | [jeffersongoncalves/filament-security-headers](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-security-headers) | 3.0.0 | Jefferson Gonçalves | Filament settings page for laravel-security-headers: edit the Content Security… |
| 2026-10-09 02:48:17 | [phpgo/hyperf-logging](https://www.nuget.org/packages/phpgo%2Fhyperf-logging) | v0.1.0 |  | Hyperf 3.1 adapters for execution-scoped structured logging. |
| 2026-10-09 02:48:17 | [phpgo/logging](https://www.nuget.org/packages/phpgo%2Flogging) | v0.1.0 |  | Execution-scoped structured logging for PHP and Monolog. |
| 2026-10-09 02:57:56 | [pivotphp/skeleton](https://www.nuget.org/packages/pivotphp%2Fskeleton) | v1.1.0 | PivotPHP Team | Skeleton project for PivotPHP v2.2.0 - The evolutionary PHP microframework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
