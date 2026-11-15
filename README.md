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

## Latest list — 2026-11-15 22:21 UTC

New packages created between 2026-11-15 21:22 UTC and 2026-11-15 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T22-21-50-908565Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 21:25:03 | [danilovl/contact-bundle](https://www.nuget.org/packages/danilovl%2Fcontact-bundle) | v0.0.1 | Vladimir Danilov | Personal address book bundle for Symfony: contacts with multiple emails, phones… |
| 2026-11-15 21:43:52 | [starbug/api](https://www.nuget.org/packages/starbug%2Fapi) | v0.9.0 | Ali Gangji | API response and controller infrastructure for Starbug. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
