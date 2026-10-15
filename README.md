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

## Latest list — 2026-10-15 20:21 UTC

New packages created between 2026-10-15 19:23 UTC and 2026-10-15 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T20-21-24-924167Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 19:30:55 | [justinholtweb/craft-archie](https://www.nuget.org/packages/justinholtweb%2Fcraft-archie) | 5.0.1 | Justin Holt | Author a Craft content model as a YAML or JSON blueprint — lint it, plan the di… |
| 2026-10-15 19:49:08 | [theprimestudio/laravel-sentinel](https://www.nuget.org/packages/theprimestudio%2Flaravel-sentinel) | v1.0.0 | The Prime Studio | Enterprise security, antivirus, webshell detection, WAF, file integrity, and qu… |
| 2026-10-15 20:01:45 | [sellinnate/sales-crm](https://www.nuget.org/packages/sellinnate%2Fsales-crm) | v1.0.0 | Filippo Calabrese | Sales pipeline CRM for Laravel: kanban board, deals, companies & people, activi… |
| 2026-10-15 20:13:28 | [rasuvaeff/context-process](https://www.nuget.org/packages/rasuvaeff%2Fcontext-process) | v0.1.0 | Victor Razuvaev | Run external processes under a rasuvaeff/context budget: the timeout follows th… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
