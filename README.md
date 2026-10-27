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

## Latest list — 2026-10-27 14:21 UTC

New packages created between 2026-10-27 13:20 UTC and 2026-10-27 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T14-21-37-901276Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 13:27:47 | [bernskiold/laravel-collaboration](https://www.nuget.org/packages/bernskiold%2Flaravel-collaboration) | v1.0.0 | Bernskiold; Erik Bernskiöld | Share Eloquent records with other users. The package has permissions, events, n… |
| 2026-10-27 13:32:19 | [dainc007/discord-rest-client](https://www.nuget.org/packages/dainc007%2Fdiscord-rest-client) | v0.1.0 | Daniel Heinze | Framework-free PHP client for the Discord REST API v10: guild, channel, role an… |
| 2026-10-27 13:47:53 | [tyto-php/helpers](https://www.nuget.org/packages/tyto-php%2Fhelpers) | v0.1.0 | Viktor Leite |  |
| 2026-10-27 13:48:35 | [tryhackx/flarum-homepage-blocks](https://www.nuget.org/packages/tryhackx%2Fflarum-homepage-blocks) | 2.12.1 | TryHackX | Customizable homepage blocks for tracker-style Flarum forums featuring dual sta… |
| 2026-10-27 13:51:20 | [nemorize/hanji](https://www.nuget.org/packages/nemorize%2Fhanji) | v0.1.0 |  | A lightweight static site generator for PHP. |
| 2026-10-27 13:59:00 | [mhinspeya/inspeya-hyva-qrloginviaapp](https://www.nuget.org/packages/mhinspeya%2Finspeya-hyva-qrloginviaapp) | 1.0.0 | MHinspeya | MHinspeya QR Login via App for Magento 2 and Hyvä. Shoppers sign in on the webs… |
| 2026-10-27 14:03:22 | [maxxksim/laravel-backup-package](https://www.nuget.org/packages/maxxksim%2Flaravel-backup-package) | v1.0.0 | Maksym | Create database backups and keep the latest N copies. |
| 2026-10-27 14:06:10 | [st-all-one/uuidv7](https://www.nuget.org/packages/st-all-one%2Fuuidv7) | v0.1.0 | St-all-one | Pure PHP RFC 9562 UUIDv7 for PHP 8.4+ with monotonic generation, parsing and Ba… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
