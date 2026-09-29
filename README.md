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

## Latest list — 2026-09-29 23:19 UTC

New packages created between 2026-09-29 22:21 UTC and 2026-09-29 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T23-19-28-596451Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 22:21:24 | [simonecerruti/laravel-translation-audit](https://www.nuget.org/packages/simonecerruti%2Flaravel-translation-audit) | v0.1.0 | SimoneCerruti | Audit your app for missing or unused translations. |
| 2026-09-29 22:23:54 | [mage2kishan/module-faq](https://www.nuget.org/packages/mage2kishan%2Fmodule-faq) | 1.2.4 | Kishan Savaliya | Advanced FAQ Module with multi-level assignment capabilities |
| 2026-09-29 22:53:11 | [mage2kishan/module-filter-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-filter-seo) | 1.1.2 | Kishan Savaliya | Panth Filter SEO — clean path-based URLs for layered navigation filters + dynam… |
| 2026-09-29 23:15:45 | [mralston/diagnostics](https://www.nuget.org/packages/mralston%2Fdiagnostics) | v1.0.0 | Matt Ralston | Run a suite of named checks against any Eloquent model, in parallel on the queu… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
