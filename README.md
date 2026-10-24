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

## Latest list — 2026-10-24 00:20 UTC

New packages created between 2026-10-23 23:20 UTC and 2026-10-24 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T00-20-01-10441Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 23:47:53 | [ez-php/graphql-subscriptions](https://www.nuget.org/packages/ez-php%2Fgraphql-subscriptions) | 2.6.0 | Andreas Uretschnig | GraphQL subscriptions over ez-php/websocket (graphql-transport-ws), fed by ez-p… |
| 2026-10-23 23:47:54 | [ez-php/psr-bridge](https://www.nuget.org/packages/ez-php%2Fpsr-bridge) | 2.6.0 | Andreas Uretschnig | Adapters between ez-php HTTP/logging types and PSR-7, PSR-15, PSR-17 and PSR-3 |
| 2026-10-23 23:50:31 | [3neti/x-deploy](https://www.nuget.org/packages/3neti%2Fx-deploy) | v1.0.0 | Lester B. Hurtado | Release compatibility, commissioning, and deployment telemetry for x-change hos… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
