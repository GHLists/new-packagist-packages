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

## Latest list — 2026-11-03 04:21 UTC

New packages created between 2026-11-03 03:20 UTC and 2026-11-03 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T04-21-36-121163Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 03:28:38 | [stougeiro/app](https://www.nuget.org/packages/stougeiro%2Fapp) | v0.2.0 | stougeiro | A PHP 8.2 application foundation for shared hosting, built on the Stougeiro run… |
| 2026-11-03 03:29:03 | [mage2kishan/module-ai-visibility](https://www.nuget.org/packages/mage2kishan%2Fmodule-ai-visibility) | 1.2.0 | Kishan Savaliya | Panth AI Visibility - analytics for Magento 2 that counts AI crawler requests (… |
| 2026-11-03 03:43:00 | [borodulin/yii2-camunda](https://www.nuget.org/packages/borodulin%2Fyii2-camunda) | 1.0.1 | Andrey Borodulin | The Camunda Rest API extension for the Yii2 framework |
| 2026-11-03 03:43:13 | [conquer/flot](https://www.nuget.org/packages/conquer%2Fflot) | 1.0.0 | Andrey Borodulin | Yii2 flot widget |
| 2026-11-03 03:43:20 | [conquer/fullcalendar](https://www.nuget.org/packages/conquer%2Ffullcalendar) | 1.0.0 | Andrey Borodulin | Yii2 fullcalendar widget |
| 2026-11-03 03:44:05 | [conquer/simplelineicons](https://www.nuget.org/packages/conquer%2Fsimplelineicons) | 1.0.0 | Andrey Borodulin | Yii2 simplelineicons widget |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
