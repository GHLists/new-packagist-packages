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

## Latest list — 2026-10-12 02:20 UTC

New packages created between 2026-10-12 01:19 UTC and 2026-10-12 02:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T02-20-21-86104Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 01:30:46 | [syahrulzzadie/satu-sehat](https://www.nuget.org/packages/syahrulzzadie%2Fsatu-sehat) | 1.3.1 | Syahrul Adiguna Kurniawan | Syahrul JS RSUI Harapan Anda - Satu Sehat |
| 2026-10-12 01:42:17 | [lensen/base-erp-sdk](https://www.nuget.org/packages/lensen%2Fbase-erp-sdk) | v1.0.0 | haiyong | A base-erp-sdk(Baselinker) component for lensen. |
| 2026-10-12 02:07:56 | [josephcrowell/wn-gdpr-plugin](https://www.nuget.org/packages/josephcrowell%2Fwn-gdpr-plugin) | 2.3.1 | Tobias Kündig; Hounddd - Dami… | Winter CMS plugin to make websites GDPR and ePrivacy compliant |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
