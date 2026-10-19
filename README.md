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

## Latest list — 2026-10-19 04:19 UTC

New packages created between 2026-10-19 03:19 UTC and 2026-10-19 04:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T04-19-40-859497Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 03:50:18 | [catzconnect/catzconnect-php](https://www.nuget.org/packages/catzconnect%2Fcatzconnect-php) | v1.5.0 | Catalizo | Official PHP SDK for Catz Connect: send email, WhatsApp, push, SMS and voice me… |
| 2026-10-19 04:08:18 | [krazybean/untangled](https://www.nuget.org/packages/krazybean%2Funtangled) | v1.0.0 | Juan Castro | Dependency health your whole team can understand: cycles and coupling in PHP pr… |
| 2026-10-19 04:08:39 | [t11n-dev/flarum-migration-tool](https://www.nuget.org/packages/t11n-dev%2Fflarum-migration-tool) | v2.5.1 | T11N | Complete migration tool with admin UI for easy Flarum server transfer. Backup,… |
| 2026-10-19 04:15:25 | [itmosoft/laravel-audit-log](https://www.nuget.org/packages/itmosoft%2Flaravel-audit-log) | v1.0.0 |  | Auditing for Eloquent models, business events, and Laravel queue lifecycle even… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
