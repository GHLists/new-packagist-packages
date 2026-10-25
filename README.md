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

## Latest list — 2026-10-25 05:20 UTC

New packages created between 2026-10-25 04:18 UTC and 2026-10-25 05:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T05-20-51-187499Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 04:32:49 | [contenir/contenir-navigation](https://www.nuget.org/packages/contenir%2Fcontenir-navigation) | v0.1.0 |  | Managed site navigation for Contenir CMS: menus of nested items linking to reco… |
| 2026-10-25 04:35:40 | [contenir-extension/navigation](https://www.nuget.org/packages/contenir-extension%2Fnavigation) | v0.1.0 |  | Managed site navigation for Contenir CMS: the Navigation section of Site Pages,… |
| 2026-10-25 04:44:51 | [atannex/localization](https://www.nuget.org/packages/atannex%2Flocalization) | v1.0.0 | Atanga Leke Collins | Complete localization for Laravel: locale registry with a built-in catalog, req… |
| 2026-10-25 05:08:36 | [makallio85/rocksoftware-cakephp-messaging-client](https://www.nuget.org/packages/makallio85%2Frocksoftware-cakephp-messaging-client) | v1.0.0 | Marko Kallio | CakePHP 5 plugin through which a Rock Software application sends email and SMS… |
| 2026-10-25 05:15:27 | [imagewize/elayne-legal](https://www.nuget.org/packages/imagewize%2Felayne-legal) | v1.0.0 | Jasper Frumau | Child theme of Elayne for law firms: Legal Corporate and Legal Blue style varia… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
