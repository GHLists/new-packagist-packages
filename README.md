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

## Latest list — 2026-11-11 10:21 UTC

New packages created between 2026-11-11 09:21 UTC and 2026-11-11 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T10-21-37-923808Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 09:37:06 | [terbora/openpgp](https://www.nuget.org/packages/terbora%2Fopenpgp) | v1.0 | Nguyen Van Nguyen; Iliya Bazl… | Terbora OpenPGP - A modern, PHP-native implementation of the OpenPGP standard (… |
| 2026-11-11 09:39:36 | [cardee/smsc-ru](https://www.nuget.org/packages/cardee%2Fsmsc-ru) | v3.7.1 | Sergei Gruzdov | SmscRu notifications channel for Laravel 5.3+ |
| 2026-11-11 09:45:18 | [jvh/nk-legpuzzelen-bundle](https://www.nuget.org/packages/jvh%2Fnk-legpuzzelen-bundle) | 1.0.2 |  | Customisations for NK Legpuzzelen. |
| 2026-11-11 09:53:38 | [contashare/socialite](https://www.nuget.org/packages/contashare%2Fsocialite) | v0.1.0 |  | Sign in with ContaShare for Laravel Socialite, plus a checker for ContaShare we… |
| 2026-11-11 10:06:24 | [subarist/waterhole-user-card](https://www.nuget.org/packages/subarist%2Fwaterhole-user-card) | v1.0.0 |  | Compact hover user cards for Waterhole |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
