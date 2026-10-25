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

## Latest list — 2026-10-25 11:19 UTC

New packages created between 2026-10-25 10:20 UTC and 2026-10-25 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T11-19-50-440023Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 10:23:04 | [blackcube/bridge-form](https://www.nuget.org/packages/blackcube%2Fbridge-form) | 1.0.0 | Philippe Gaultier | Form fields for Yii framework, without any styling |
| 2026-10-25 10:27:26 | [yuriitatur/repository-laravel](https://www.nuget.org/packages/yuriitatur%2Frepository-laravel) | v0.1.0 | Yurii Tatur | Laravel repository drivers and more |
| 2026-10-25 10:28:46 | [blackcube/graphql](https://www.nuget.org/packages/blackcube%2Fgraphql) | 1.0.0 | Philippe Gaultier | GraphQL read-only API for Blackcube CMS |
| 2026-10-25 10:35:41 | [privatus/analytics](https://www.nuget.org/packages/privatus%2Fanalytics) | v1.0.0 | Two Phase LLC | Adds the cookieless Privatus Analytics tracking script to PHP, Laravel and Symf… |
| 2026-10-25 10:37:54 | [blackcube/ssr](https://www.nuget.org/packages/blackcube%2Fssr) | 1.0.0 | Philippe Gaultier | Server-side routing and rendering bridge for blackcube/dcore |
| 2026-10-25 10:43:41 | [blackcube/bleet](https://www.nuget.org/packages/blackcube%2Fbleet) | 1.0.0 | Philippe Gaultier | Blackcube UIKit for Yii framework |
| 2026-10-25 10:55:53 | [jasonbaciulis/bedrock-commands](https://www.nuget.org/packages/jasonbaciulis%2Fbedrock-commands) | v1.0.0 | Jason Baciulis | Artisan commands that scaffold, rename and delete page builder blocks and artic… |
| 2026-10-25 10:56:07 | [blackcube/dboard](https://www.nuget.org/packages/blackcube%2Fdboard) | 1.0.0 | Philippe Gaultier | CMS Administration Panel |
| 2026-10-25 10:58:13 | [lucinda/console-view](https://www.nuget.org/packages/lucinda%2Fconsole-view) | v1.0.0 | Lucian Popescu | HTML-like terminal view language and renderer for console MVC applications |
| 2026-10-25 11:01:33 | [yuriitatur/subscriptions](https://www.nuget.org/packages/yuriitatur%2Fsubscriptions) | v0.1.0 | Yurii Tatur | subscription tracking |
| 2026-10-25 11:03:06 | [blackcube/dboard-bridge](https://www.nuget.org/packages/blackcube%2Fdboard-bridge) | 1.0.0 | Philippe Gaultier | Blackcube Dboard bridge for non-Yii3 frameworks |
| 2026-10-25 11:16:47 | [blackcube/mcp](https://www.nuget.org/packages/blackcube%2Fmcp) | 1.0.0 | Philippe Gaultier | MCP server for the Blackcube admin data layer |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
