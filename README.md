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

## Latest list — 2026-10-27 20:21 UTC

New packages created between 2026-10-27 19:19 UTC and 2026-10-27 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T20-21-52-643859Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 19:44:39 | [tencentcloud/cvd](https://www.nuget.org/packages/tencentcloud%2Fcvd) | 3.0.1690 | tencentcloudapi | TencentCloudApi php sdk cvd |
| 2026-10-27 19:49:16 | [happiness/tracker_monitoring](https://www.nuget.org/packages/happiness%2Ftracker_monitoring) | v0.1.0 |  | Sends the site's packages, status report and error log to Tracker. |
| 2026-10-27 20:14:31 | [neowiki/neowiki](https://www.nuget.org/packages/neowiki%2Fneowiki) | 0.1.0-rc.1 | Professional.Wiki; Jeroen De… | Collaborative knowledge graph: model it with schemas, edit it in generated form… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
