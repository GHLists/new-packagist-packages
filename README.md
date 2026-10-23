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

## Latest list — 2026-10-23 10:19 UTC

New packages created between 2026-10-23 09:19 UTC and 2026-10-23 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T10-19-30-221047Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 09:21:48 | [hiddencms/gamification](https://www.nuget.org/packages/hiddencms%2Fgamification) | 0.0.2 |  | Teams, matches, awards and tournaments for HiddenCMS |
| 2026-10-23 09:32:32 | [coolms/imap](https://www.nuget.org/packages/coolms%2Fimap) | v0.1.0-alpha.1 | Dmitry Popov | An IMAP client for PHP that keeps mail in sync: CONDSTORE, QRESYNC, IDLE, SPECI… |
| 2026-10-23 09:52:50 | [plagiarismcheckerx/plagx-preflight](https://www.nuget.org/packages/plagiarismcheckerx%2Fplagx-preflight) | v0.1.2 | Plagiarism Checker X | Free draft checker for PHP: word count, citation and reference list checks, pun… |
| 2026-10-23 10:08:30 | [phoenix1331/laravel-jev-moderation](https://www.nuget.org/packages/phoenix1331%2Flaravel-jev-moderation) | v0.1.0 | Darren Williams | Confidence-aware content moderation for Laravel: classify any Eloquent model wi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
