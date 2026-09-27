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

## Latest list — 2026-09-27 15:21 UTC

New packages created between 2026-09-27 14:21 UTC and 2026-09-27 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-27T15-21-29-610267Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-27 14:34:29 | [mammatus/healthz-vhost](https://www.nuget.org/packages/mammatus%2Fhealthz-vhost) | 0.1.0 |  | ⚕️ Basic health check vhost |
| 2026-09-27 14:54:24 | [zemkogabor/xinfra-php](https://www.nuget.org/packages/zemkogabor%2Fxinfra-php) | v1.0.0 |  | PHP client for sending logs and errors to xInfra. |
| 2026-09-27 14:56:05 | [webx-ui/module-team](https://www.nuget.org/packages/webx-ui%2Fmodule-team) | v0.45.0 | WebX UI | The team for the WebX UI admin panel: people with a photo, a name, a job title,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
