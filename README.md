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

## Latest list — 2026-09-29 13:20 UTC

New packages created between 2026-09-29 12:22 UTC and 2026-09-29 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T13-20-31-568782Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 12:22:54 | [freento/base](https://www.nuget.org/packages/freento%2Fbase) | 1.0.0 |  | Base module for Freento extensions: shows installed Freento products with avail… |
| 2026-09-29 12:31:39 | [emirustaoglu/fmc](https://www.nuget.org/packages/emirustaoglu%2Ffmc) | 0.0.1 |  | A lightweight PHP client for Firebase Cloud Messaging (FCM) HTTP v1 API. |
| 2026-09-29 12:32:14 | [mdrbx/nova-mcp](https://www.nuget.org/packages/mdrbx%2Fnova-mcp) | v0.1.0 | Matthieu Deroubaix | Expose Laravel Nova resources to MCP clients through Nova's existing permission… |
| 2026-09-29 12:41:49 | [alexandrebulete/ddd-activity-bundle](https://www.nuget.org/packages/alexandrebulete%2Fddd-activity-bundle) | 1.0.0 | Alexandre Bulete | Activity journal as a reusable DDD building block — who did what, through which… |
| 2026-09-29 12:42:57 | [silunilabs/behat-cucumber-formatter](https://www.nuget.org/packages/silunilabs%2Fbehat-cucumber-formatter) | v0.1.0 |  | Behat 4 extension writing a Cucumber JSON report (with tags) |
| 2026-09-29 12:50:17 | [thelemon2020/pest-plugin-simulator](https://www.nuget.org/packages/thelemon2020%2Fpest-plugin-simulator) | v0.1.0 |  | Pest plugin that drives NativePHP screens on iOS Simulators and Android Emulato… |
| 2026-09-29 12:59:42 | [webx-ui/module-catalog](https://www.nuget.org/packages/webx-ui%2Fmodule-catalog) | v0.50.0 | WebX UI | A product catalogue for the WebX UI admin panel: products, a tree of categories… |
| 2026-09-29 13:09:03 | [baggins800/reverb-rs](https://www.nuget.org/packages/baggins800%2Freverb-rs) | v0.1.0 | Ruan Luies | Laravel integration for reverb-rs, a drop-in Rust replacement for the Laravel R… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
