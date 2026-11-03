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

## Latest list — 2026-11-03 14:20 UTC

New packages created between 2026-11-03 13:19 UTC and 2026-11-03 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T14-20-07-417803Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 13:21:51 | [gilles-g/dump-loader-bundle](https://www.nuget.org/packages/gilles-g%2Fdump-loader-bundle) | v0.1.0 | gilles-g | Symfony bundle loading a SQL dump into the application database, with a live we… |
| 2026-11-03 13:22:43 | [crystoline/xpsr-auth-oauth2-server](https://www.nuget.org/packages/crystoline%2Fxpsr-auth-oauth2-server) | v0.7.0 | Adekunle | An OAuth2 authorization server for XPSR applications, on league/oauth2-server:… |
| 2026-11-03 13:22:43 | [crystoline/xpsr-broadcast](https://www.nuget.org/packages/crystoline%2Fxpsr-broadcast) | v0.7.0 | Adekunle | Live updates to browsers for XPSR applications, through a Mercure hub: publish… |
| 2026-11-03 13:22:43 | [crystoline/xpsr-health](https://www.nuget.org/packages/crystoline%2Fxpsr-health) | v0.7.0 | Adekunle | Health checks for XPSR applications: live and ready endpoints for load balancer… |
| 2026-11-03 13:22:43 | [crystoline/xpsr-orm-cycle](https://www.nuget.org/packages/crystoline%2Fxpsr-orm-cycle) | v0.7.0 | Adekunle | Cycle ORM for XPSR applications: attribute-mapped entities on XPSR's database c… |
| 2026-11-03 13:22:43 | [crystoline/xpsr-translation](https://www.nuget.org/packages/crystoline%2Fxpsr-translation) | v0.7.0 | Adekunle | Translations for XPSR applications on Symfony Translation: message files per lo… |
| 2026-11-03 13:48:10 | [rajtik76/nette-console](https://www.nuget.org/packages/rajtik76%2Fnette-console) | v0.1.2 |  | Artisan-like console for Nette: Symfony Console in DI, package auto-discovery a… |
| 2026-11-03 13:48:31 | [rajtik76/nette-migrations](https://www.nuget.org/packages/rajtik76%2Fnette-migrations) | v0.1.3 |  | Laravel-like migrations, schema builder, seeders and factories for Nette Databa… |
| 2026-11-03 13:48:35 | [spearsystems/lcp-sdk](https://www.nuget.org/packages/spearsystems%2Flcp-sdk) | v1.1.1 |  | LCP Lead Context Protocol SDK for PHP |
| 2026-11-03 13:53:51 | [golpilolz/media-library](https://www.nuget.org/packages/golpilolz%2Fmedia-library) | v0.0.1 | Arthur Haton | Media library for Symfony Form |
| 2026-11-03 14:04:31 | [schachbulle/contao-allinkl-bundle](https://www.nuget.org/packages/schachbulle%2Fcontao-allinkl-bundle) | 0.1.0 | Frank Hoppe | Verwaltet Domains, Subdomains, DNS, Postfächer, Datenbanken, FTP-Zugänge, Cronj… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
