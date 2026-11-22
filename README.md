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

## Latest list — 2026-11-22 12:19 UTC

New packages created between 2026-11-22 11:19 UTC and 2026-11-22 12:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T12-19-40-536267Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 11:32:55 | [raj5852/hello-world](https://www.nuget.org/packages/raj5852%2Fhello-world) | v1.0.0 |  | A test package |
| 2026-11-22 11:34:58 | [smstunnel/flarum-sms](https://www.nuget.org/packages/smstunnel%2Fflarum-sms) | v1.0.0 | NARBOWEB SRL | Text alerts for your Flarum staff, and opt-in reply and mention texts for membe… |
| 2026-11-22 11:41:38 | [datacircle/mcp-tools](https://www.nuget.org/packages/datacircle%2Fmcp-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. This package adds four tools to an MCP server that uses… |
| 2026-11-22 12:11:38 | [esoul-cz/coding-standard](https://www.nuget.org/packages/esoul-cz%2Fcoding-standard) | v0.1.0 |  | Shared PHP-CS-Fixer ruleset for eSoul PHP projects. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
