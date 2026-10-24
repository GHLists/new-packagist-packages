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

## Latest list — 2026-10-24 22:19 UTC

New packages created between 2026-10-24 21:21 UTC and 2026-10-24 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T22-19-35-089546Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 21:39:34 | [jponchiroli/laravel-base](https://www.nuget.org/packages/jponchiroli%2Flaravel-base) | v0.1.0 | Joao Pedro Ferreira Ponchiroli | Base classes, standardized JSON responses with i18n messages (en, pt_BR) and a… |
| 2026-10-24 21:58:28 | [socialweb/http-message-signatures](https://www.nuget.org/packages/socialweb%2Fhttp-message-signatures) | 0.1.0 |  | Signs and verifies HTTP messages under RFC 9421 and draft-cavage-http-signature… |
| 2026-10-24 22:01:44 | [jeffersongoncalves/laravel-auto-translate](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-auto-translate) | 1.0.0 | Jefferson Gonçalves | Queued machine translation for Laravel translatable model attributes (spatie/la… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
