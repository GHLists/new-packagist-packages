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

## Latest list — 2026-10-15 06:19 UTC

New packages created between 2026-10-15 05:21 UTC and 2026-10-15 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T06-19-50-826237Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 05:24:19 | [pieceofcake2/panther](https://www.nuget.org/packages/pieceofcake2%2Fpanther) | v1.0.0 |  | End-to-End tests for CakePHP 2 applications with Symfony Panther and PHPUnit |
| 2026-10-15 05:27:38 | [vlydev/yajl-stream](https://www.nuget.org/packages/vlydev%2Fyajl-stream) | v0.1.0 |  | Stream the elements of a huge JSON array out of a file in constant memory, on t… |
| 2026-10-15 05:34:10 | [toolspacks/utils](https://www.nuget.org/packages/toolspacks%2Futils) | v1.1.1 |  | Shared Utils for Wujie Projects |
| 2026-10-15 06:10:01 | [ntcte/max-platform](https://www.nuget.org/packages/ntcte%2Fmax-platform) | v0.1.0 | ГАПОУ СО "Нижнетагильский тор… | PHP SDK for the Max messenger Bot API: typed API client, bot framework, webhook… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
