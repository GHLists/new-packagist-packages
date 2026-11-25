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

## Latest list — 2026-11-25 08:19 UTC

New packages created between 2026-11-25 07:20 UTC and 2026-11-25 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T08-19-26-910762Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 07:23:49 | [octoverse-id/octoreview-php](https://www.nuget.org/packages/octoverse-id%2Foctoreview-php) | v0.1.0 |  | Official PHP SDK for Octoreview: multi-tenant reviews, ratings and review media. |
| 2026-11-25 07:55:08 | [averay/salesforce-utils](https://www.nuget.org/packages/averay%2Fsalesforce-utils) | v0.1.0 | Adam Averay | A collection of utilities to make interacting with the Phpforce Salesforce SOAP… |
| 2026-11-25 07:57:39 | [adachsoft/mailbox-contract-tests](https://www.nuget.org/packages/adachsoft%2Fmailbox-contract-tests) | v0.2.0 | Arkadiusz Adach | Reusable PHPUnit contract tests for mailbox implementations |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
