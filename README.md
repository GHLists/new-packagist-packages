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

## Latest list — 2026-10-04 00:20 UTC

New packages created between 2026-10-03 23:20 UTC and 2026-10-04 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T00-20-36-572215Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 23:33:49 | [ernestdefoe/greeter](https://www.nuget.org/packages/ernestdefoe%2Fgreeter) | 1.0.0 | Ernest Defoe | Welcome every new member with a private message, an email, or both — sent the m… |
| 2026-10-03 23:54:03 | [ernestdefoe/reel](https://www.nuget.org/packages/ernestdefoe%2Freel) | 1.0.0 | Ernest Defoe | GIF search in the composer for Flarum 2: trending and search results from GIPHY… |
| 2026-10-04 00:17:43 | [mohammed-mojaly/laralyze](https://www.nuget.org/packages/mohammed-mojaly%2Flaralyze) | v0.1.0 | Mohammed Mojaly | Self-hosted production monitoring and analysis for Laravel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
