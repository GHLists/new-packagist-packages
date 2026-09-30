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

## Latest list — 2026-09-30 20:21 UTC

New packages created between 2026-09-30 19:21 UTC and 2026-09-30 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T20-21-25-844042Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 19:23:24 | [curly-deni/laravel-api-concern](https://www.nuget.org/packages/curly-deni%2Flaravel-api-concern) | 1.0 | Danila Mikhalev | Reusable API responses and exception rendering for Laravel |
| 2026-09-30 19:30:57 | [rutgers-oit-eds/laravel-cas-authentication](https://www.nuget.org/packages/rutgers-oit-eds%2Flaravel-cas-authentication) | v1.0.0 | Nicholas Blew | Laravel package for integrating CAS authentication |
| 2026-09-30 19:33:08 | [squipix/openai-php-client](https://www.nuget.org/packages/squipix%2Fopenai-php-client) | 1.0.0 | Nuno Maduro; Sandro Gehri | OpenAI PHP is a supercharged PHP API client that allows you to interact with th… |
| 2026-09-30 19:33:24 | [doxa-soft/laravel-seeme](https://www.nuget.org/packages/doxa-soft%2Flaravel-seeme) | v1.0.0 | Mánuel Fodor | Laravel package for the SeeMe SMS Gateway |
| 2026-09-30 19:37:08 | [heimseiten/contao-custom-navigation-bundle](https://www.nuget.org/packages/heimseiten%2Fcontao-custom-navigation-bundle) | 1.0.0 | heimseiten.de - Webdesign aus… | Sicherheitsdreieck für das barrierefreie Navigationsmenü von Contao: Fährt die… |
| 2026-09-30 19:40:33 | [spiggle/filament-portal-snapshot](https://www.nuget.org/packages/spiggle%2Ffilament-portal-snapshot) | 1.0.0 | Spiggle | Filament 4/5 plugin for creating, scheduling, restoring, exporting and remotely… |
| 2026-09-30 19:55:25 | [fabeat/markdown-word](https://www.nuget.org/packages/fabeat%2Fmarkdown-word) | v0.1.0 | Fabian Graßl | Pure PHP Markdown to Word (DOCX) generator and back, built on PHPWord. Full Com… |
| 2026-09-30 19:56:53 | [curly-deni/laravel-tenancy](https://www.nuget.org/packages/curly-deni%2Flaravel-tenancy) | 1.0 | Danila Mikhalev | Tenant identity, membership, access control, and resource isolation for Laravel. |
| 2026-09-30 19:59:13 | [kodhe/events](https://www.nuget.org/packages/kodhe%2Fevents) | 1.0.0 |  | PSR-14 compatible event dispatcher for the Kodhe framework (standalone, general… |
| 2026-09-30 20:11:04 | [reactor/reactor](https://www.nuget.org/packages/reactor%2Freactor) | 1.0.0 |  | A powerful event dispatcher with middleware, listener groups, and context-based… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
