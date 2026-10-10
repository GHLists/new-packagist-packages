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

## Latest list — 2026-10-10 04:22 UTC

New packages created between 2026-10-10 03:19 UTC and 2026-10-10 04:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T04-22-16-274358Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 03:33:53 | [pantosource/magento](https://www.nuget.org/packages/pantosource%2Fmagento) | 1.2.7 |  | PantoSource event tracking for Magento — canonical ingestion payloads, attribut… |
| 2026-10-10 03:40:55 | [mmuqiitf/filament-qr-code](https://www.nuget.org/packages/mmuqiitf%2Ffilament-qr-code) | v0.1.0 | Muhammad Muqiit Faturrahman | A powerful, modern QR code package for Filament v5 supporting generation, camer… |
| 2026-10-10 03:43:12 | [polaris/api-keys](https://www.nuget.org/packages/polaris%2Fapi-keys) | v0.9.0 | 2am.tech | API keys for Polaris for PHP: keys owned by users and organizations with a perm… |
| 2026-10-10 03:43:12 | [polaris/oauth-provider](https://www.nuget.org/packages/polaris%2Foauth-provider) | v0.9.0 | 2am.tech | Polaris for PHP as an OAuth 2.1 and OpenID Connect provider: authorization code… |
| 2026-10-10 03:51:03 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.5.0 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
