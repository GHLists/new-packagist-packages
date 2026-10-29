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

## Latest list — 2026-10-29 20:22 UTC

New packages created between 2026-10-29 19:19 UTC and 2026-10-29 20:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T20-22-07-082958Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 19:23:50 | [sahilphp/installer](https://www.nuget.org/packages/sahilphp%2Finstaller) | v1.0.1 | Idrisa John | SahilPHP Installer - Creates new SahilPHP projects with Tailwind CSS or Bootstr… |
| 2026-10-29 19:24:22 | [folklore/laravel-eclair](https://www.nuget.org/packages/folklore%2Flaravel-eclair) | v0.1.0 | Folklore; David Mongeau-Petit… | Laravel client for Eclair, the self-hosted media processing server |
| 2026-10-29 19:31:02 | [mailvex/mailvex-php](https://www.nuget.org/packages/mailvex%2Fmailvex-php) | v1.0.1 | Mailvex Team | Official PHP & Laravel SDK for Mailvex Email Infrastructure. Supports single &… |
| 2026-10-29 19:49:40 | [pikoman/compat-laravel](https://www.nuget.org/packages/pikoman%2Fcompat-laravel) | 0.2.0 |  | A Laravel broadcast driver for Pikoman: Laravel Echo with @pikoman/compat, sign… |
| 2026-10-29 19:52:28 | [blackairplane/skylock-laravel](https://www.nuget.org/packages/blackairplane%2Fskylock-laravel) | v0.1.0 | Black Airplane | Reports a Laravel app's health and scheduled tasks to SkyLock, Black Airplane's… |
| 2026-10-29 20:14:05 | [pikoman/compat-php](https://www.nuget.org/packages/pikoman%2Fcompat-php) | 0.1.0 |  | Pusher's PHP library (pusher/pusher-php-server) on Pikoman: the same trigger, t… |
| 2026-10-29 20:18:24 | [larasell-dev/extension-starter-kit](https://www.nuget.org/packages/larasell-dev%2Fextension-starter-kit) | v0.1.0 |  | A Larasell extension |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
