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

## Latest list — 2026-10-22 15:21 UTC

New packages created between 2026-10-22 14:20 UTC and 2026-10-22 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T15-21-49-317491Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 14:39:17 | [tenma/discord](https://www.nuget.org/packages/tenma%2Fdiscord) | v0.1.0 |  | Discord bots in PHP on Tenma: gateway events, slash commands, buttons and voice… |
| 2026-10-22 14:43:24 | [jacerider/ux](https://www.nuget.org/packages/jacerider%2Fux) | 6.0.0 | Cyle Carlson (JaceRider) | A suite of UI elements and components to improve user experience. |
| 2026-10-22 14:44:03 | [jacerider/escort](https://www.nuget.org/packages/jacerider%2Fescort) | 5.0.0 | Cyle Carlson (JaceRider) | An admin menu of extreme super awesomeness. |
| 2026-10-22 14:47:31 | [considbrs-webdev/modularity-link-cards](https://www.nuget.org/packages/considbrs-webdev%2Fmodularity-link-cards) | 1.0.0 | Consid Borås AB | A grid of clickable link cards with icons. |
| 2026-10-22 14:47:53 | [considbrs-webdev/modularity-quick-links](https://www.nuget.org/packages/considbrs-webdev%2Fmodularity-quick-links) | 1.0.1 | Consid Borås AB | A module for Modularity that creates the ability for the user to create a grid… |
| 2026-10-22 14:58:00 | [filagora/filagora-notifications](https://www.nuget.org/packages/filagora%2Ffilagora-notifications) | v0.1.0 |  | Notification preferences for Filagora: per-person, per-category, per-channel ch… |
| 2026-10-22 15:16:25 | [mehrabhossain/loglens](https://www.nuget.org/packages/mehrabhossain%2Floglens) | v1.0.0 | Mehrab Hossain | Developer-focused application log analyzer and monitoring dashboard for Laravel… |
| 2026-10-22 15:19:48 | [risetechapps/notify-service-for-laravel](https://www.nuget.org/packages/risetechapps%2Fnotify-service-for-laravel) | 1.0.0 | Rise Tech |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
