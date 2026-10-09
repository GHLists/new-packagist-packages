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

## Latest list — 2026-10-09 20:20 UTC

New packages created between 2026-10-09 19:21 UTC and 2026-10-09 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T20-20-43-730607Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 19:35:26 | [polaris/anonymous](https://www.nuget.org/packages/polaris%2Fanonymous) | v0.7.0 | 2am.tech | Anonymous sign-in for Polaris for PHP: guest sessions, an explicit conversion i… |
| 2026-10-09 19:35:26 | [polaris/multi-session](https://www.nuget.org/packages/polaris%2Fmulti-session) | v0.7.0 | 2am.tech | Multi-session for Polaris for PHP: several signed-in accounts on one device, sw… |
| 2026-10-09 19:35:26 | [polaris/passwordless](https://www.nuget.org/packages/polaris%2Fpasswordless) | v0.7.0 | 2am.tech | Passwordless sign-in for Polaris for PHP: magic links, email one-time codes (si… |
| 2026-10-09 19:35:26 | [polaris/username](https://www.nuget.org/packages/polaris%2Fusername) | v0.7.0 | 2am.tech | Username for Polaris for PHP: sign in with a username or an email through core'… |
| 2026-10-09 19:38:03 | [ernestdefoe/millwright-bridge](https://www.nuget.org/packages/ernestdefoe%2Fmillwright-bridge) | v0.1.0 | Ernest Defoe | Upgrade a Flarum 1.8 forum to Flarum 2.0 from the admin page: checks every exte… |
| 2026-10-09 19:42:14 | [avelto/avelto-php](https://www.nuget.org/packages/avelto%2Favelto-php) | v0.2.0 |  | The official PHP SDK for Avelto, the email API for developers who want it to ju… |
| 2026-10-09 20:11:26 | [acrnogor/audit-api-bundle](https://www.nuget.org/packages/acrnogor%2Faudit-api-bundle) | v0.7.3 | Ante Crnogorac | Symfony bundle providing an API interface for damienharper/auditor-bundle audit… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
