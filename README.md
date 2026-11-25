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

## Latest list — 2026-11-25 10:19 UTC

New packages created between 2026-11-25 09:19 UTC and 2026-11-25 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T10-19-00-202729Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 09:21:41 | [baris-dev/filament-media-library](https://www.nuget.org/packages/baris-dev%2Ffilament-media-library) | v0.1.1 |  | Filament Curator için klasör gezintili, kullanım takipli ve güvenli silmeli med… |
| 2026-11-25 09:26:57 | [tanbal/php-router](https://www.nuget.org/packages/tanbal%2Fphp-router) | v1.0.1 | tanbal8 | A simple PHP router and backend utilities |
| 2026-11-25 09:27:25 | [mathsgod/light-xml](https://www.nuget.org/packages/mathsgod%2Flight-xml) | v1.0.0 |  | LINQ-style XML construction, querying and editing for PHP |
| 2026-11-25 09:49:18 | [proudnerds/pn-utilities](https://www.nuget.org/packages/proudnerds%2Fpn-utilities) | 14.3.0 | Proud Nerds | Backend tools for TYPO3: a list of pages that have not been changed for a while… |
| 2026-11-25 10:04:13 | [iquesters/event](https://www.nuget.org/packages/iquesters%2Fevent) | v1.0.0 | Pritam Bag | Events for organisations: publish events, members register, admins see attendee… |
| 2026-11-25 10:05:36 | [iquesters/community](https://www.nuget.org/packages/iquesters%2Fcommunity) | v1.0.0 | Pritam Bag | Members, a configurable member directory, approval, plans and tags for Laravel… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
