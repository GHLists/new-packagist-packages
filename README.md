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

## Latest list — 2026-10-13 19:21 UTC

New packages created between 2026-10-13 18:21 UTC and 2026-10-13 19:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T19-21-28-361123Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 18:49:51 | [gavtaylor/retentionpolicy](https://www.nuget.org/packages/gavtaylor%2Fretentionpolicy) | v0.1.0 | Gavin Taylor | Outlook-style per-folder retention policies: automatically delete or archive me… |
| 2026-10-13 19:16:25 | [mnapoli/backoffice-mcp](https://www.nuget.org/packages/mnapoli%2Fbackoffice-mcp) | 0.1.0 |  | A read-only MCP server over a whitelist of Eloquent models, for the internal to… |
| 2026-10-13 19:17:13 | [phattarachai/remote-prompt](https://www.nuget.org/packages/phattarachai%2Fremote-prompt) | v1.0.0 | Phattarachai | A PHPStorm-style remote host panel for the terminal — pick a project's server,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
