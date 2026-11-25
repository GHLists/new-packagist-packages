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

## Latest list — 2026-11-25 01:21 UTC

New packages created between 2026-11-25 00:20 UTC and 2026-11-25 01:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T01-21-24-708404Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 00:43:14 | [oe2i/groy-package](https://www.nuget.org/packages/oe2i%2Fgroy-package) | v1.0.0-alpha.1 | Anthony Osawere; oe2i | Opinionated Laravel 13 package starter kit. |
| 2026-11-25 00:48:51 | [verbb/editor](https://www.nuget.org/packages/verbb%2Feditor) | 1.0.0 | Verbb | A Craft-native frontend rich-text editor foundation. |
| 2026-11-25 00:48:55 | [verbb/protect](https://www.nuget.org/packages/verbb%2Fprotect) | 1.0.0 | Verbb | Shared protection infrastructure for untrusted user-generated actions. |
| 2026-11-25 00:57:02 | [datacircle/logiscape-mcp-tools](https://www.nuget.org/packages/datacircle%2Flogiscape-mcp-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. This package adds four tools to an MCP server made with… |
| 2026-11-25 01:07:03 | [edydeyemi/laravel-paystack](https://www.nuget.org/packages/edydeyemi%2Flaravel-paystack) | v1.0.0 | edydeyemi | A modern, fluent PHP/Laravel 13 package for integrating Paystack payments, subs… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
