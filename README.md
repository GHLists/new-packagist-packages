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

## Latest list — 2026-10-06 11:21 UTC

New packages created between 2026-10-06 10:22 UTC and 2026-10-06 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T11-21-45-100119Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 10:43:20 | [scbudgetweb/laravel-cookie-consent](https://www.nuget.org/packages/scbudgetweb%2Flaravel-cookie-consent) | v1.0.0 |  | A simple, compliant cookie consent banner for Laravel: Accept, Reject and Custo… |
| 2026-10-06 10:53:19 | [sachin-cloee/pterodactyl-sso](https://www.nuget.org/packages/sachin-cloee%2Fpterodactyl-sso) | v1.0.0 |  | Pterodactyl 2.x panel extension that signs customers in from a Paymenter billin… |
| 2026-10-06 10:56:59 | [crushjs/aba-payway](https://www.nuget.org/packages/crushjs%2Faba-payway) | v1.0.0 | Crushjs | Pay as You Wish in Cambodia - ABA PayWay payment gateway client for PHP and Lar… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
