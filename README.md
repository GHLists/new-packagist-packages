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

## Latest list — 2026-10-30 01:20 UTC

New packages created between 2026-10-30 00:21 UTC and 2026-10-30 01:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T01-20-11-789089Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 01:00:07 | [tacraft-social-guild/flarum-login-screen](https://www.nuget.org/packages/tacraft-social-guild%2Fflarum-login-screen) | 1.0.0 | TCS Dev HUB | Customize the login screen for your Flarum forum. |
| 2026-10-30 01:03:31 | [ez-php/encryption](https://www.nuget.org/packages/ez-php%2Fencryption) | 2.6.4 | Andreas Uretschnig | Symmetric authenticated encryption (ext-sodium XChaCha20-Poly1305) with key rot… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
