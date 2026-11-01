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

## Latest list — 2026-11-01 13:19 UTC

New packages created between 2026-11-01 12:20 UTC and 2026-11-01 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T13-19-42-834888Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 12:29:47 | [rightform/rightform](https://www.nuget.org/packages/rightform%2Frightform) | v1.0.0 | rightform Aleksander Jagusiak | Holds the rightform vendor name on Packagist for packages made by rightform. Co… |
| 2026-11-01 12:33:19 | [php-script/editor-filament](https://www.nuget.org/packages/php-script%2Feditor-filament) | v0.1.0 | Robert Kummer | Filament 5 form field (PhpScriptEditor) for the <php-script-editor> web compone… |
| 2026-11-01 12:33:35 | [php-script/editor-laravel](https://www.nuget.org/packages/php-script%2Feditor-laravel) | v0.1.0 | Robert Kummer | Laravel integration (Blade component, config endpoint, lint response, validatio… |
| 2026-11-01 12:34:41 | [owebstudio/kirby-search-insights](https://www.nuget.org/packages/owebstudio%2Fkirby-search-insights) | 1.0.0 | oweb studio | Shows what visitors search for on your Kirby site, which searches find nothing… |
| 2026-11-01 12:42:10 | [dynv/dynv](https://www.nuget.org/packages/dynv%2Fdynv) | v0.1.0 |  | Dependency-free PHP client for the Dynv local agent |
| 2026-11-01 12:48:19 | [kayedspace/laravel-mcp-bridge](https://www.nuget.org/packages/kayedspace%2Flaravel-mcp-bridge) | v0.1.0 | Ali Youssef Kayed | Turn what your Laravel app already declares (routes, Artisan commands, jobs, ac… |
| 2026-11-01 12:50:16 | [eveshipfit/esf-format](https://www.nuget.org/packages/eveshipfit%2Fesf-format) | v1.0.0 | EVEShipFit Team | Read and write esf/1, the plain-text format for EVE Online ship fits |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
