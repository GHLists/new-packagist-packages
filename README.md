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

## Latest list — 2026-11-21 10:20 UTC

New packages created between 2026-11-21 09:20 UTC and 2026-11-21 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T10-20-52-90488Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 10:11:36 | [login512/login512-laravel](https://www.nuget.org/packages/login512%2Flogin512-laravel) | 2.1.1 | Login512 Team | Official Laravel Package for Login512 Post-Quantum Biometrics and Passkeys |
| 2026-11-21 10:11:37 | [login512/login512-symfony-bundle](https://www.nuget.org/packages/login512%2Flogin512-symfony-bundle) | 2.1.1 | Login512 Team | Symfony bundle for Login512 (face login + passkeys): security authenticator, no… |
| 2026-11-21 10:11:37 | [login512/server-sdk](https://www.nuget.org/packages/login512%2Fserver-sdk) | v1.0.0 | login512.com | Official Login512 Server SDK for PHP (Post-Quantum Passwordless Face Authentica… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
