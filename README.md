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

## Latest list — 2026-11-06 12:22 UTC

New packages created between 2026-11-06 11:20 UTC and 2026-11-06 12:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T12-22-13-928404Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 11:41:44 | [vos/label-classifier](https://www.nuget.org/packages/vos%2Flabel-classifier) | v1 |  | Suggests labels for pull requests by answering per-label policy questions again… |
| 2026-11-06 12:00:11 | [intragile/laravel-reverb-kit](https://www.nuget.org/packages/intragile%2Flaravel-reverb-kit) | v1.0.0 | IntrAgile Kft. | Production toolkit for Laravel Reverb: a static `reverb:doctor` deploy gate (al… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
