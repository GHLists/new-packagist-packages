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

## Latest list — 2026-11-25 04:19 UTC

New packages created between 2026-11-25 03:20 UTC and 2026-11-25 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T04-19-56-803509Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 03:26:13 | [particle-academy/fancy-schema](https://www.nuget.org/packages/particle-academy%2Ffancy-schema) | v0.1.0 | Particle Academy | Zero-dependency, fail-closed JSON Schema 2020-12 validator for PHP, matching @p… |
| 2026-11-25 03:28:02 | [dmorenof/sendgrid-sdk](https://www.nuget.org/packages/dmorenof%2Fsendgrid-sdk) | v0.1.0 | David Moreno Falero | Unofficial PHP SDK for the whole Twilio SendGrid v3 API (mail send, marketing c… |
| 2026-11-25 03:59:02 | [jiannius/audit](https://www.nuget.org/packages/jiannius%2Faudit) | v1.0.0-alpha.2 | TJ | A small, generic audit trail for Laravel 13: append-only, strict-mode safe, fai… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
