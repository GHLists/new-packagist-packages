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

## Latest list — 2026-11-18 09:19 UTC

New packages created between 2026-11-18 08:22 UTC and 2026-11-18 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T09-19-40-394835Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 08:58:34 | [qaify/sentinel](https://www.nuget.org/packages/qaify%2Fsentinel) | v0.1.0 |  | Sensor aktivitas keamanan Laravel untuk SOC Qaify: login gagal, payload seranga… |
| 2026-11-18 09:12:09 | [thb/rabbitmq](https://www.nuget.org/packages/thb%2Frabbitmq) | v3.0 |  | Webman plugin: RabbitMQ send/consume (workerman/rabbitmq) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
