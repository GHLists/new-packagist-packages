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

## Latest list — 2026-11-08 11:21 UTC

New packages created between 2026-11-08 10:21 UTC and 2026-11-08 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T11-21-09-15947Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 10:25:01 | [gismatul/laravel-support-chat](https://www.nuget.org/packages/gismatul%2Flaravel-support-chat) | v1.2.0 | Gismat Mammadov | Website live-chat widget for Laravel where your team answers from Telegram or f… |
| 2026-11-08 10:25:02 | [gismatul/nova-support-chat](https://www.nuget.org/packages/gismatul%2Fnova-support-chat) | v1.2.0 | Gismat Mammadov | Laravel Nova admin panel for gismatul/laravel-support-chat: read, answer and cl… |
| 2026-11-08 10:40:37 | [mulertech/blog-bundle](https://www.nuget.org/packages/mulertech%2Fblog-bundle) | v1.0.0 | Sébastien Muler | Symfony bundle for a Markdown blog: shared article model, admin, public pages,… |
| 2026-11-08 10:59:22 | [codebypinar/glpi-guard](https://www.nuget.org/packages/codebypinar%2Fglpi-guard) | v0.1.0 | Pınar Topuz | Read-only security audit for your own GLPI installation: known vulnerabilities,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
