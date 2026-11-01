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

## Latest list — 2026-11-01 03:19 UTC

New packages created between 2026-11-01 02:21 UTC and 2026-11-01 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T03-19-20-105493Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 02:21:14 | [wodzy/cakephp-disposable-email](https://www.nuget.org/packages/wodzy%2Fcakephp-disposable-email) | v1.0.1 | Walid Oukaci | CakePHP plugin that blocks disposable (throwaway) email addresses, powered by w… |
| 2026-11-01 02:40:02 | [webware/asciidoc-php](https://www.nuget.org/packages/webware%2Fasciidoc-php) | 0.1.0 | Joey (aka Tyrsson) Smith | A PHP port of the Asciidoctor toolchain that converts AsciiDoc source files to… |
| 2026-11-01 02:41:37 | [hamada-emam-tech/einvoice-eta](https://www.nuget.org/packages/hamada-emam-tech%2Feinvoice-eta) | v0.1.0 |  | Egypt ETA eInvoicing for hamada-emam-tech/einvoice: the v1.0 JSON document, ETA… |
| 2026-11-01 02:41:38 | [hamada-emam-tech/einvoice-keysource-agent](https://www.nuget.org/packages/hamada-emam-tech%2Feinvoice-keysource-agent) | v0.1.0 |  | A KeySource for hamada-emam-tech/einvoice that signs with a USB token or HSM th… |
| 2026-11-01 02:46:30 | [oocscommerce/magento2-souin-cache](https://www.nuget.org/packages/oocscommerce%2Fmagento2-souin-cache) | 1.0.0 |  | Souin (Caddy cache-handler) full page cache application for Magento 2 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
