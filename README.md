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

## Latest list — 2026-11-08 17:19 UTC

New packages created between 2026-11-08 16:20 UTC and 2026-11-08 17:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T17-19-18-461667Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 16:22:29 | [nowo-tech/mcp-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fmcp-kit-bundle) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Model Context Protocol (MCP) server for Symfony: stateless Streamable HTTP (JSO… |
| 2026-11-08 16:52:19 | [class-atlas/laravel-flitt](https://www.nuget.org/packages/class-atlas%2Flaravel-flitt) | v1.0.0-beta.1 | Irakli Kirkitadze | Laravel client for the Flitt payment gateway: hosted checkout, order status, re… |
| 2026-11-08 17:00:25 | [particle-academy/twilio-php](https://www.nuget.org/packages/particle-academy%2Ftwilio-php) | v0.1.0 | Particle Academy | Twilio for PHP — the service descriptor, its faker, its webhook verification, o… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
