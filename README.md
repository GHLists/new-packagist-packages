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

## Latest list — 2026-11-03 18:19 UTC

New packages created between 2026-11-03 17:21 UTC and 2026-11-03 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T18-19-09-467705Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 17:38:42 | [hazelchat/agent-plugin](https://www.nuget.org/packages/hazelchat%2Fagent-plugin) | v1.0.0 | Hazelchat | Adds your Hazelchat AI chat agent to every page of an October CMS site from one… |
| 2026-11-03 17:57:18 | [muhpuc40/chunkit](https://www.nuget.org/packages/muhpuc40%2Fchunkit) | v0.1.0 | Minhaj | Chunked, resumable, server-authoritative file uploads for Laravel 11/12 with a… |
| 2026-11-03 17:58:43 | [ramon/magic-link](https://www.nuget.org/packages/ramon%2Fmagic-link) | v1.0.0 | Ramon Guilherme | Passwordless sign in and sign up for Flarum 2 with a magic link and a one-time… |
| 2026-11-03 18:00:45 | [atannex/news-publisher](https://www.nuget.org/packages/atannex%2Fnews-publisher) | v0.1.0 |  | Headless Laravel news ingestion, editorial review and safe Facebook Page publis… |
| 2026-11-03 18:09:53 | [semsen1/image-safe-area](https://www.nuget.org/packages/semsen1%2Fimage-safe-area) | v1.0.0 |  | Nova image field with safe area overlay |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
