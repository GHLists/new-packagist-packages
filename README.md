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

## Latest list — 2026-11-25 16:19 UTC

New packages created between 2026-11-25 15:19 UTC and 2026-11-25 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T16-19-31-630153Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 15:23:45 | [shoplygg/shoply-php](https://www.nuget.org/packages/shoplygg%2Fshoply-php) | v0.12.1 |  | Shoply's API from your own server: every route as a method, safe retries, pages… |
| 2026-11-25 15:32:38 | [rushphp/schema-tool](https://www.nuget.org/packages/rushphp%2Fschema-tool) | v0.1.0 | RUSHphp | RUSH schema tool. Structural database schema versioning for SQLite and MySQL/Ma… |
| 2026-11-25 15:55:29 | [webfactory/newsletter-registration-bundle](https://www.nuget.org/packages/webfactory%2Fnewsletter-registration-bundle) | 1.0.0 |  | Symfony-Bundle for Newsletter-Registration |
| 2026-11-25 15:56:08 | [nr/processmigrations](https://www.nuget.org/packages/nr%2Fprocessmigrations) | 1.0.2 | Neue Rituale | Run schema and data migrations step by step, from the admin, a cron job or the… |
| 2026-11-25 16:13:39 | [postilon/postilon-php](https://www.nuget.org/packages/postilon%2Fpostilon-php) | v1.0.0 | Kulina Pte. Ltd. | PHP SDK for the Postilon transactional email API |
| 2026-11-25 16:13:57 | [concept-image/wp-hook-attributes](https://www.nuget.org/packages/concept-image%2Fwp-hook-attributes) | 0.0.1 | Aurélien | Declare WordPress actions and filters with PHP attributes (#[Action], #[Filter]… |
| 2026-11-25 16:15:35 | [concept-image/wp-fortress](https://www.nuget.org/packages/concept-image%2Fwp-fortress) | 0.0.1 | Aurélien | WP Fortress: switchable security modules for WordPress on Bedrock + Acorn (secu… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
