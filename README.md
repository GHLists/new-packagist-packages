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

## Latest list — 2026-10-28 07:21 UTC

New packages created between 2026-10-28 06:19 UTC and 2026-10-28 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T07-21-18-283245Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 06:31:25 | [bbwdadfg/pdftomd-url-tools](https://www.nuget.org/packages/bbwdadfg%2Fpdftomd-url-tools) | v0.1.0 | wangneo276-lgtm | Free in-browser pdf to md tool. Drop a text PDF, preview Markdown, copy or down… |
| 2026-10-28 06:56:00 | [hipdevteam/ion-mu](https://www.nuget.org/packages/hipdevteam%2Fion-mu) | v3.5.1 | ION | ION MU — WordPress mu-plugin that fire-and-forgets activity events to Site Inte… |
| 2026-10-28 06:58:44 | [privatus/filament-analytics](https://www.nuget.org/packages/privatus%2Ffilament-analytics) | v1.0.0 | Two Phase LLC | Privatus Analytics dashboard widgets for Filament: visitors, pageviews, a traff… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
