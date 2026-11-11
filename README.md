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

## Latest list — 2026-11-11 08:20 UTC

New packages created between 2026-11-11 07:20 UTC and 2026-11-11 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-11T08-20-08-848944Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 07:46:52 | [fiskit/fiskit-php](https://www.nuget.org/packages/fiskit%2Ffiskit-php) | v0.1.0 |  | Official PHP client for the FisKit API: Argentine electronic invoices with ARCA… |
| 2026-11-11 07:50:10 | [garak/sf-dep](https://www.nuget.org/packages/garak%2Fsf-dep) | v0.1.0 | Massimiliano Arione | Shared Deployer recipe for Symfony projects |
| 2026-11-11 07:56:17 | [totalcms/starter-realtor](https://www.nuget.org/packages/totalcms%2Fstarter-realtor) | v1.0.0 | Joe Workman | Valeria Montoya: a real estate agent's site for Total CMS, in English and Spani… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
