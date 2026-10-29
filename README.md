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

## Latest list — 2026-10-29 11:19 UTC

New packages created between 2026-10-29 10:20 UTC and 2026-10-29 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T11-19-51-991086Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 10:29:03 | [astral-php/astral-cache](https://www.nuget.org/packages/astral-php%2Fastral-cache) | 0.1.0 | astral-php | Cache multi-drivers opt-in pour Astral — array, file, Redis/Memcache (extension… |
| 2026-10-29 10:31:43 | [sandstorm/backendusermanagement](https://www.nuget.org/packages/sandstorm%2Fbackendusermanagement) | 1.0.0 |  | Backend User Management Package for Neos, includes 2FA, password reset, new use… |
| 2026-10-29 10:52:55 | [bernskiold/laravel-snowflake](https://www.nuget.org/packages/bernskiold%2Flaravel-snowflake) | 0.1.0 | Bernskiold | Snowflake database driver for Laravel, supporting both the native pdo_snowflake… |
| 2026-10-29 10:53:57 | [klimadashboard/typo3-klimadashboard](https://www.nuget.org/packages/klimadashboard%2Ftypo3-klimadashboard) | 1.0.0 | Klimadashboard | Embed charts from Klimadashboard (klimadashboard.de / .at / .org) as TYPO3 cont… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
