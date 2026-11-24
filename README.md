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

## Latest list — 2026-11-24 19:20 UTC

New packages created between 2026-11-24 18:20 UTC and 2026-11-24 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T19-20-15-621265Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 18:23:44 | [averay/phpforce-soap-client](https://www.nuget.org/packages/averay%2Fphpforce-soap-client) | v0.2.0 | David de Boer; Adam Averay | A PHP client for the Salesforce SOAP API |
| 2026-11-24 18:43:00 | [lokus/servercheck](https://www.nuget.org/packages/lokus%2Fservercheck) | v1.0.0 |  |  |
| 2026-11-24 18:43:30 | [scottboms/mastodon-feed](https://www.nuget.org/packages/scottboms%2Fmastodon-feed) | 6.0.0 | Scott Boms | Mastodon Feed plugin for Kirby |
| 2026-11-24 19:12:13 | [statamic/forms-pro](https://www.nuget.org/packages/statamic%2Fforms-pro) | v1.0.0 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
