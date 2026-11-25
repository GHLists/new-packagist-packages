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

## Latest list — 2026-11-25 14:21 UTC

New packages created between 2026-11-25 13:20 UTC and 2026-11-25 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T14-21-04-175002Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 13:33:33 | [solutionforest/filament-unsaved-changes-bar](https://www.nuget.org/packages/solutionforest%2Ffilament-unsaved-changes-bar) | v0.2.0 | Solution Forest | A floating Shopify / Laravel Cloud-style "Unsaved changes · Discard · Save" bar… |
| 2026-11-25 14:03:00 | [qiick/laravel-access](https://www.nuget.org/packages/qiick%2Flaravel-access) | v0.1.0-beta.1 | Qiick | Shared authorization core for qiick Laravel products: Gate::before, effective p… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
