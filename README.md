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

## Latest list — 2026-11-27 09:19 UTC

New packages created between 2026-11-27 08:21 UTC and 2026-11-27 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T09-19-07-674406Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 08:38:16 | [clesson-de/silverstripe-qr-code](https://www.nuget.org/packages/clesson-de%2Fsilverstripe-qr-code) | 1.0.0 |  | A public React QR code generator with SVG/PNG downloads, a page type and option… |
| 2026-11-27 08:42:55 | [ixbox/wristband](https://www.nuget.org/packages/ixbox%2Fwristband) | v0.2.0 |  | Verify user identity passed by an authenticating edge (AWS ALB x-amzn-oidc-data… |
| 2026-11-27 08:44:01 | [ixbox/laravel-wristband](https://www.nuget.org/packages/ixbox%2Flaravel-wristband) | v0.2.0 |  | Laravel guard that authenticates users from an authenticating edge: AWS ALB (x-… |
| 2026-11-27 08:45:10 | [loki-checkout/magento2-ca](https://www.nuget.org/packages/loki-checkout%2Fmagento2-ca) | 1.0.0 |  | Canadian settings for LokiCheckout |
| 2026-11-27 08:46:21 | [loki-checkout/magento2-ch](https://www.nuget.org/packages/loki-checkout%2Fmagento2-ch) | 1.0.0 |  | Swiss settings for LokiCheckout |
| 2026-11-27 08:49:08 | [bifrost-mz/pulse-laravel](https://www.nuget.org/packages/bifrost-mz%2Fpulse-laravel) | v1.0.0 |  | Automatic Pulse feedback widget and error monitoring for Laravel |
| 2026-11-27 08:59:59 | [craftcms/wp-import](https://www.nuget.org/packages/craftcms%2Fwp-import) | 1.0.0 | Pixel & Tonic | WordPress → Craft CMS content importer |
| 2026-11-27 09:12:52 | [santa77/peppol-dir](https://www.nuget.org/packages/santa77%2Fpeppol-dir) | v0.2.0 |  | Live Peppol recipient lookup for Slovak DIČ and company names |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
