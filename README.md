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

## Latest list — 2026-11-04 02:20 UTC

New packages created between 2026-11-04 01:19 UTC and 2026-11-04 02:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T02-20-26-753888Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 01:30:48 | [jeffersongoncalves/kv-cli](https://www.nuget.org/packages/jeffersongoncalves%2Fkv-cli) | 1.1.0 | Jefferson Goncalves | Read-only CLI to inspect Redis (keys, values of any type, INFO) through named c… |
| 2026-11-04 01:42:53 | [mzm/mydigitalid](https://www.nuget.org/packages/mzm%2Fmydigitalid) | v1.2.0 |  | MyDigital ID (MIMOS/Keycloak OpenID Connect) SSO login integration for Laravel… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
