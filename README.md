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

## Latest list — 2026-11-10 22:21 UTC

New packages created between 2026-11-10 21:22 UTC and 2026-11-10 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T22-21-06-803299Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 21:30:26 | [mannydmorales/system](https://www.nuget.org/packages/mannydmorales%2Fsystem) | v2.0.0 | Manny Morales | PHP library for the host system. |
| 2026-11-10 21:31:44 | [fernandoebert/valet-linux-plus](https://www.nuget.org/packages/fernandoebert%2Fvalet-linux-plus) | 2.1.0 | Uttam Rabadiya; Divyank Munja… | Advanced local development experience for Linux. |
| 2026-11-10 21:35:44 | [themusicdev/redis-acl](https://www.nuget.org/packages/themusicdev%2Fredis-acl) | 1.0.1 | TheMusicDev | CakePHP 5 plugin: a RedisEngine subclass that authenticates as a Redis 6 ACL us… |
| 2026-11-10 21:43:23 | [uams-web/patches-pest-plugin-mutate](https://www.nuget.org/packages/uams-web%2Fpatches-pest-plugin-mutate) | v1.0.0 |  | Patches UAMS-Web repositories apply to pestphp/pest-plugin-mutate |
| 2026-11-10 21:50:49 | [ernestdefoe/kudos](https://www.nuget.org/packages/ernestdefoe%2Fkudos) | 1.0.0 | Ernest Defoe | Kudos Wall: members thank each other with a few kudos cards a week. A wall of t… |
| 2026-11-10 22:11:04 | [solvebeam/twinfield](https://www.nuget.org/packages/solvebeam%2Ftwinfield) | v0.1.0 | Remco Tolsma | Modern PHP SDK for the Twinfield API |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
