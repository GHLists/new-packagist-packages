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

## Latest list — 2026-10-05 07:20 UTC

New packages created between 2026-10-05 06:19 UTC and 2026-10-05 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T07-20-35-280974Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 06:20:35 | [stubbedev/atlassian-mcp](https://www.nuget.org/packages/stubbedev%2Fatlassian-mcp) | v0.5.24 |  | MCP server for self-hosted Jira and Bitbucket (Go, distributed as a prebuilt bi… |
| 2026-10-05 06:22:17 | [cyllene-digital/sylius-tarteaucitron-plugin](https://www.nuget.org/packages/cyllene-digital%2Fsylius-tarteaucitron-plugin) | v1.0.0 |  | tarteaucitron.js cookie consent manager for Sylius. |
| 2026-10-05 06:26:22 | [ianfoxdev/money-lint](https://www.nuget.org/packages/ianfoxdev%2Fmoney-lint) | v0.1.0 | Anatoly Pankratyev | PHPStan rules for code that moves money: floats in amounts, HTTP calls inside d… |
| 2026-10-05 06:48:00 | [openemail/sdk](https://www.nuget.org/packages/openemail%2Fsdk) | v0.0.1 | OpenEmail | The official PHP SDK for the OpenEmail API. Send email and broadcasts, work wit… |
| 2026-10-05 06:50:44 | [joydeep-bhowmik/quire](https://www.nuget.org/packages/joydeep-bhowmik%2Fquire) | v0.1.1 | Joydeep Bhowmik | File-based page router for plain PHP: every .php or .blade.php file is a route,… |
| 2026-10-05 06:51:57 | [russelcruz28/filament-demo-mode](https://www.nuget.org/packages/russelcruz28%2Ffilament-demo-mode) | v0.1.0 | Russelcruz28 | Persistent SQLite demo sandboxes, role switching, and production-data isolation… |
| 2026-10-05 06:52:49 | [mage2kishan/module-redirects](https://www.nuget.org/packages/mage2kishan%2Fmodule-redirects) | 1.2.6 |  | Redirects and 404 management for Magento 2 (Hyva + Luma). Manual + auto redirec… |
| 2026-10-05 06:56:36 | [mohan-devstack/magento2-guest-order-to-customer](https://www.nuget.org/packages/mohan-devstack%2Fmagento2-guest-order-to-customer) | 1.0.0 | Mohan Prabhu | Map Magento 2 guest orders to an existing customer account with the same email,… |
| 2026-10-05 07:00:51 | [stubbedev/ds-mcp](https://www.nuget.org/packages/stubbedev%2Fds-mcp) | v0.3.15 |  | DataStore MCP — one MCP server for MySQL/MariaDB, PostgreSQL, SQLite, DuckDB, S… |
| 2026-10-05 07:05:58 | [janprikryl/revolutx](https://www.nuget.org/packages/janprikryl%2Frevolutx) | 0.0.6 | Jan Přikryl | PHP SDK for the Revolut X Crypto Exchange REST API (v1.0) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
