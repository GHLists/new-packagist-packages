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

## Latest list — 2026-10-14 09:22 UTC

New packages created between 2026-10-14 08:19 UTC and 2026-10-14 09:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T09-22-29-96086Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 08:19:32 | [szenario/craft-embedded-posters](https://www.nuget.org/packages/szenario%2Fcraft-embedded-posters) | 1.0.0 |  | Local poster images for Embedded Assets embeds, so cookie-consent placeholders… |
| 2026-10-14 08:21:09 | [dskripchenko/laravel-admin-oidc](https://www.nuget.org/packages/dskripchenko%2Flaravel-admin-oidc) | v0.1.0 | Denis Skripchenko | Sign in to dskripchenko/laravel-admin panels with OpenID Connect — Keycloak, Mi… |
| 2026-10-14 08:35:52 | [tratto/email](https://www.nuget.org/packages/tratto%2Femail) | v1.0.0 |  | Official PHP SDK for the Tratto email API |
| 2026-10-14 08:45:31 | [wamesk/laravel-nova-action-toolbar](https://www.nuget.org/packages/wamesk%2Flaravel-nova-action-toolbar) | 5.0.0 |  | Choose per Laravel Nova action how it is shown: a button, an icon or the ⋯ menu… |
| 2026-10-14 08:51:18 | [cosmira/soda](https://www.nuget.org/packages/cosmira%2Fsoda) | v1.0.0 | Alexandr Chernyaev | Keep your PHP code clean and maintainable by enforcing quality rules based on m… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
