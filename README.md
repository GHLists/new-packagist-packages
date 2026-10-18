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

## Latest list — 2026-10-18 13:18 UTC

New packages created between 2026-10-18 12:19 UTC and 2026-10-18 13:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T13-18-51-302711Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 12:26:43 | [studi-assist/typo3-chatbot-widget](https://www.nuget.org/packages/studi-assist%2Ftypo3-chatbot-widget) | v1.3.0 |  | TYPO3 extension that adds a floating bottom-right chatbot widget and opens an i… |
| 2026-10-18 13:09:54 | [bicho-fyi/php](https://www.nuget.org/packages/bicho-fyi%2Fphp) | 1.0.0 | FreshJuice; Alex Zappa | Report PHP exceptions and errors to Bicho over OTLP/HTTP JSON |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
