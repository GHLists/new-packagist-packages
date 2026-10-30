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

## Latest list — 2026-10-30 15:22 UTC

New packages created between 2026-10-30 14:25 UTC and 2026-10-30 15:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T15-22-22-514404Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 14:27:52 | [ernestdefoe/rotation](https://www.nuget.org/packages/ernestdefoe%2Frotation) | 1.0.0 | Ernest Defoe | Rotation — members' music listening for Flarum 2: connect Last.fm, now playing… |
| 2026-10-30 14:29:06 | [survos/duckdb-api-bundle](https://www.nuget.org/packages/survos%2Fduckdb-api-bundle) | 2.45.7 |  | Read-only API Platform 5 state provider for explicitly mapped DuckDB resources… |
| 2026-10-30 14:36:50 | [jeffersongoncalves/livewire-horizon](https://www.nuget.org/packages/jeffersongoncalves%2Flivewire-horizon) | 1.0.0 |  |  |
| 2026-10-30 14:39:33 | [nedal-network/filament-scrollable-topnav](https://www.nuget.org/packages/nedal-network%2Ffilament-scrollable-topnav) | 1.0.0 | Emuniq | Makes Filament's top navigation scrollable instead of wrapping into multiple ro… |
| 2026-10-30 14:39:57 | [ahmed-ahmed/laravel-ddd](https://www.nuget.org/packages/ahmed-ahmed%2Flaravel-ddd) | v1.0.0 |  | A Laravel DDD implementation |
| 2026-10-30 14:41:11 | [mage-os-italia/module-language-it_it](https://www.nuget.org/packages/mage-os-italia%2Fmodule-language-it_it) | 0.0.26 |  | it_IT language package. |
| 2026-10-30 14:46:50 | [ryzemcbe/ryzemp](https://www.nuget.org/packages/ryzemcbe%2Fryzemp) | v1.0.0-beta.3 |  | RyzeMP: a multiversion Minecraft Bedrock server built on the PocketMine-MP 5 API |
| 2026-10-30 14:47:02 | [daycry/twig-codeigniter4](https://www.nuget.org/packages/daycry%2Ftwig-codeigniter4) | v4.0.0 |  | CodeIgniter 4 adapter for daycry/twig |
| 2026-10-30 15:05:51 | [xddesigners/silverstripe-sitemap-cache](https://www.nuget.org/packages/xddesigners%2Fsilverstripe-sitemap-cache) | 1.0.0 | XD designers | Static file cache for silverstripe/googlesitemaps (wilr) on SilverStripe 4/5, r… |
| 2026-10-30 15:06:48 | [milwad/laravel-validate-filament](https://www.nuget.org/packages/milwad%2Flaravel-validate-filament) | v1.0.0 | Milwad Khosravi | Filament field macros for the milwad/laravel-validate validation rules. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
