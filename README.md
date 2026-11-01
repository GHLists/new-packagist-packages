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

## Latest list — 2026-11-01 14:19 UTC

New packages created between 2026-11-01 13:19 UTC and 2026-11-01 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T14-19-25-311248Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-01 13:33:26 | [spkm/fortinac](https://www.nuget.org/packages/spkm%2Ffortinac) | v1.0.1 | Simon Mitchell | Integrate with the Fortinet FortiNAC-F REST API using SaloonPHP |
| 2026-11-01 13:33:47 | [marko/queue-redis](https://www.nuget.org/packages/marko%2Fqueue-redis) | 0.12.0 |  | Redis queue driver for Marko Framework |
| 2026-11-01 13:39:24 | [evolvaru/laravel-query-duplicates](https://www.nuget.org/packages/evolvaru%2Flaravel-query-duplicates) | v0.1.0 |  | Detect duplicated SQL queries and N+1 queries inside Laravel HTTP requests. |
| 2026-11-01 13:47:36 | [jelix/ldap-client](https://www.nuget.org/packages/jelix%2Fldap-client) | v1.0.0-beta.1 | Laurent Jouanneau | library to authenticate against an Ldap server or Active Directory. Users accou… |
| 2026-11-01 13:57:36 | [khurrambaig/hr-management](https://www.nuget.org/packages/khurrambaig%2Fhr-management) | v1.0.0 | Mirza Khurram Baig | HR management package: departments, employees, attendance, leaves and annual le… |
| 2026-11-01 14:15:15 | [dbout/wp-foundation](https://www.nuget.org/packages/dbout%2Fwp-foundation) | v1.0.0-rc.1 | Dimitri BOUTEILLE | Lightweight application foundation for WordPress: service container, attribute-… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
