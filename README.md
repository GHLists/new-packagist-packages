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

## Latest list — 2026-10-30 12:20 UTC

New packages created between 2026-10-30 11:21 UTC and 2026-10-30 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T12-20-46-407564Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 11:22:27 | [statikbe/craft-link-checker](https://www.nuget.org/packages/statikbe%2Fcraft-link-checker) | 1.1.0 | Statik | Finds broken links in the content of Craft CMS entries (links to deleted, disab… |
| 2026-10-30 11:36:16 | [tacraft-sociality/flarum-qq-oauth](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-qq-oauth) | 1.0.0 | TCS Dev HUB | QQ (Tencent) OAuth login for Flarum 2, with an uploadable custom login button i… |
| 2026-10-30 11:53:30 | [ryzemcbe/bedrock-protocol](https://www.nuget.org/packages/ryzemcbe%2Fbedrock-protocol) | v1.0.0-beta.1 |  | An implementation of the Minecraft: Bedrock Edition protocol in PHP |
| 2026-10-30 11:55:13 | [yuriitatur/strategies](https://www.nuget.org/packages/yuriitatur%2Fstrategies) | v0.1.0 | Yurii Tatur | A simple package to update entities in certain declarative way |
| 2026-10-30 12:00:25 | [tollwerk/tw-console](https://www.nuget.org/packages/tollwerk%2Ftw-console) | v1.0.0 | Klaus Fiedler | Collection of useful ViewHelpers |
| 2026-10-30 12:10:04 | [rishadblack/authos-client-laravel](https://www.nuget.org/packages/rishadblack%2Fauthos-client-laravel) | v0.0.1 | S M Rishad | Authos client for Laravel applications: the button block, the code exchange, th… |
| 2026-10-30 12:12:40 | [futuraweb/contao-backend-suite](https://www.nuget.org/packages/futuraweb%2Fcontao-backend-suite) | v1.0.0 | Dinko Skopljak | Backend-Werkzeuge für Contao 5 – ID-/Alias-Suche, Style-Selector für CSS-Klasse… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
