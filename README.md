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

## Latest list — 2026-11-24 18:20 UTC

New packages created between 2026-11-24 17:20 UTC and 2026-11-24 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T18-20-14-774844Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 17:28:22 | [huseyinfiliz/theme-transitions](https://www.nuget.org/packages/huseyinfiliz%2Ftheme-transitions) | 1.0 | Hüseyin Filiz | Smooth, customizable View Transition animations for Flarum 2 theme switching. |
| 2026-11-24 17:29:27 | [barrierepruefungde/typo3](https://www.nuget.org/packages/barrierepruefungde%2Ftypo3) | v0.1.0 |  | Barrierefreiheitserklärung von barrierepruefung.de in TYPO3 einbinden: Prüfung,… |
| 2026-11-24 17:44:18 | [mrcaspan/flarum2-mail-catcher](https://www.nuget.org/packages/mrcaspan%2Fflarum2-mail-catcher) | v1.0.0 | MrCaspan | Catch every outgoing email in the database instead of sending it, and read or d… |
| 2026-11-24 18:00:36 | [buriti8/log-viewer](https://www.nuget.org/packages/buriti8%2Flog-viewer) | 12.0.0 | buriti8; ARCANEDEV | Log Viewer for Laravel with compiled assets included. Fork of arcanedev/log-vie… |
| 2026-11-24 18:14:28 | [adachsoft/data-backup-contracts](https://www.nuget.org/packages/adachsoft%2Fdata-backup-contracts) | v0.2.0 | Arkadiusz Adach | Interfaces and value objects for interoperable PHP data backup and restore inte… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
