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

## Latest list — 2026-11-24 02:20 UTC

New packages created between 2026-11-24 01:21 UTC and 2026-11-24 02:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T02-20-13-0131Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 01:28:29 | [pushinbr/nimbus-rector](https://www.nuget.org/packages/pushinbr%2Fnimbus-rector) | v0.1.0 |  | Rector rules that rewrite the mechanical parts of a Laravel application for Nim… |
| 2026-11-24 01:42:32 | [rushphp/code-tool](https://www.nuget.org/packages/rushphp%2Fcode-tool) | v0.2.0 | RUSHphp | RUSH code tool. Shared-host code delivery: check, push, promote, release and ro… |
| 2026-11-24 01:58:02 | [js-upup/image-text-edit-csv](https://www.nuget.org/packages/js-upup%2Fimage-text-edit-csv) | v0.1.0 |  | Stream text replacement manifests for image edit reviews as CSV. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
