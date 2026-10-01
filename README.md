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

## Latest list — 2026-10-01 15:22 UTC

New packages created between 2026-10-01 14:18 UTC and 2026-10-01 15:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T15-22-04-817133Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 14:28:45 | [kevinpirnie/kpt-database](https://www.nuget.org/packages/kevinpirnie%2Fkpt-database) | v1.2.16 | Kevin Pirnie | A modern, fluent PHP database wrapper built on top of PDO, providing an elegant… |
| 2026-10-01 14:32:03 | [robertboes/laravel-cloudflare-proxies](https://www.nuget.org/packages/robertboes%2Flaravel-cloudflare-proxies) | v0.1.1 | Robert Boes | Trust Cloudflare's published ranges and the private proxy hop, so the client IP… |
| 2026-10-01 14:32:26 | [philipstuessel/deploy-machine](https://www.nuget.org/packages/philipstuessel%2Fdeploy-machine) | v1.2.1 |  | Deploys a folder to a server. One bash script, one config file. |
| 2026-10-01 14:32:56 | [migears/mail](https://www.nuget.org/packages/migears%2Fmail) | 2.0.0 |  | Minimalist mail sending library with native mail() and SMTP support |
| 2026-10-01 14:35:41 | [reshapify/sendseven](https://www.nuget.org/packages/reshapify%2Fsendseven) | v0.1.2 | Richard Bowen | Unofficial. A typed, fully documented PHP SDK for the SendSeven messaging API:… |
| 2026-10-01 14:42:35 | [se7enxweb/expui](https://www.nuget.org/packages/se7enxweb%2Fexpui) | v1.0.0.0 | 7x | Exponential UI: the jQuery 4 API (Exp.*) that delivers the admin's and the site… |
| 2026-10-01 14:43:28 | [reshapify/sendseven-laravel](https://www.nuget.org/packages/reshapify%2Fsendseven-laravel) | v0.1.0 | Richard Bowen | Unofficial. SendSeven for Laravel: configured client, verified webhooks as Lara… |
| 2026-10-01 14:56:39 | [digit7s/filament-view-website](https://www.nuget.org/packages/digit7s%2Ffilament-view-website) | 1.0.0 | Myo Min Oo | A lightweight Filament 5 panel plugin that adds a configurable Visit Website ac… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
