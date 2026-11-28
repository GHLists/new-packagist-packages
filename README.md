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

## Latest list — 2026-11-28 17:20 UTC

New packages created between 2026-11-28 16:20 UTC and 2026-11-28 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T17-20-03-867725Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 16:34:49 | [egensolve/intelligence](https://www.nuget.org/packages/egensolve%2Fintelligence) | 0.2.0 |  | Egensolve Intelligence client for PHP |
| 2026-11-28 16:45:32 | [altlimit/altengine](https://www.nuget.org/packages/altlimit%2Faltengine) | v0.1.0 | altlimit | Official PHP SDK for altengine - managed datastore, search, and realtime channe… |
| 2026-11-28 16:50:06 | [growtask/simflex-file-manager](https://www.nuget.org/packages/growtask%2Fsimflex-file-manager) | v1.0.0 | pf; Denis Glushkov; Arseniy K… | Файловый менеджер для PHP-сайтов: окно выбора и управления файлами каталога заг… |
| 2026-11-28 16:50:06 | [simflex/file-manager](https://www.nuget.org/packages/simflex%2Ffile-manager) | v1.0.0 | pf; Denis Glushkov; Arseniy K… | Файловый менеджер для PHP-сайтов: окно выбора и управления файлами каталога заг… |
| 2026-11-28 17:04:16 | [ernestdefoe/callboard](https://www.nuget.org/packages/ernestdefoe%2Fcallboard) | 1.0.0 | Ernest Defoe | Callboard: a light sticky-note board where members post collaboration calls (lo… |
| 2026-11-28 17:05:42 | [ernestdefoe/mayfly](https://www.nuget.org/packages/ernestdefoe%2Fmayfly) | 1.0.0 | Ernest Defoe | Disappearing messages for Flarum's Messages: a timer for each conversation, cou… |
| 2026-11-28 17:06:30 | [ernestdefoe/livery](https://www.nuget.org/packages/ernestdefoe%2Flivery) | 1.0.0 | Ernest Defoe | Colors for every Flarum tag: generate a palette for all of them at once, readab… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
