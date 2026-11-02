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

## Latest list — 2026-11-02 11:19 UTC

New packages created between 2026-11-02 10:20 UTC and 2026-11-02 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T11-19-33-498991Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 10:30:57 | [eolica/laravel-cloudflare-turnstile](https://www.nuget.org/packages/eolica%2Flaravel-cloudflare-turnstile) | v0.1.0 | David Llobell | Cloudflare Turnstile integration for Laravel |
| 2026-11-02 10:35:57 | [owlframework/studio](https://www.nuget.org/packages/owlframework%2Fstudio) | v1.0.0 | Emmanuel Austin | A lightweight custom PHP MVC framework |
| 2026-11-02 10:47:56 | [hirasso/rh-free-layouts](https://www.nuget.org/packages/hirasso%2Frh-free-layouts) | 1.5.0 | Rasso Hilber | Free drag-and-drop layouts for ACF Flexible Content and Repeater fields |
| 2026-11-02 10:54:51 | [yu-dev/easyadminlte-bundle](https://www.nuget.org/packages/yu-dev%2Feasyadminlte-bundle) | v1.0.0 | Yuriy Akishin | AdminLTE 4 theme for EasyAdmin (Symfony bundle) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
