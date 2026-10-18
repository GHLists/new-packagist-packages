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

## Latest list — 2026-10-18 16:21 UTC

New packages created between 2026-10-18 15:20 UTC and 2026-10-18 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T16-21-26-495741Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 15:24:27 | [intosql/intosql](https://www.nuget.org/packages/intosql%2Fintosql) | v0.1.0 | IntoSQL | Convert spreadsheets, CSV and JSON into SQL with the IntoSQL API. |
| 2026-10-18 15:27:31 | [86hc/hk-company-registry-validator](https://www.nuget.org/packages/86hc%2Fhk-company-registry-validator) | v1.0.2 | HC BUSINESS LIMITED (86HC Com… | Lightweight validator & format parser for Hong Kong Company Registration Number… |
| 2026-10-18 15:34:43 | [eighteen73/wordpress-challenge](https://www.nuget.org/packages/eighteen73%2Fwordpress-challenge) | v0.1.0 |  | Opinionated CAPTCHA protection for WordPress |
| 2026-10-18 15:43:21 | [heinhtet/api-authorizer](https://www.nuget.org/packages/heinhtet%2Fapi-authorizer) | v1.0.0 | Hein Htet | Protect Laravel APIs with HMAC-SHA256 request signing headers (X-POWERED-BY, X-… |
| 2026-10-18 15:54:07 | [filagora/filagora-memberships](https://www.nuget.org/packages/filagora%2Ffilagora-memberships) | v0.1.1 |  | Memberships and billing for Filagora: plans, prices, member subscriptions, PayP… |
| 2026-10-18 15:54:14 | [proudly-snoring/seat-comlink](https://www.nuget.org/packages/proudly-snoring%2Fseat-comlink) | 1.0.0 | Proudly-Snoring | SeAT plugin managing Discord roles (from squads) and nicknames on multiple serv… |
| 2026-10-18 15:58:56 | [1994/laravel-mail-batch](https://www.nuget.org/packages/1994%2Flaravel-mail-batch) | v0.1.0 | Daniel Jones | Send mail and notifications in batches, paced to your provider's rate limits. |
| 2026-10-18 16:00:49 | [86hc/hk-statutory-compliance-datasets](https://www.nuget.org/packages/86hc%2Fhk-statutory-compliance-datasets) | 1.0.2 | HC BUSINESS LIMITED (86HC Com… | Open JSON/CSV datasets and PHP loader for Hong Kong Licensed Bank Clearing/SWIF… |
| 2026-10-18 16:00:57 | [tomgould/turbopush](https://www.nuget.org/packages/tomgould%2Fturbopush) | v2.0.0 | Tom Gould | PHP endpoint for TurboPush chunked uploads: validates, stores and safely reasse… |
| 2026-10-18 16:11:46 | [nightguardian/laravel](https://www.nuget.org/packages/nightguardian%2Flaravel) | v1.0.0 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
