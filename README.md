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

## Latest list — 2026-10-20 06:20 UTC

New packages created between 2026-10-20 05:19 UTC and 2026-10-20 06:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T06-20-49-332534Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 05:27:03 | [magepow/smtptest](https://www.nuget.org/packages/magepow%2Fsmtptest) | 1.0.0 |  | Magepow SMTP Test Connection for Mail Sending Settings |
| 2026-10-20 05:27:40 | [aporat/laravel-push-notifications](https://www.nuget.org/packages/aporat%2Flaravel-push-notifications) | v0.1.0 | Adar Porat | Laravel integration for aporat/push-notifications: APNs and FCM pushes per app,… |
| 2026-10-20 05:30:59 | [ispgrid/documents](https://www.nuget.org/packages/ispgrid%2Fdocuments) | v0.1.0 | Karan | Customer documents for ISPGrid: ID proofs and agreements, photographed or uploa… |
| 2026-10-20 05:31:38 | [roundly-consulting/tags-for-laravel](https://www.nuget.org/packages/roundly-consulting%2Ftags-for-laravel) | 1.0.0 | Andrej Mihaliak | Typed taxonomies for any Eloquent model: flat or nested, single- or multi-selec… |
| 2026-10-20 05:53:44 | [greenhat-services/magpie-laravel](https://www.nuget.org/packages/greenhat-services%2Fmagpie-laravel) | v0.1.1 |  | Magpie error tracking and performance monitoring for Laravel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
