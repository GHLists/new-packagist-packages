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

## Latest list — 2026-10-18 01:21 UTC

New packages created between 2026-10-18 00:21 UTC and 2026-10-18 01:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T01-21-44-602071Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 00:24:59 | [1994/cookie-connect-core](https://www.nuget.org/packages/1994%2Fcookie-connect-core) | v1.0.0 | 1994 | The framework-free core shared by Cookie Connect for Craft CMS and Statamic: ev… |
| 2026-10-18 00:29:34 | [verisec/verisec-php](https://www.nuget.org/packages/verisec%2Fverisec-php) | 1.0.0 | VeriSec Labs | The official PHP library for the VeriSec API: identity (KYC) and Financial chec… |
| 2026-10-18 00:34:49 | [1994/cookie-connect-craft](https://www.nuget.org/packages/1994%2Fcookie-connect-craft) | v1.0.1 | 1994 | Connect your site to the cookie consent platform you already use: paste its ID,… |
| 2026-10-18 00:34:55 | [1994/cookie-connect-statamic](https://www.nuget.org/packages/1994%2Fcookie-connect-statamic) | v1.0.1 | 1994 | Connect your site to the cookie consent platform you already use: paste its ID,… |
| 2026-10-18 00:43:13 | [acephp/ace](https://www.nuget.org/packages/acephp%2Face) | v1.0.0 | Celionatti | A lightweight, high-performance PHP 8.2+ MVC framework with Active Record, Mult… |
| 2026-10-18 00:43:59 | [geisonq/jh2pdf](https://www.nuget.org/packages/geisonq%2Fjh2pdf) | v1.0.0 | Geison Quevedo | Pixel-perfect HTML to PDF in PHP without a browser on the server: the user's br… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
