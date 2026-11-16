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

## Latest list — 2026-11-16 00:22 UTC

New packages created between 2026-11-15 23:21 UTC and 2026-11-16 00:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T00-22-23-332424Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 23:47:46 | [ernestdefoe/glimpse](https://www.nuget.org/packages/ernestdefoe%2Fglimpse) | 1.0.0 | Ernest Defoe | Glimpse: Stories for Flarum. Short photo, video and text posts that disappear a… |
| 2026-11-16 00:04:37 | [sailantis/azera-aop](https://www.nuget.org/packages/sailantis%2Fazera-aop) | v0.4.2 | Sailantis | AOP companion for the Azera framework: additional advice attributes and interce… |
| 2026-11-16 00:04:39 | [sailantis/azera-auth](https://www.nuget.org/packages/sailantis%2Fazera-auth) | v0.4.2 | Sailantis | Authentication companion for the Azera framework: guards (session, token, JWT,… |
| 2026-11-16 00:04:42 | [sailantis/azera-cache](https://www.nuget.org/packages/sailantis%2Fazera-cache) | v0.4.2 | Sailantis | Cache companion for the Azera framework: production-grade PSR-16 backends (Redi… |
| 2026-11-16 00:04:42 | [sailantis/azera-log](https://www.nuget.org/packages/sailantis%2Fazera-log) | v0.4.2 | Sailantis | Logging companion for the Azera framework: Monolog-based logging with Azera-spe… |
| 2026-11-16 00:04:45 | [sailantis/azera-queue](https://www.nuget.org/packages/sailantis%2Fazera-queue) | v0.4.2 | Sailantis | Queue companion for the Azera framework: async backends (database, Redis, AMQP)… |
| 2026-11-16 00:05:07 | [oneverse/lazers](https://www.nuget.org/packages/oneverse%2Flazers) | v0.1.0 | Emmanuel Ilori | Server-side PHP SDK for Lazers Signal Protocol v1 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
