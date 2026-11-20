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

## Latest list — 2026-11-20 21:21 UTC

New packages created between 2026-11-20 20:19 UTC and 2026-11-20 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T21-21-04-006331Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 20:24:43 | [sorge-it/http-server](https://www.nuget.org/packages/sorge-it%2Fhttp-server) | v1.0.0 | Stefan Sorge | In-process HTTP/1.1 server for Pest and PHPUnit browser tests, built for coding… |
| 2026-11-20 21:13:28 | [sebastian-meyer/post-office](https://www.nuget.org/packages/sebastian-meyer%2Fpost-office) | v1.0.0 | Sebastian Meyer; Sebastian Me… | This is a Web Frontend for a Mail Server with Postfix and Dovecot. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
