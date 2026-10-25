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

## Latest list — 2026-10-25 19:22 UTC

New packages created between 2026-10-25 18:19 UTC and 2026-10-25 19:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T19-22-32-961587Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 18:43:55 | [protendai/nativephp-wifi-direct](https://www.nuget.org/packages/protendai%2Fnativephp-wifi-direct) | v1.0.0 | Tendai Karuma | Wi-Fi Direct for NativePHP Mobile: phone-to-phone networking with no router, wi… |
| 2026-10-25 19:00:06 | [bernskiold/laravel-postmark](https://www.nuget.org/packages/bernskiold%2Flaravel-postmark) | 1.0.0 | Bernskiold; Erik Bernskiöld | Receive Postmark webhooks as typed Laravel events, and recognise Postmark's ina… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
