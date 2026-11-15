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

## Latest list — 2026-11-15 10:20 UTC

New packages created between 2026-11-15 09:19 UTC and 2026-11-15 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T10-20-40-274373Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 09:38:56 | [july/julyadmin](https://www.nuget.org/packages/july%2Fjulyadmin) | v1.0.7 | July | ThinkPHP 6/8 rapid admin extension (Layui + Lyear). Requires a ThinkPHP host pr… |
| 2026-11-15 09:41:37 | [mailtruss/mailtruss](https://www.nuget.org/packages/mailtruss%2Fmailtruss) | v0.1.0 |  | PHP client for the Mailtruss email API, with a Laravel mail transport. |
| 2026-11-15 10:10:38 | [pasax/secure-monitor](https://www.nuget.org/packages/pasax%2Fsecure-monitor) | v1.0.0 | Roby; pasax-dev | Pasax - enterprise-grade headless self-hosted WAF, threat detection engine, zer… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
