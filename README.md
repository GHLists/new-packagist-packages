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

## Latest list — 2026-10-14 05:21 UTC

New packages created between 2026-10-14 04:21 UTC and 2026-10-14 05:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T05-21-48-837449Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 04:32:01 | [directorytree/screenshot](https://www.nuget.org/packages/directorytree%2Fscreenshot) | v1.1.0 | Steve Bauman | Create browser screenshots with PHP and Laravel. |
| 2026-10-14 04:48:03 | [freepeace13/laraversine](https://www.nuget.org/packages/freepeace13%2Flaraversine) | v1.0.0 | Kin Basco | Find the nearest locations in Laravel with Eloquent using the haversine formula… |
| 2026-10-14 05:02:17 | [itools/svgsecuritycheck](https://www.nuget.org/packages/itools%2Fsvgsecuritycheck) | v1.0.0 | interactivetools.com | Allowlist check for uploaded SVG files: rejects any that could run script, load… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
