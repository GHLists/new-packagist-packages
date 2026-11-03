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

## Latest list — 2026-11-03 16:18 UTC

New packages created between 2026-11-03 15:19 UTC and 2026-11-03 16:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T16-18-46-258084Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 15:22:07 | [omaacha/2fa](https://www.nuget.org/packages/omaacha%2F2fa) | v1.0.0 | Otmane Maacha | Multi-Factor Authentication (TOTP, Multi-Channel OTP, Recovery Codes, Trusted D… |
| 2026-11-03 15:23:04 | [scrapfly/scrapfly-sdk](https://www.nuget.org/packages/scrapfly%2Fscrapfly-sdk) | v0.0.1 | Scrapfly | Official PHP SDK for the Scrapfly platform: web scraping, screenshots, AI extra… |
| 2026-11-03 15:28:10 | [dlundgren/phagrancy](https://www.nuget.org/packages/dlundgren%2Fphagrancy) | 1.0.0 | David Lundgren | Private Vagrant Cloud |
| 2026-11-03 15:36:33 | [chrismou/streamseal](https://www.nuget.org/packages/chrismou%2Fstreamseal) | 0.1.0 | Chris Chrisostomou | Streaming authenticated file encryption for PHP on libsodium secretstream (XCha… |
| 2026-11-03 15:52:53 | [alvesbeto/mysql2i](https://www.nuget.org/packages/alvesbeto%2Fmysql2i) | v1.0.1 | Beto Souza | Legacy mysql_* functions for PHP 8+, implemented on ext-mysqli (compatibility s… |
| 2026-11-03 16:01:44 | [justbetter/magento2-sentry-logrocket](https://www.nuget.org/packages/justbetter%2Fmagento2-sentry-logrocket) | 1.0.0 | JustBetter B.V. | Magento 2 LogRocket integration for JustBetter Sentry |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
