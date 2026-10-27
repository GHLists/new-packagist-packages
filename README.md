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

## Latest list — 2026-10-27 19:19 UTC

New packages created between 2026-10-27 18:20 UTC and 2026-10-27 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T19-19-48-957345Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 18:23:16 | [gsu-cetloe/cetloelib-oracle-php](https://www.nuget.org/packages/gsu-cetloe%2Fcetloelib-oracle-php) | v1 | Melody Kimball |  |
| 2026-10-27 18:31:09 | [logicoy/oe-module-logicoy-erx](https://www.nuget.org/packages/logicoy%2Foe-module-logicoy-erx) | v1.0.9 | LogiCoy | Connects an OpenEMR installation to the LogiCoy eRx network. |
| 2026-10-27 18:41:58 | [rewi.sh/menu](https://www.nuget.org/packages/rewi.sh%2Fmenu) | 1.0.0 | rewi.sh | Menus, navigation, and navbar builder for Craft CMS — nested nav, element links… |
| 2026-10-27 18:57:49 | [mailinfra/mailinfra](https://www.nuget.org/packages/mailinfra%2Fmailinfra) | v0.1.0 |  | Официальный SDK MailInfra для PHP — email API для разработчиков |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
