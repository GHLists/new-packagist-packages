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

## Latest list — 2026-10-03 20:19 UTC

New packages created between 2026-10-03 19:21 UTC and 2026-10-03 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-03T20-19-22-652872Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-03 19:24:09 | [justinholtweb/craft-freeride](https://www.nuget.org/packages/justinholtweb%2Fcraft-freeride) | 5.0.0 | Justin Holt | Free shipping rules for Craft Commerce — offer it, waive it, block it, and tell… |
| 2026-10-03 19:26:05 | [liyang042218/hello-thinkphp8](https://www.nuget.org/packages/liyang042218%2Fhello-thinkphp8) | v1.0.0 | liyang042218 | 一个简单的 ThinkPHP8 Composer 学习包 |
| 2026-10-03 19:27:17 | [mage2kishan/module-disable-wishlist-compare](https://www.nuget.org/packages/mage2kishan%2Fmodule-disable-wishlist-compare) | 1.0.12 |  | Disable Wishlist and Compare functionality across the entire Magento 2 frontend… |
| 2026-10-03 19:33:20 | [ernestdefoe/chronicle](https://www.nuget.org/packages/ernestdefoe%2Fchronicle) | 1.0.0 | Ernest Defoe | An Activity tab on every member's profile: the discussions they started, their… |
| 2026-10-03 19:35:01 | [ernestdefoe/kindred](https://www.nuget.org/packages/ernestdefoe%2Fkindred) | 1.0.0 | Ernest Defoe | Similar discussions at the foot of every discussion, the way traditional forums… |
| 2026-10-03 19:39:50 | [justinholtweb/craft-shipper](https://www.nuget.org/packages/justinholtweb%2Fcraft-shipper) | 5.0.0 | Justin Holt | ShipStation integration for Craft Commerce — export orders, receive tracking, q… |
| 2026-10-03 19:40:43 | [ernestdefoe/sheaf](https://www.nuget.org/packages/ernestdefoe%2Fsheaf) | 1.0.0 | Ernest Defoe | Multi-quote for Flarum: collect quotes from several posts, even across discussi… |
| 2026-10-03 19:49:51 | [ernestdefoe/rubric](https://www.nuget.org/packages/ernestdefoe%2Frubric) | 1.0.0 | Ernest Defoe | Thread prefixes for Flarum 2: a short coloured label before a discussion's titl… |
| 2026-10-03 19:53:53 | [stewart-php/mqtt](https://www.nuget.org/packages/stewart-php%2Fmqtt) | v0.2.1 |  | MQTT 3.1.1 client that connects Stewart apps to an MQTT server. Non-blocking, o… |
| 2026-10-03 20:10:25 | [dekor/devio](https://www.nuget.org/packages/dekor%2Fdevio) | v1.0.0 | Denys | Laravel-style dev & deploy scripts for Docker-based PHP projects: shell, SSH, D… |
| 2026-10-03 20:11:27 | [justinholtweb/craft-friend](https://www.nuget.org/packages/justinholtweb%2Fcraft-friend) | 5.0.0 | Justin Holt | Every dead URL has a friend. When a page 404s, Friend finds the entry the visit… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
