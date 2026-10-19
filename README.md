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

## Latest list — 2026-10-19 09:21 UTC

New packages created between 2026-10-19 08:22 UTC and 2026-10-19 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T09-21-00-566585Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 08:27:14 | [patelutkarsh/masthead](https://www.nuget.org/packages/patelutkarsh%2Fmasthead) | v1.0.0 |  | Kanban publishing workflows for wp-admin. |
| 2026-10-19 08:39:23 | [csba92/revx-php](https://www.nuget.org/packages/csba92%2Frevx-php) | v0.1.0 | csba92 | A small, unofficial PHP client for the Revolut X REST API. |
| 2026-10-19 08:47:45 | [pollora/media](https://www.nuget.org/packages/pollora%2Fmedia) | v0.1.0 | Amphibee | WordPress media on any Flysystem disk: uploads, public URLs, private files, ima… |
| 2026-10-19 08:48:38 | [elibri/elibri_onix_client](https://www.nuget.org/packages/elibri%2Felibri_onix_client) | 0.10.1 |  | PHP client for the elibri API (ONIX 3.0 book metadata) |
| 2026-10-19 08:49:52 | [oki-technologies/people-laravel](https://www.nuget.org/packages/oki-technologies%2Fpeople-laravel) | v1.0.0.0 |  | Sign people in with People, verify their tokens and keep their identities curre… |
| 2026-10-19 08:49:54 | [oki-technologies/people-php](https://www.nuget.org/packages/oki-technologies%2Fpeople-php) | v1.0.0.0 |  | Sign people in with People, verify their tokens and keep their identities curre… |
| 2026-10-19 08:51:48 | [oki-technologies/laravel-module-test](https://www.nuget.org/packages/oki-technologies%2Flaravel-module-test) | v1.0.0.0 | Solomon Ochepa | Run a nwidart/laravel-modules suite a module at a time, with coverage scoped to… |
| 2026-10-19 09:00:07 | [weldist/laravel-passport-client-scopes](https://www.nuget.org/packages/weldist%2Flaravel-passport-client-scopes) | v1.0.0 | X-Adam | Per-client default scopes and RFC 6750 insufficient_scope responses for Laravel… |
| 2026-10-19 09:12:46 | [prasanth/greeting-package](https://www.nuget.org/packages/prasanth%2Fgreeting-package) | v1.0.0 |  | Simple reusable Laravel package |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
