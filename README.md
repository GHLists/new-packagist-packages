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

## Latest list — 2026-10-14 03:22 UTC

New packages created between 2026-10-14 02:19 UTC and 2026-10-14 03:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T03-22-43-609701Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 02:38:58 | [versawys/kernel](https://www.nuget.org/packages/versawys%2Fkernel) | v2.2.0 | Jorge Jara H. | Núcleo del framework versaWYS-PHP: enrutamiento, middlewares, sesión/JWT, Twig,… |
| 2026-10-14 02:53:20 | [snebes/newrelic-zts](https://www.nuget.org/packages/snebes%2Fnewrelic-zts) | v12.6.0.34 |  | Unofficial ZTS (thread-safe) build of the New Relic PHP agent extension for Fra… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
