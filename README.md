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

## Latest list — 2026-10-31 20:20 UTC

New packages created between 2026-10-31 19:21 UTC and 2026-10-31 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T20-20-33-55528Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 19:35:03 | [awcodes/panelist](https://www.nuget.org/packages/awcodes%2Fpanelist) | v1.0.0 | Adam Weston | A Filament plugin that turns a resource's list page into a master-detail editor… |
| 2026-10-31 19:40:18 | [webalternatif/temporal-bundle](https://www.nuget.org/packages/webalternatif%2Ftemporal-bundle) | v0.1.0 | Web\|Alternatif | A bundle to integrate Temporal workflows and activities into Symfony applicatio… |
| 2026-10-31 19:51:28 | [filippo-toso/wireguard-http](https://www.nuget.org/packages/filippo-toso%2Fwireguard-http) | v1.0.0 | Filippo Toso | Laravel-style HTTP client that sends requests through a WireGuard tunnel. |
| 2026-10-31 19:54:45 | [filippo-toso/wireguard-proxy](https://www.nuget.org/packages/filippo-toso%2Fwireguard-proxy) | v1.0.0 | Filippo Toso | Forward an HTTP request to a URL inside a WireGuard tunnel. |
| 2026-10-31 19:58:02 | [filippo-toso/wireguard-transport](https://www.nuget.org/packages/filippo-toso%2Fwireguard-transport) | 1.0.0 | Filippo Toso | PSR-18 HTTP client that sends requests through a userspace WireGuard tunnel. |
| 2026-10-31 20:04:59 | [faleh/shoppingcart](https://www.nuget.org/packages/faleh%2Fshoppingcart) | v3.5.0 | Rob Gloudemans; Faleh | Laravel Shoppingcart (fork hardevine/shoppingcart) dengan dukungan Laravel 10 s… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
