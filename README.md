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

## Latest list — 2026-10-22 12:21 UTC

New packages created between 2026-10-22 11:20 UTC and 2026-10-22 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T12-21-31-72067Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 11:24:29 | [skeeks/cms-communication](https://www.nuget.org/packages/skeeks%2Fcms-communication) | 1.0.0 | Semenov Alexander | Communications for SkeekS CMS CRM: mailboxes, messenger bots, conversations, cl… |
| 2026-10-22 11:24:58 | [skeeks/cms-communication-imap](https://www.nuget.org/packages/skeeks%2Fcms-communication-imap) | 1.0.0 | Semenov Alexander | IMAP/SMTP mailbox driver for skeeks/cms-communication |
| 2026-10-22 11:30:07 | [stickysoftware/bump-laravel](https://www.nuget.org/packages/stickysoftware%2Fbump-laravel) | v1.0.0 | Wouter Dijkstra | Laravel client for Bump: send events from your app, and Bump keeps exact runnin… |
| 2026-10-22 11:50:17 | [coastercms/coastercommerce](https://www.nuget.org/packages/coastercms%2Fcoastercommerce) | v13.0.0-beta.1 | Neil Jennings | Ecommerce addon for Coaster CMS |
| 2026-10-22 11:57:58 | [jeffersongoncalves/laravel-autentique](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-autentique) | 1.0.0 | Jefferson Gonçalves | Laravel client for the Autentique GraphQL API (e-signature): documents, signers… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
