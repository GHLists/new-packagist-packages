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

## Latest list — 2026-11-04 06:21 UTC

New packages created between 2026-11-04 05:19 UTC and 2026-11-04 06:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T06-21-26-081087Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 05:22:32 | [pharaonic/laravel-dynamic-config](https://www.nuget.org/packages/pharaonic%2Flaravel-dynamic-config) | 13.0.0 | Moamen Eltouny (Raggi) | Store Laravel configuration values in the database, globally, per identifier or… |
| 2026-11-04 05:54:07 | [contenir/contenir-audience-mezzio](https://www.nuget.org/packages/contenir%2Fcontenir-audience-mezzio) | v0.1.0 |  | The site half of contenir/contenir-audience for Mezzio: a Subscriptions service… |
| 2026-11-04 05:54:19 | [contenir-extension/campaign-monitor](https://www.nuget.org/packages/contenir-extension%2Fcampaign-monitor) | v0.1.0 |  | The Campaign Monitor add-on for Contenir CMS: keeps a Campaign Monitor list in… |
| 2026-11-04 05:54:31 | [contenir-extension/mailchimp](https://www.nuget.org/packages/contenir-extension%2Fmailchimp) | v0.1.0 |  | The Mailchimp add-on for Contenir CMS: keeps a Mailchimp audience in step with… |
| 2026-11-04 05:55:35 | [sameoldnick/laravel-notification-preferences](https://www.nuget.org/packages/sameoldnick%2Flaravel-notification-preferences) | v1.0.0 | Nick Hamnett | A Laravel package for managing user notification preferences by notification ty… |
| 2026-11-04 06:13:07 | [hipdevteam/ion-mu](https://www.nuget.org/packages/hipdevteam%2Fion-mu) | v3.5.5 | ION | ION MU — WordPress mu-plugin that fire-and-forgets activity events to Site Inte… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
