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

## Latest list — 2026-10-30 13:19 UTC

New packages created between 2026-10-30 12:20 UTC and 2026-10-30 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T13-19-34-10669Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 12:39:03 | [ismailnakkar/laravel-mail-frame](https://www.nuget.org/packages/ismailnakkar%2Flaravel-mail-frame) | v0.1.0 | Ismail Nakkar | One hand-tuned HTML frame for Laravel notification mail, with an ordered block… |
| 2026-10-30 12:58:55 | [rllngr/kirby-memo](https://www.nuget.org/packages/rllngr%2Fkirby-memo) | 1.0.0 | Nicolas Rollinger | Kirby 5 plugin — a read-only cheat sheet in the Panel, rendered from a Markdown… |
| 2026-10-30 13:03:21 | [yuriitatur/permissions](https://www.nuget.org/packages/yuriitatur%2Fpermissions) | v0.1.0 | Yurii Tatur | simple permission manager |
| 2026-10-30 13:07:41 | [cboxdk/laravel-webhooks](https://www.nuget.org/packages/cboxdk%2Flaravel-webhooks) | v0.1.0 | Sylvester Damgaard | Cbox Webhooks: the outbound and inbound webhook engine for Laravel. A persisten… |
| 2026-10-30 13:09:05 | [ycloudyusa/embedded_groupexpro_schedule](https://www.nuget.org/packages/ycloudyusa%2Fembedded_groupexpro_schedule) | 1.0.0 |  | Provides an Embedded GroupEx Pro Schedule element and block. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
