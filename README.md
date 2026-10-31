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

## Latest list — 2026-10-31 12:20 UTC

New packages created between 2026-10-31 11:18 UTC and 2026-10-31 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T12-20-37-705056Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 11:39:50 | [wilbere/bagisto-manual-payments](https://www.nuget.org/packages/wilbere%2Fbagisto-manual-payments) | v1.1.0 | wilbere | Pasarela de pagos manuales verificados (Pago Móvil, Transferencias, Zelle, Bina… |
| 2026-10-31 11:42:54 | [reirev/fastgtp](https://www.nuget.org/packages/reirev%2Ffastgtp) | v0.1.0 |  | PHP client for fastgtp, an HTTP API for Go engines and KataGo analysis. |
| 2026-10-31 11:45:01 | [tenma/redis](https://www.nuget.org/packages/tenma%2Fredis) | v0.1.0 |  | A Valkey server of the app's own on Tenma, for Redis clients: started next to t… |
| 2026-10-31 11:46:42 | [mistrfilda/amqp](https://www.nuget.org/packages/mistrfilda%2Famqp) | v0.1.0 |  | RabbitMQ integration with typed JSON messages, producers, consumers and Symfony… |
| 2026-10-31 11:54:15 | [qiyuanlabs/refit](https://www.nuget.org/packages/qiyuanlabs%2Frefit) | v0.1.0 | QiYuan Labs LLC | Check and fix PHP 8.x compatibility in WordPress plugins and plain PHP code, wi… |
| 2026-10-31 11:56:28 | [altayofficial/bedrockstructure](https://www.nuget.org/packages/altayofficial%2Fbedrockstructure) | 1.0.0+bedrock-1.26.… |  | Read, write and edit Minecraft Bedrock Edition .mcstructure files on Altay |
| 2026-10-31 12:11:14 | [survos/panorama-bundle](https://www.nuget.org/packages/survos%2Fpanorama-bundle) | v0.1.3 |  | Reusable panorama tours and historical photograph overlays for Symfony UX |
| 2026-10-31 12:11:28 | [facturalo-pe/facturalo-php](https://www.nuget.org/packages/facturalo-pe%2Ffacturalo-php) | v1.0.0 | Facturalo | SDK oficial de Facturalo para PHP: emite facturas, boletas, notas y guías de re… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
