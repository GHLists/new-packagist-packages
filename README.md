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

## Latest list — 2026-10-07 21:19 UTC

New packages created between 2026-10-07 20:20 UTC and 2026-10-07 21:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T21-19-13-451494Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 20:43:14 | [ephraitech/ci4-auth](https://www.nuget.org/packages/ephraitech%2Fci4-auth) | v0.9.0 | Ephraitech Unified Solutions | DB-backed authentication (session + opaque token) and role/permission authoriza… |
| 2026-10-07 20:56:21 | [tsara/tsara-php](https://www.nuget.org/packages/tsara%2Ftsara-php) | v0.1.0 |  | Official server-side PHP SDK for Tsara. |
| 2026-10-07 21:04:30 | [azymuthia/turnstile-bundle](https://www.nuget.org/packages/azymuthia%2Fturnstile-bundle) | v0.1.0 | Bartosz Piotr Pazoła | Strict Cloudflare Turnstile verification for Symfony firewalls and forms, refus… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
