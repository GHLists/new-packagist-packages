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

## Latest list — 2026-10-16 20:21 UTC

New packages created between 2026-10-16 19:20 UTC and 2026-10-16 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T20-21-10-442218Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 19:36:18 | [alien1225/basisu](https://www.nuget.org/packages/alien1225%2Fbasisu) | v0.1.1 |  |  |
| 2026-10-16 19:41:37 | [uhifadhi/el-nino-module](https://www.nuget.org/packages/uhifadhi%2Fel-nino-module) | v0.1.1 | Ezekiel Mjema | El Niño watch: the state of the equatorial Pacific, the chance it lasts into th… |
| 2026-10-16 19:45:14 | [sala/framework](https://www.nuget.org/packages/sala%2Fframework) | v1.2.0 | Abraão Xavier Sungo Sala | Um mini-framework em PHP prático, leve e moderno, construído utilizando os pode… |
| 2026-10-16 19:56:36 | [jklejczyk/security-toolkit-for-laravel](https://www.nuget.org/packages/jklejczyk%2Fsecurity-toolkit-for-laravel) | v0.1.0 | Jakub Klejczyk | Security audit for Laravel 12 and 13 in one Artisan command: configuration, fil… |
| 2026-10-16 20:05:00 | [tontonpro/contracts](https://www.nuget.org/packages/tontonpro%2Fcontracts) | v0.1.0 | Denis Albert NGANKAM | Contrats partagés des modules TontonPro : faits d'argent, registre de menus, co… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
