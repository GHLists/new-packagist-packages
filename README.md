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

## Latest list — 2026-10-04 05:19 UTC

New packages created between 2026-10-04 04:21 UTC and 2026-10-04 05:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T05-19-09-916213Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 04:28:21 | [kopaing/laravel-cloudflare-kv](https://www.nuget.org/packages/kopaing%2Flaravel-cloudflare-kv) | v1.0.0 | kopaing | A Laravel cache store backed by Cloudflare Workers KV, with honest semantics fo… |
| 2026-10-04 05:10:30 | [patterns/guard](https://www.nuget.org/packages/patterns%2Fguard) | v1.0.0 |  | Guard pattern - validate inputs and preconditions early, returning a Result ins… |
| 2026-10-04 05:15:20 | [patterns/value-object](https://www.nuget.org/packages/patterns%2Fvalue-object) | v1.0.0 |  | Value Object pattern - immutable, self-validating domain objects that compare b… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
