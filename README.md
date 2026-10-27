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

## Latest list — 2026-10-27 10:21 UTC

New packages created between 2026-10-27 09:22 UTC and 2026-10-27 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T10-21-44-649487Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 09:32:32 | [lasselehtinen/healthchecks-helper](https://www.nuget.org/packages/lasselehtinen%2Fhealthchecks-helper) | v1.0.0 | Lasse Lehtinen | Ping Healthchecks.io from the Laravel scheduler with a single method call |
| 2026-10-27 09:37:09 | [big-bang-notify/sdk](https://www.nuget.org/packages/big-bang-notify%2Fsdk) | v0.1.0 |  | Standalone PHP client for Big Bang Notify notifications addressed by Telegram u… |
| 2026-10-27 09:44:59 | [keytd/manat](https://www.nuget.org/packages/keytd%2Fmanat) | v0.1.0 | KeyTD | One API for Azerbaijani online payment providers. |
| 2026-10-27 10:07:07 | [php-forge/diff](https://www.nuget.org/packages/php-forge%2Fdiff) | 0.1.0 | Wilmer Arambula | Git-compatible line diff for PHP: a port of Git's xdiff Myers pipeline with the… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
