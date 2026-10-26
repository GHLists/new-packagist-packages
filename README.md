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

## Latest list — 2026-10-26 02:19 UTC

New packages created between 2026-10-26 01:21 UTC and 2026-10-26 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T02-19-27-76071Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 01:41:13 | [billsensei/moodle-report_studentsummary](https://www.nuget.org/packages/billsensei%2Fmoodle-report_studentsummary) | v0.4.5 | billsensei | A Moodle report that summarises one student's engagement across the site on a s… |
| 2026-10-26 02:07:10 | [vitisstudio/nativephp-firestore](https://www.nuget.org/packages/vitisstudio%2Fnativephp-firestore) | v0.1.0 | Vitis Studio | Cloud Firestore and Firebase Authentication for NativePHP Mobile, backed by the… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
