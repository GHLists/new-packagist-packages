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

## Latest list — 2026-11-13 14:22 UTC

New packages created between 2026-11-13 13:20 UTC and 2026-11-13 14:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T14-22-37-575127Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 13:22:59 | [dbravoan/dbcms-module-popups](https://www.nuget.org/packages/dbravoan%2Fdbcms-module-popups) | v1.0.0 |  | Editorial popups and announcement overlays using shared dbCMS blocks and privac… |
| 2026-11-13 13:24:42 | [rsgrinko/ai-sdk](https://www.nuget.org/packages/rsgrinko%2Fai-sdk) | v0.1.2 | rsgrinko | Лёгкий PHP SDK для агентов с вызовом инструментов поверх OpenAI-совместимых API… |
| 2026-11-13 13:27:18 | [tonsinn/sticky-links-bundle](https://www.nuget.org/packages/tonsinn%2Fsticky-links-bundle) | v1.0.0 | Mathias Ebert | Sticky icon links for Contao 5 and 6 - a bar of icons fixed to the left or righ… |
| 2026-11-13 13:29:02 | [pushword/twigstan](https://www.nuget.org/packages/pushword%2Ftwigstan) | 1.0.108.1 |  | TwigStan integration for Pushword projects. |
| 2026-11-13 13:36:45 | [shadcs/ferga-builder-mutlilanguage-rtl-support](https://www.nuget.org/packages/shadcs%2Fferga-builder-mutlilanguage-rtl-support) | v0.1.0 | Ferga Solutions | Drag-and-drop visual page builder for Filament with multilingual content, RTL s… |
| 2026-11-13 13:47:25 | [glitchr/symfony-profiler-pack](https://www.nuget.org/packages/glitchr%2Fsymfony-profiler-pack) | v1.0.0 | Marco Meyer | A floating web debug toolbar for Symfony's profiler (drag it, resize it, fold i… |
| 2026-11-13 13:50:51 | [glitchr/laravel-profiler-pack](https://www.nuget.org/packages/glitchr%2Flaravel-profiler-pack) | v1.0.0 | Marco Meyer | A floating debug bar for Laravel, read from Laravel Telescope: status, route, t… |
| 2026-11-13 13:52:24 | [tobimori/kirby-file-usage](https://www.nuget.org/packages/tobimori%2Fkirby-file-usage) | 0.1.0 | Tobias Möritz | See where files are used in Kirby: on which pages, in which fields and blocks,… |
| 2026-11-13 13:55:50 | [x-laravel/listmonk](https://www.nuget.org/packages/x-laravel%2Flistmonk) | v1.0.0 | Mehmet ÖĞMEN | Listmonk subscribers for Eloquent models with queued syncing, list membership a… |
| 2026-11-13 14:16:08 | [simplygoodwork/craft-environment-banner](https://www.nuget.org/packages/simplygoodwork%2Fcraft-environment-banner) | 1.0.0 | Good Work | Marks Craft environments with a control panel banner and a coloured symbol at t… |
| 2026-11-13 14:16:41 | [armanoide/roundcube-iconizer](https://www.nuget.org/packages/armanoide%2Froundcube-iconizer) | 1.0.0 | Armanoide | Custom per-folder icons in the Roundcube Elastic sidebar — searchable Iconify p… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
