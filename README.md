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

## Latest list — 2026-11-15 14:19 UTC

New packages created between 2026-11-15 13:21 UTC and 2026-11-15 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-15T14-19-43-903808Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-15 13:22:44 | [youvision/think-store-codeditor](https://www.nuget.org/packages/youvision%2Fthink-store-codeditor) | v1.3 | indiboy-create; AI | ThinkPHP 8 模板代码编辑器扩展：基于 Ace 与 layui 编辑 HTML + PHP 混合模板，提供页面、读取、更新、新增与静态资源路由。 |
| 2026-11-15 13:23:25 | [camelia/orm](https://www.nuget.org/packages/camelia%2Form) | 1.0.0 | Dario Garcia | Lightweight attribute-mapped Active Record ORM for MariaDB/MySQL over PDO. |
| 2026-11-15 13:23:43 | [camelia/controllers](https://www.nuget.org/packages/camelia%2Fcontrollers) | 1.0.0 | Dario Garcia | Framework-agnostic REST controller toolkit: routing, request parsing, validatio… |
| 2026-11-15 13:28:17 | [adamjenkins/moodle-assignsubmission_vrtour](https://www.nuget.org/packages/adamjenkins%2Fmoodle-assignsubmission_vrtour) | v0.1.3 |  | An assignment submission type for 360° photo tours: students upload panoramas,… |
| 2026-11-15 13:28:17 | [adamjenkins/moodle-local_vravatar](https://www.nuget.org/packages/adamjenkins%2Fmoodle-local_vravatar) | v0.1.3 |  | Lets each user design the avatar that stands for them in VR room live rooms, fr… |
| 2026-11-15 13:28:17 | [adamjenkins/moodle-mod_vrmakerspace](https://www.nuget.org/packages/adamjenkins%2Fmoodle-mod_vrmakerspace) | v0.1.1 |  | A Moodle activity in which students sculpt and model 3D pieces, alone or with t… |
| 2026-11-15 13:28:17 | [adamjenkins/moodle-mod_vrroom](https://www.nuget.org/packages/adamjenkins%2Fmoodle-mod_vrroom) | v0.1.3 |  | 3D rooms students explore in the browser: stations with models, images, texts a… |
| 2026-11-15 13:28:17 | [adamjenkins/moodle-vrroomenv_rooms](https://www.nuget.org/packages/adamjenkins%2Fmoodle-vrroomenv_rooms) | v0.1.2 |  | Twenty ready-made 3D rooms for the VR room activity, from freely licensed sourc… |
| 2026-11-15 13:28:17 | [adamjenkins/moodle-vrroomruntime_companion](https://www.nuget.org/packages/adamjenkins%2Fmoodle-vrroomruntime_companion) | v0.1.2 |  | A VR room run mode that sends live rooms through a self-hosted companion servic… |
| 2026-11-15 13:30:50 | [flytachi/winter-service-mariadb](https://www.nuget.org/packages/flytachi%2Fwinter-service-mariadb) | v1.0.0 | Flytachi | MariaDB inside a Winter application's container: a service the application star… |
| 2026-11-15 13:30:55 | [flytachi/winter-service-redis](https://www.nuget.org/packages/flytachi%2Fwinter-service-redis) | v1.0.0 | Flytachi | Redis inside a Winter application's container: a service the application starts… |
| 2026-11-15 13:47:34 | [mainframe98/arc_booster](https://www.nuget.org/packages/mainframe98%2Farc_booster) | v1.0.0 | mainframe98 | Arc Booster is a PHP extension aiming to speed up performance of Arcanist, and… |
| 2026-11-15 13:58:42 | [laravelazier/laravelazier](https://www.nuget.org/packages/laravelazier%2Flaravelazier) | v1.2.2 | Laravelazier Contributors | Lightweight Laravel package for generating PDF and Excel files with minimal set… |
| 2026-11-15 14:12:31 | [nowo-tech/notify-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fnotify-kit-bundle) | v0.1.0 | Héctor Franco Aceituno; Nowo.… | Notifications for Symfony: one notify() call, an in-app inbox with a real-time… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
