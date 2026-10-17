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

## Latest list — 2026-10-17 12:19 UTC

New packages created between 2026-10-17 11:21 UTC and 2026-10-17 12:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T12-19-58-366681Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 11:23:53 | [survos/tour-bundle](https://www.nuget.org/packages/survos%2Ftour-bundle) | 2.42.23 |  | Reusable translated tours for rendered menus and explicit Twig targets |
| 2026-10-17 11:29:34 | [ivopdf/ivopdf](https://www.nuget.org/packages/ivopdf%2Fivopdf) | v1.0.0 | Ivo Apostolov | Modern Pure-PHP HTML & CSS to PDF Engine with Flexbox, CSS Grid, and Full UTF-8… |
| 2026-10-17 11:41:36 | [tobiasnagel01/resend-sdk](https://www.nuget.org/packages/tobiasnagel01%2Fresend-sdk) | 1.1.0 | Tobias Nagel | Saloon-powered PHP & Laravel SDK for the Resend API. |
| 2026-10-17 11:47:56 | [raqmeyat/workspace](https://www.nuget.org/packages/raqmeyat%2Fworkspace) | v0.1.0 | Loai Kanou | Multi-tenant Workspace management for Laravel 12 and 13, built on spatie/larave… |
| 2026-10-17 12:10:14 | [conratwebsolutions/crgalerie](https://www.nuget.org/packages/conratwebsolutions%2Fcrgalerie) | v3.0.0 | ConRat WebSolutions | ConRat Photo Gallery - image galleries maintained centrally in a backend module… |
| 2026-10-17 12:13:03 | [goblinq/client](https://www.nuget.org/packages/goblinq%2Fclient) | 0.0.2 |  | PHP client for the GoblinQ job delivery service |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
