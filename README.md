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

## Latest list — 2026-10-13 23:19 UTC

New packages created between 2026-10-13 22:18 UTC and 2026-10-13 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T23-19-39-373535Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 22:24:14 | [hksagentur/kirby-fragments](https://www.nuget.org/packages/hksagentur%2Fkirby-fragments) | 0.1.1 | Daniel Weidner | Serve snippets as HTML fragments for progressive enhancement in Kirby CMS |
| 2026-10-13 22:36:30 | [mtubis/html-translator-laravel](https://www.nuget.org/packages/mtubis%2Fhtml-translator-laravel) | v0.1.0 | Magdalena Tubis | Laravel integration for mtubis/html-translator: translate HTML with LLMs (OpenA… |
| 2026-10-13 22:37:08 | [tryhackx/flarum-homepage-blocks](https://www.nuget.org/packages/tryhackx%2Fflarum-homepage-blocks) | 2.8.2 | TryHackX | Customizable homepage blocks for tracker-style Flarum forums featuring dual sta… |
| 2026-10-13 22:46:50 | [fiber-interop/pg](https://www.nuget.org/packages/fiber-interop%2Fpg) | v0.1.0 |  | Cooperative pg_query() for fiber-interop/api: async\pg\query(), query_params(),… |
| 2026-10-13 22:56:09 | [wilycode/translation-array](https://www.nuget.org/packages/wilycode%2Ftranslation-array) | v0.1.0 | Simon Piter | Lazy PHP array translation provider with language fallback, pluralization, and… |
| 2026-10-13 23:03:21 | [tamarackdb/tamarackdb-php](https://www.nuget.org/packages/tamarackdb%2Ftamarackdb-php) | v0.5.0 |  | PHP client for TamarackDB, an event store compliant with the DCB specification. |
| 2026-10-13 23:13:35 | [wilycode/translation-database](https://www.nuget.org/packages/wilycode%2Ftranslation-database) | v0.1.0 | Simon Piter | Lazy database-backed PHP translation provider with pluralization, language fall… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
