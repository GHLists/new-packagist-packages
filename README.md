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

## Latest list — 2026-11-16 13:19 UTC

New packages created between 2026-11-16 12:18 UTC and 2026-11-16 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T13-19-51-405557Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 12:30:46 | [golovanov/alertloop-php](https://www.nuget.org/packages/golovanov%2Falertloop-php) | v0.1.0 |  | Incident alerts and reliable delivery for PHP sites on shared hosting: Telegram… |
| 2026-11-16 12:35:18 | [studio-variable/kirby-dev-kit](https://www.nuget.org/packages/studio-variable%2Fkirby-dev-kit) | v1.0.0 | Studio Variable | Studio Variable's Kirby plugins for building a site: CSS variants and assets ve… |
| 2026-11-16 12:35:19 | [studio-variable/kirby-prod-kit](https://www.nuget.org/packages/studio-variable%2Fkirby-prod-kit) | v1.0.0 | Studio Variable | Studio Variable's Kirby plugins for a live site: edit button and cookieless ana… |
| 2026-11-16 12:44:39 | [mathsyo/larabase](https://www.nuget.org/packages/mathsyo%2Flarabase) | v0.1.0 |  | Laravel application starter with Sail, Filament, and a production image built f… |
| 2026-11-16 13:01:58 | [dud/contao-pdf-preview](https://www.nuget.org/packages/dud%2Fcontao-pdf-preview) | 1.0.4 | Gunnar Haeuschkel / Drum und… | PDF-Dateien als responsive Bilder in News, Events und allen Inhaltselementen mi… |
| 2026-11-16 13:13:55 | [flytachi/winter-front-nuxt](https://www.nuget.org/packages/flytachi%2Fwinter-front-nuxt) | v1.0.0-rc.1 | Flytachi | A Nuxt frontend in a Winter application: declared in one line, served by the ap… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
