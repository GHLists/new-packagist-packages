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

## Latest list — 2026-11-28 13:19 UTC

New packages created between 2026-11-28 12:20 UTC and 2026-11-28 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T13-19-58-21063Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 12:24:12 | [mignuti/contao-trackd-analytics](https://www.nuget.org/packages/mignuti%2Fcontao-trackd-analytics) | 1.0.1 | Mignuti Media | trackd.one for Contao - cookieless, privacy-friendly analytics. Adds the trackd… |
| 2026-11-28 12:56:30 | [jaizendra-netizen/cold-email-subject-lint](https://www.nuget.org/packages/jaizendra-netizen%2Fcold-email-subject-lint) | v1.0.0 | OneGTMLab | PHP CLI and library that lints a cold email subject line: length, ALL CAPS, rep… |
| 2026-11-28 12:56:42 | [jaizendra-netizen/average-contract-value-calc](https://www.nuget.org/packages/jaizendra-netizen%2Faverage-contract-value-calc) | v1.0.0 | OneGTMLab | PHP CLI and library: average contract value (mean and median) from a contracts… |
| 2026-11-28 13:05:59 | [klsoft/auth-session](https://www.nuget.org/packages/klsoft%2Fauth-session) | 1.0.0 |  | Session based authentication |
| 2026-11-28 13:15:53 | [aldinokemal/gowa-sdk-php](https://www.nuget.org/packages/aldinokemal%2Fgowa-sdk-php) | v9.11.0 | OpenAPI | This API is used for sending whatsapp via API. The web dashboard is a separate… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
