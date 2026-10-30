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

## Latest list — 2026-10-30 06:20 UTC

New packages created between 2026-10-30 05:21 UTC and 2026-10-30 06:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T06-20-06-924969Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 05:39:08 | [hospodskej-cz/eet-gateway-client](https://www.nuget.org/packages/hospodskej-cz%2Feet-gateway-client) | v0.1.0 |  | Typed PHP client for the EET Gateway HTTP API v1 (Czech EET 2.0). ext-curl, no… |
| 2026-10-30 06:08:24 | [idbi/blackbox](https://www.nuget.org/packages/idbi%2Fblackbox) | v1.0.0 |  | Request tracing and audit trail for Laravel: request id, client session, who, p… |
| 2026-10-30 06:16:12 | [tacraft-sociality/flarum-blessing-oauth](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-blessing-oauth) | 1.0.0 |  | Blessing Skin / TcsSkin OAuth2 login for Flarum 2. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
