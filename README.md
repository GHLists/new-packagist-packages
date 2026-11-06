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

## Latest list — 2026-11-06 10:19 UTC

New packages created between 2026-11-06 09:21 UTC and 2026-11-06 10:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T10-19-58-703935Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 09:24:56 | [mattleads/agent-publishing-bundle](https://www.nuget.org/packages/mattleads%2Fagent-publishing-bundle) | v0.1.1 | Matvei (Matt) Mochalkin | Publishing API and MCP server for Symfony sites: AI agents, marketing platforms… |
| 2026-11-06 09:36:03 | [ithilbert/dev-tools](https://www.nuget.org/packages/ithilbert%2Fdev-tools) | 1.0.0 | Jörg Hilbert | Gemeinsame Entwicklerwerkzeuge für Laravel-13-Projekte der IT-Hilbert GmbH (nur… |
| 2026-11-06 09:52:29 | [intragile/laravel-observability](https://www.nuget.org/packages/intragile%2Flaravel-observability) | v1.0.0 | IntrAgile Kft. | Observability kit for Laravel on top of spatie/laravel-health and spatie/larave… |
| 2026-11-06 10:14:05 | [mikepagedev/portfolio-frontend](https://www.nuget.org/packages/mikepagedev%2Fportfolio-frontend) | v1.0.0 | Mike Page | Public portfolio and case-study pages for Laravel, with or without Filament. |
| 2026-11-06 10:17:10 | [atannex/domain-routing](https://www.nuget.org/packages/atannex%2Fdomain-routing) | v1.0.0 | Atangageih Leke Collins | Multi-domain routing for Laravel: sites bound to hosts, site-scoped routes, cro… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
