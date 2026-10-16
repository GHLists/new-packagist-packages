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

## Latest list — 2026-10-16 02:20 UTC

New packages created between 2026-10-16 01:21 UTC and 2026-10-16 02:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T02-20-42-552274Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 01:48:02 | [pieceofcake2/totp](https://www.nuget.org/packages/pieceofcake2%2Ftotp) | v1.0.0 |  | Two-factor authentication with time-based one-time passwords (TOTP, RFC 6238) f… |
| 2026-10-16 01:48:20 | [pieceofcake2/acl_menu](https://www.nuget.org/packages/pieceofcake2%2Facl_menu) | v1.0.0 | Mark Story | CakePHP 2 component that builds navigation menus of the actions a user may acce… |
| 2026-10-16 01:48:32 | [pieceofcake2/purifiable](https://www.nuget.org/packages/pieceofcake2%2Fpurifiable) | v1.0.0 | Jose Diaz-Gonzalez | CakePHP 2 behavior that sanitizes model data with HTML Purifier |
| 2026-10-16 02:04:33 | [janalis/bumpversion](https://www.nuget.org/packages/janalis%2Fbumpversion) | v0.1.0 |  | A PHP CLI to update version strings and prepare Git releases. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
