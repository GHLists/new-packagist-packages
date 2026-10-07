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

## Latest list — 2026-10-07 11:20 UTC

New packages created between 2026-10-07 10:21 UTC and 2026-10-07 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T11-20-26-886056Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 10:21:39 | [ferrox/ferrox-php-auth](https://www.nuget.org/packages/ferrox%2Fferrox-php-auth) | v1.1.0 |  | Ferrox PHP Auth module |
| 2026-10-07 10:21:39 | [ferrox/ferrox-php-broadcasting](https://www.nuget.org/packages/ferrox%2Fferrox-php-broadcasting) | v1.1.0 |  | Ferrox PHP Broadcasting module |
| 2026-10-07 10:21:39 | [ferrox/ferrox-php-cli](https://www.nuget.org/packages/ferrox%2Fferrox-php-cli) | v1.1.0 |  | Ferrox PHP Cli module |
| 2026-10-07 10:47:53 | [peter9x/laravel-mail-listeners](https://www.nuget.org/packages/peter9x%2Flaravel-mail-listeners) | v0.0.2 | Peter | Read mailboxes (Microsoft Graph, IMAP) and turn every new email into Laravel ev… |
| 2026-10-07 11:04:51 | [arout/rhapsody-forms](https://www.nuget.org/packages/arout%2Frhapsody-forms) | v1.0.2 |  | Forms for Rhapsody: code-defined forms, spam protection, a submissions inbox an… |
| 2026-10-07 11:06:15 | [kipchak/identity](https://www.nuget.org/packages/kipchak%2Fidentity) | 1.0 |  | Consumer and tenant identity for the Kipchak API Development Kit (ADK): who a r… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
