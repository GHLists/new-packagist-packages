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

## Latest list — 2026-10-09 01:20 UTC

New packages created between 2026-10-09 00:19 UTC and 2026-10-09 01:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T01-20-24-094108Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 00:20:37 | [edulazaro/php-pop3](https://www.nuget.org/packages/edulazaro%2Fphp-pop3) | 1.1.0 | Edu Lazaro | A POP3 client in plain PHP: SSL or STARTTLS, certificate checks you control, pa… |
| 2026-10-09 00:36:57 | [jgamboa/laravel-aurora-dsql](https://www.nuget.org/packages/jgamboa%2Flaravel-aurora-dsql) | v0.1.1 | Joaquín Gamboa | Laravel driver for Amazon Aurora DSQL: IAM token auth, DSQL-compatible schema b… |
| 2026-10-09 01:09:51 | [units/hasher](https://www.nuget.org/packages/units%2Fhasher) | v1.0.0 |  | Hashing unit - native digests, HMAC and timing-safe comparison, on the patterns… |
| 2026-10-09 01:10:36 | [units/password](https://www.nuget.org/packages/units%2Fpassword) | v1.0.0 |  | Password-hashing unit - Argon2id, Argon2i and bcrypt via PHP's password_* funct… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
