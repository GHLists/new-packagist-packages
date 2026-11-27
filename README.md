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

## Latest list — 2026-11-27 03:20 UTC

New packages created between 2026-11-27 02:22 UTC and 2026-11-27 03:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T03-20-23-886774Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 02:39:02 | [melo/exception-handler](https://www.nuget.org/packages/melo%2Fexception-handler) | v1.0.0 | 棉花糖 | Webman exception handler with unified JSON responses |
| 2026-11-27 03:01:23 | [nativehttp/client](https://www.nuget.org/packages/nativehttp%2Fclient) | v1.1.0 |  | Pure-PHP HTTP client with its own TLS 1.3 and HTTP/2 stack and a modern browser… |
| 2026-11-27 03:05:44 | [codepulse2020/media-upload](https://www.nuget.org/packages/codepulse2020%2Fmedia-upload) | v1.0.0 |  | Secure-by-default file and image upload pipeline for Laravel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
