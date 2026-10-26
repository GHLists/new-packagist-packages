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

## Latest list — 2026-10-26 01:21 UTC

New packages created between 2026-10-26 00:19 UTC and 2026-10-26 01:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T01-21-21-356994Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 00:35:54 | [wilycode/validators](https://www.nuget.org/packages/wilycode%2Fvalidators) | v0.1.0 | Simon Piter | Ready-to-use validators built on the wilycode/validator contract. |
| 2026-10-26 00:40:25 | [ernestdefoe/insert-coin](https://www.nuget.org/packages/ernestdefoe%2Finsert-coin) | 1.0.1 | Ernest Defoe | Insert Coin — an arcade for Flarum. HTML5 games in a sandboxed cabinet, signed… |
| 2026-10-26 00:55:47 | [amo1943/dm-db](https://www.nuget.org/packages/amo1943%2Fdm-db) | v1.0.0 | amo | ThinkPHP ORM driver for DM(达梦),KingDatabase(金仓)。基于 bingher/db fork，适配未安装 Oracle… |
| 2026-10-26 01:06:22 | [privatus/flarum-privatus-analytics](https://www.nuget.org/packages/privatus%2Fflarum-privatus-analytics) | v1.0.0 | Two Phase LLC | Adds the cookieless Privatus Analytics tracking script to your Flarum forum, wi… |
| 2026-10-26 01:07:15 | [teamones/think-validate](https://www.nuget.org/packages/teamones%2Fthink-validate) | 3.0.0 | liu21st | Teamones think-validate fork with strict integer validation and PHP 8.5 regress… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
