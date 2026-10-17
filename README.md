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

## Latest list — 2026-10-17 04:20 UTC

New packages created between 2026-10-17 03:20 UTC and 2026-10-17 04:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T04-20-28-531951Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 03:29:23 | [panelsso/pterodactyl](https://www.nuget.org/packages/panelsso%2Fpterodactyl) | v1.0.0 |  | Single sign-on bridge that lets your clients log into their Pterodactyl panel a… |
| 2026-10-17 03:57:13 | [daemonlabs/shield-oidc](https://www.nuget.org/packages/daemonlabs%2Fshield-oidc) | v1.0.0 | Daemon Labs | OpenID Connect single sign-on for CodeIgniter Shield: Microsoft Entra ID, Okta,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
