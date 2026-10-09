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

## Latest list — 2026-10-09 05:19 UTC

New packages created between 2026-10-09 04:19 UTC and 2026-10-09 05:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T05-19-57-769097Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 04:27:55 | [max-messenger-bot/max-bot-sender-php](https://www.nuget.org/packages/max-messenger-bot%2Fmax-bot-sender-php) | 1.0.0 | Eugene Makhaev | PHP library for sending messages via the Max Messenger Bot API |
| 2026-10-09 04:33:26 | [klyp/wordpress](https://www.nuget.org/packages/klyp%2Fwordpress) | 7.1.2 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
