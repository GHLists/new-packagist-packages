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

## Latest list — 2026-11-03 15:19 UTC

New packages created between 2026-11-03 14:20 UTC and 2026-11-03 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T15-19-49-348385Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 14:20:39 | [tualo/ds-sftp-import](https://www.nuget.org/packages/tualo%2Fds-sftp-import) | 1.0.2 |  | SFTP import package for Tualo Office package |
| 2026-11-03 14:22:43 | [gp247/mcp](https://www.nuget.org/packages/gp247%2Fmcp) | 2.0.0 | GP247 | MCP server for GP247 / S-Cart: let the site owner's AI agents (Claude, Cursor,… |
| 2026-11-03 14:31:26 | [rajtik76/nette-middleware](https://www.nuget.org/packages/rajtik76%2Fnette-middleware) | v0.2.0 |  | Laravel-style route middleware for Nette Application |
| 2026-11-03 14:45:38 | [apip/wallet](https://www.nuget.org/packages/apip%2Fwallet) | v1.0.3 | apip | apip.io Wallet |
| 2026-11-03 14:48:17 | [urbania/apple-news](https://www.nuget.org/packages/urbania%2Fapple-news) | v1.0.0 | Folklore; David Mongeau-Petit… |  |
| 2026-11-03 15:00:08 | [julien-its/emails-queue-s8](https://www.nuget.org/packages/julien-its%2Femails-queue-s8) | 1.0.0 | Julien IT Solutions | Symfony Easy Emails Queue Bundle for Symfony 8 |
| 2026-11-03 15:00:51 | [vielhuber/linkedinmcp](https://www.nuget.org/packages/vielhuber%2Flinkedinmcp) | v0.1.1 |  | Minimal PHP helper and MCP server for LinkedIn posting and member data portabil… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
