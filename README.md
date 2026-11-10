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

## Latest list — 2026-11-10 11:23 UTC

New packages created between 2026-11-10 10:21 UTC and 2026-11-10 11:23 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T11-23-00-792062Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 10:22:03 | [grinet/billing-address-at-shipping](https://www.nuget.org/packages/grinet%2Fbilling-address-at-shipping) | 1.0.0 | Hidayet OK @ grinet | Billing address below shipping with optional restricted HTML descriptions |
| 2026-11-10 10:23:47 | [tecclub/otpkit](https://www.nuget.org/packages/tecclub%2Fotpkit) | v1.0.0 | Sameed | Headless one-time codes for Laravel: issue, deliver, verify and expire codes fo… |
| 2026-11-10 11:03:52 | [medienbaecker/kirby-stars-field](https://www.nuget.org/packages/medienbaecker%2Fkirby-stars-field) | 1.0.0 | Thomas Günther | A star rating field for the Kirby Panel |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
