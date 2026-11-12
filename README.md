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

## Latest list — 2026-11-12 02:21 UTC

New packages created between 2026-11-12 01:19 UTC and 2026-11-12 02:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T02-21-50-604026Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 01:37:11 | [laranail/waitlist-kit](https://www.nuget.org/packages/laranail%2Fwaitlist-kit) | v0.1.0 | Simtabi LLC; Imani Manyara | Waitlists, coming-soon and early-access pages for Laravel: lead capture and con… |
| 2026-11-12 01:39:15 | [laranail/waitlist-starter](https://www.nuget.org/packages/laranail%2Fwaitlist-starter) | v0.1.0 | Simtabi LLC; Imani Manyara | A Laravel app that runs laranail/waitlist-kit: a waitlist, coming-soon or early… |
| 2026-11-12 01:55:36 | [php-io-extensions/soloud](https://www.nuget.org/packages/php-io-extensions%2Fsoloud) | v0.11.0 | Project Saturn Studios, LLC | 1:1 PHP bindings of the SoLoud C++ audio engine, with the library compiled into… |
| 2026-11-12 02:05:35 | [s3rgiosan/divi-migration](https://www.nuget.org/packages/s3rgiosan%2Fdivi-migration) | 1.0.0 | Sérgio Santos | Convert Divi Builder content to blocks. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
