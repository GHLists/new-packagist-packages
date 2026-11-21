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

## Latest list — 2026-11-21 19:19 UTC

New packages created between 2026-11-21 18:21 UTC and 2026-11-21 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T19-19-13-427725Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 18:29:15 | [ebln/psr7-symfony1-bridge](https://www.nuget.org/packages/ebln%2Fpsr7-symfony1-bridge) | v0.2.0 | ebln | Converts between symfony1 request and response objects and PSR-7 messages |
| 2026-11-21 18:37:00 | [kladero/veratag-typo3-extension](https://www.nuget.org/packages/kladero%2Fveratag-typo3-extension) | v1.0.0 | Kladero GmbH | vera[tag] - Synchronize disclosure data from vera[tag], manage your integration… |
| 2026-11-21 18:38:03 | [simplygoodwork/craft-dolly](https://www.nuget.org/packages/simplygoodwork%2Fcraft-dolly) | 5.0.0-beta.1 |  | Easily port content from one environment to another. |
| 2026-11-21 18:48:27 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.43.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-21 18:54:42 | [loki-checkout/magento2-indian-gst](https://www.nuget.org/packages/loki-checkout%2Fmagento2-indian-gst) | 1.0.0 |  | Indian GST number field for Loki Checkout |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
