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

## Latest list — 2026-10-05 06:19 UTC

New packages created between 2026-10-05 05:21 UTC and 2026-10-05 06:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T06-19-17-204158Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 05:25:27 | [contenir/errors-mezzio](https://www.nuget.org/packages/contenir%2Ferrors-mezzio) | v0.1.0 |  | Mezzio (PSR-15) adapter for contenir/errors — renders admin-authored per-status… |
| 2026-10-05 05:26:17 | [wentthefox/services_libravatar](https://www.nuget.org/packages/wentthefox%2Fservices_libravatar) | v1.0.5 | Melissa Draper; Christian Wei… | API interfacing class for libravatar.org |
| 2026-10-05 05:42:53 | [patterns/unit](https://www.nuget.org/packages/patterns%2Funit) | v1.0.0 |  | Unit pattern - a named, versioned identity for code that produces data, so ever… |
| 2026-10-05 05:50:28 | [contenir/contenir-db-model-tools](https://www.nuget.org/packages/contenir%2Fcontenir-db-model-tools) | v1.0.0-rc1 |  | Command-line tools for contenir-db-model: generate entities from live tables, u… |
| 2026-10-05 05:50:58 | [mage2kishan/module-sale-filter](https://www.nuget.org/packages/mage2kishan%2Fmodule-sale-filter) | 1.1.5 | Kishan Savaliya | Panth Sale Filter — "On Sale" layered navigation filter for Magento 2, backed b… |
| 2026-10-05 05:58:50 | [units/logger](https://www.nuget.org/packages/units%2Flogger) | v1.0.0 |  | Log unit - a versioned logging identity that writes through an injected adapter… |
| 2026-10-05 06:05:43 | [stubbedev/jenkins-mcp](https://www.nuget.org/packages/stubbedev%2Fjenkins-mcp) | v0.2.6 |  | MCP server for Jenkins build status and logs (Go, distributed as a prebuilt bin… |
| 2026-10-05 06:07:29 | [stubbedev/sentry-mcp](https://www.nuget.org/packages/stubbedev%2Fsentry-mcp) | v0.2.8 |  | MCP server for self-hosted Sentry (Go, distributed as a prebuilt binary) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
