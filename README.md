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

## Latest list — 2026-10-30 19:20 UTC

New packages created between 2026-10-30 18:21 UTC and 2026-10-30 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T19-20-22-734826Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 18:24:38 | [organiseyou/mcp-server](https://www.nuget.org/packages/organiseyou%2Fmcp-server) | v1.1.0 |  | Drop-in MCP (Model Context Protocol) server for Laravel applications |
| 2026-10-30 18:40:23 | [ernestdefoe/kiosk](https://www.nuget.org/packages/ernestdefoe%2Fkiosk) | 1.0.1 | Ernest Defoe | Kiosk — sell anything on your Flarum forum: memberships, premium tags, single d… |
| 2026-10-30 18:46:16 | [tacraft-sociality/flarum-microsoft-oauth](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-microsoft-oauth) | 1.0.0 | Tacraft Sociality | Log in to your Flarum forum with Microsoft |
| 2026-10-30 18:46:44 | [craigsimps/assertpdf](https://www.nuget.org/packages/craigsimps%2Fassertpdf) | v0.1.0 |  | Pest and PHPUnit assertions against real PDF text, pages and rendered snapshots. |
| 2026-10-30 19:01:34 | [tacraft-sociality/flarum-github-oauth](https://www.nuget.org/packages/tacraft-sociality%2Fflarum-github-oauth) | 1.0.0 | TCS Dev Hub | GitHub OAuth login for Flarum 2, with account linking in the security settings. |
| 2026-10-30 19:03:19 | [dr2gsistemas/erplibs](https://www.nuget.org/packages/dr2gsistemas%2Ferplibs) | v1.1.0 | dr2gsistemas | Librería PHP 8.4+ para ERP: ORM por atributos, migraciones, eventos, validación… |
| 2026-10-30 19:14:44 | [zapsmtp/zapsmtp-php](https://www.nuget.org/packages/zapsmtp%2Fzapsmtp-php) | v0.1.0-beta.1 |  | The official PHP SDK for the ZapSMTP email API |
| 2026-10-30 19:14:49 | [zapsmtp/zapsmtp-laravel](https://www.nuget.org/packages/zapsmtp%2Fzapsmtp-laravel) | v0.1.0-beta.1 |  | The official Laravel integration for the ZapSMTP email API: mail driver, webhoo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
