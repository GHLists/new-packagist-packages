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

## Latest list — 2026-10-25 15:21 UTC

New packages created between 2026-10-25 14:20 UTC and 2026-10-25 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T15-21-00-188669Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 14:23:37 | [near/near-jsonrpc-client-php](https://www.nuget.org/packages/near%2Fnear-jsonrpc-client-php) | v0.1.2 |  | Typed PHP client and OpenAPI generator for NEAR JSON-RPC |
| 2026-10-25 14:24:29 | [edgarmiralles/laravel-async-subscribers](https://www.nuget.org/packages/edgarmiralles%2Flaravel-async-subscribers) | v0.1.0 |  | Auto-discovered, queued event subscribers for Laravel. |
| 2026-10-25 14:42:07 | [gisoo/gisoo-php](https://www.nuget.org/packages/gisoo%2Fgisoo-php) | v0.1.0 | Gisoo | Official PHP SDK and Laravel package for the Gisoo AI API (OpenAI-compatible):… |
| 2026-10-25 14:50:27 | [dockcodes/dockaccess-alt-generator](https://www.nuget.org/packages/dockcodes%2Fdockaccess-alt-generator) | 1.0.0 | Dock | Framework-agnostic PHP client for the dockaccess.org AI alt text generator, wit… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
