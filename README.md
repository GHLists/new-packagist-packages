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

## Latest list — 2026-10-11 11:20 UTC

New packages created between 2026-10-11 10:21 UTC and 2026-10-11 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T11-20-39-881138Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 10:31:10 | [heyjorgedev/qstash-laravel](https://www.nuget.org/packages/heyjorgedev%2Fqstash-laravel) | v0.1.0 | Jorge Lapa | A Laravel queue driver for Upstash QStash |
| 2026-10-11 10:56:57 | [inupress/seo](https://www.nuget.org/packages/inupress%2Fseo) | v0.1.0 |  | Search engine basics for Inupress: canonical and Open Graph tags, sitemap.xml a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
