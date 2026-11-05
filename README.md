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

## Latest list — 2026-11-05 11:21 UTC

New packages created between 2026-11-05 10:22 UTC and 2026-11-05 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T11-21-39-55983Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 10:25:03 | [ihsan/umm-alqura-prayer-times](https://www.nuget.org/packages/ihsan%2Fumm-alqura-prayer-times) | v0.1.0 |  | Offline PHP library for Islamic prayer (adhan) times using the official Umm al-… |
| 2026-11-05 10:52:23 | [dpezer/silverstripe-remote-assets](https://www.nuget.org/packages/dpezer%2Fsilverstripe-remote-assets) | 1.0.0 | Darjan Pezer | Serve missing asset files from a remote Silverstripe site on the frontend, with… |
| 2026-11-05 10:59:29 | [elgentos/m2-vatfallback-graph-ql](https://www.nuget.org/packages/elgentos%2Fm2-vatfallback-graph-ql) | 1.0.0 | Sander Jongsma | Provides graph ql endpoint to dutchento/m2-vatfallback |
| 2026-11-05 11:09:47 | [nmirceac/sms-tools-2](https://www.nuget.org/packages/nmirceac%2Fsms-tools-2) | 0.0.3 | Mircea Nicolae | Laravel client for the WeAnswer SMS Toolkit (API v2): send SMS, track delivery… |
| 2026-11-05 11:17:25 | [ibexa/doctrine-migrations](https://www.nuget.org/packages/ibexa%2Fdoctrine-migrations) | v4.6.33 |  | Symfony Bundle providing service-based Doctrine Migrations infrastructure for I… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
