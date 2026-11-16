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

## Latest list — 2026-11-16 22:19 UTC

New packages created between 2026-11-16 21:19 UTC and 2026-11-16 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T22-19-01-7385Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 21:23:07 | [hyphaeworks/nullable-embeddable-bundle](https://www.nuget.org/packages/hyphaeworks%2Fnullable-embeddable-bundle) | 1.0.0 | Wolfgang Klinger | Symfony bundle for handling nullable Doctrine embeddables |
| 2026-11-16 21:24:53 | [nmirceac/mailchecker-tools](https://www.nuget.org/packages/nmirceac%2Fmailchecker-tools) | 0.0.2 | Mircea Nicolae | Laravel client for the WeAnswer Mail Checker (API v2): check email addresses (s… |
| 2026-11-16 21:35:53 | [xddesigners/silverstripe-event-tickets-discounts](https://www.nuget.org/packages/xddesigners%2Fsilverstripe-event-tickets-discounts) | 6.0.0 | Remy Vaartjes | Discount module for SilverStripe Event Tickets |
| 2026-11-16 21:40:45 | [flashpi/flashpi-laravel](https://www.nuget.org/packages/flashpi%2Fflashpi-laravel) | v0.1.0 | SIGNIADIGITAL S.A. | The official Laravel package for Flashpi, the electronic invoicing API for Ecua… |
| 2026-11-16 21:44:37 | [jeffersongoncalves/filament-lgpd-dsar](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-lgpd-dsar) | 3.0.0 | Jefferson Gonçalves | Filament plugin to handle LGPD data subject requests (art. 18): verify, export,… |
| 2026-11-16 22:14:01 | [jolimardi/filament-focal-point](https://www.nuget.org/packages/jolimardi%2Ffilament-focal-point) | 1.0.0 | Joli Mardi | Point focal pour les images de la media library Spatie dans Filament : choisi e… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
