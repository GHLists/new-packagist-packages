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

## Latest list — 2026-10-23 18:21 UTC

New packages created between 2026-10-23 17:21 UTC and 2026-10-23 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T18-21-19-231557Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 17:22:52 | [vijaycs85/drupal-contrib-skills](https://www.nuget.org/packages/vijaycs85%2Fdrupal-contrib-skills) | 1.0.1 | Vijay | Curated collection of AI agent skills for Drupal Core and Contrib development,… |
| 2026-10-23 17:23:06 | [uams-web/statamic-form-settings](https://www.nuget.org/packages/uams-web%2Fstatamic-form-settings) | v0.1.0 | UAMS Web Services; Josh Daugh… | Control Panel form settings for Statamic: notification routing and conditions,… |
| 2026-10-23 17:28:56 | [alibabacloud/csasedr-20241122](https://www.nuget.org/packages/alibabacloud%2Fcsasedr-20241122) | 1.0.0 | Alibaba Cloud SDK | Alibaba Cloud CsasEdr (20241122) SDK Library for PHP |
| 2026-10-23 18:06:30 | [voltkit/rtc-server](https://www.nuget.org/packages/voltkit%2Frtc-server) | v0.1.0 |  | VoltKit RTC server SDK for PHP: rooms, tokens, chat, broadcast streams, usage,… |
| 2026-10-23 18:07:00 | [ucf/ucf-plugin-directory](https://www.nuget.org/packages/ucf%2Fucf-plugin-directory) | v0.1.0 |  | Browse, install, and update UCF WordPress plugins from the UCF Composer reposit… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
