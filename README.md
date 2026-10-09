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

## Latest list — 2026-10-09 21:20 UTC

New packages created between 2026-10-09 20:20 UTC and 2026-10-09 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T21-20-34-099018Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 20:35:11 | [b44x/edoreczenia](https://www.nuget.org/packages/b44x%2Fedoreczenia) | v0.1.0 | Michell Hoduń | Unofficial, framework-agnostic PHP SDK for the Polish e-Doręczenia (e-Delivery)… |
| 2026-10-09 20:39:13 | [asignua/filament-image-annotations](https://www.nuget.org/packages/asignua%2Ffilament-image-annotations) | v1.1.0 | Mykhailo Hladchenko | Non-destructive vector annotations for Filament 5: arrows, rectangles, ellipses… |
| 2026-10-09 20:45:22 | [abangateway/abangateway-php-package](https://www.nuget.org/packages/abangateway%2Fabangateway-php-package) | v1.0.0 | AbanGateway | AbanGateway card-to-card payment gateway for PHP and Laravel: invoices with aut… |
| 2026-10-09 20:46:35 | [romanfedorskij/cron](https://www.nuget.org/packages/romanfedorskij%2Fcron) | v0.1.0-rc.1 | Roman Fedorskij | Non-blocking cron scheduler with forked PHP workers |
| 2026-10-09 20:50:40 | [evopixel/socialiteproviders-minecraft-evopixel](https://www.nuget.org/packages/evopixel%2Fsocialiteproviders-minecraft-evopixel) | 1.0.0 | EvoPixel | Minecraft EvoPixel OAuth2 provider for Laravel Socialite |
| 2026-10-09 21:08:02 | [nhanaz/blockdata](https://www.nuget.org/packages/nhanaz%2Fblockdata) | v1.0.1 |  | A virion for persistent JSON data attached to blocks on Axolotl-PM |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
