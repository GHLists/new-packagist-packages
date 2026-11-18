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

## Latest list — 2026-11-18 19:22 UTC

New packages created between 2026-11-18 18:21 UTC and 2026-11-18 19:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T19-22-07-322069Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 18:29:52 | [westmschools/hello-wizard-of-oz](https://www.nuget.org/packages/westmschools%2Fhello-wizard-of-oz) | v1.0.0 |  | Tornado Engine module: a random Wizard of Oz quote in the header of every page,… |
| 2026-11-18 18:31:15 | [numencode/wn-syncops-plugin](https://www.nuget.org/packages/numencode%2Fwn-syncops-plugin) | v2.0.1 | Blaz Orazem | Deployment, synchronization and backup commands for Winter CMS: deploy via Git,… |
| 2026-11-18 18:31:18 | [numencode/wn-dropboxadapter-plugin](https://www.nuget.org/packages/numencode%2Fwn-dropboxadapter-plugin) | v2.0.1 | Blaz Orazem | Dropbox (API v2) filesystem disk for Winter CMS with OAuth2 refresh tokens and… |
| 2026-11-18 19:01:10 | [woocommerce/extension-changelogger](https://www.nuget.org/packages/woocommerce%2Fextension-changelogger) | v1.0.0 |  | Jetpack Changelogger formatter for the WooCommerce extension changelog format |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
