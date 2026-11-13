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

## Latest list — 2026-11-13 10:19 UTC

New packages created between 2026-11-13 09:19 UTC and 2026-11-13 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T10-19-38-220755Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 09:29:11 | [javierms/subroles](https://www.nuget.org/packages/javierms%2Fsubroles) | 1.0.0 |  | Adds subroles: extra permission sets attached to a parent user role. |
| 2026-11-13 09:47:22 | [kafka-bus/typed-topics](https://www.nuget.org/packages/kafka-bus%2Ftyped-topics) | v2.2.0 |  | Typed topics for Kafka Bus |
| 2026-11-13 09:50:36 | [lara-igniter/laraigniter-excel](https://www.nuget.org/packages/lara-igniter%2Flaraigniter-excel) | 1.0.0 |  | Excel exports for Laraigniter. Export classes collect rows and the writer store… |
| 2026-11-13 09:58:43 | [pharaonic/laravel-bookmarks](https://www.nuget.org/packages/pharaonic%2Flaravel-bookmarks) | 13.0.0 | Moamen Eltouny (Raggi) | Polymorphic bookmarks for Laravel Eloquent models, with JSON-object metadata an… |
| 2026-11-13 10:04:57 | [mtubis/html-translator-filament](https://www.nuget.org/packages/mtubis%2Fhtml-translator-filament) | v0.1.0 | Magdalena Tubis | Filament v5 plugin for markup-safe AI translation of translatable models, built… |
| 2026-11-13 10:14:29 | [silarhi/voter-bundle](https://www.nuget.org/packages/silarhi%2Fvoter-bundle) | v0.1.0 | Guillaume Sainthillier | Declare Symfony voter rules with a #[Grants] attribute on the method that decid… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
