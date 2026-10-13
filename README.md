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

## Latest list — 2026-10-13 22:18 UTC

New packages created between 2026-10-13 21:23 UTC and 2026-10-13 22:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T22-18-53-644047Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 21:36:09 | [gatovel/storage](https://www.nuget.org/packages/gatovel%2Fstorage) | v1.0.0 |  | Sistema modular e independente de gerenciamento de arquivos para aplicações PHP. |
| 2026-10-13 21:42:22 | [wilycode/translation-languages](https://www.nuget.org/packages/wilycode%2Ftranslation-languages) | v0.1.0 | Simon Piter | Language pluralization rules and configurable locale formatting resources for W… |
| 2026-10-13 21:42:48 | [koh/typo3-indexnow](https://www.nuget.org/packages/koh%2Ftypo3-indexnow) | v1.0.12 | Kai Ole Hartwig | IndexNow for TYPO3: tells search engines within minutes which pages were publis… |
| 2026-10-13 21:44:28 | [firasarafah/laronclad](https://www.nuget.org/packages/firasarafah%2Flaronclad) | v0.1.0-alpha | Firas Arafah | Runtime monitoring and protection layer for Laravel applications. |
| 2026-10-13 21:59:51 | [fiber-interop/curl](https://www.nuget.org/packages/fiber-interop%2Fcurl) | v0.1.1 |  | Cooperative curl_exec() for fiber-interop/api: async\curl\exec() and start() on… |
| 2026-10-13 22:01:24 | [fiber-interop/guzzle](https://www.nuget.org/packages/fiber-interop%2Fguzzle) | v0.1.1 |  | Guzzle handler for fiber-interop/api: concurrent Guzzle requests in fibers on a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
