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

## Latest list — 2026-10-07 17:21 UTC

New packages created between 2026-10-07 16:23 UTC and 2026-10-07 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T17-21-50-965813Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 17:01:26 | [adeguntoro/j2fakit](https://www.nuget.org/packages/adeguntoro%2Fj2fakit) | v1.0.0 | adeguntoro | 2FA gate package: by default every route requires login+2FA, whitelist via conf… |
| 2026-10-07 17:01:40 | [malevich/malevich](https://www.nuget.org/packages/malevich%2Fmalevich) | 1.0.0 | chipslays | Variant-driven Blade components: declare class maps, render them with @ui. |
| 2026-10-07 17:13:47 | [jeffersongoncalves/filament-saml2](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-saml2) | 3.0.0 | Jefferson Gonçalves | Filament 5 plugin for SAML2 single sign-on with multi-tenant Identity Providers… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
