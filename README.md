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

## Latest list — 2026-11-06 13:22 UTC

New packages created between 2026-11-06 12:22 UTC and 2026-11-06 13:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-06T13-22-08-546223Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-06 12:44:52 | [netipar/laravel-dev-login](https://www.nuget.org/packages/netipar%2Flaravel-dev-login) | v0.1.0 | NETipar | Switch-gated dev login for Laravel: sign the browser in as any user with one UR… |
| 2026-11-06 12:47:12 | [medienbaecker/kirby-base-select](https://www.nuget.org/packages/medienbaecker%2Fkirby-base-select) | 1.0.0 | Thomas Günther | A select field for the Kirby Panel with icons, images, info, fonts and themes o… |
| 2026-11-06 13:15:02 | [taba2177/log-issues-github](https://www.nuget.org/packages/taba2177%2Flog-issues-github) | v0.1.0 | taba2177 | Turn Laravel production errors into deduplicated, redacted GitHub issues that a… |
| 2026-11-06 13:20:34 | [zapj/zap-php-framework](https://www.nuget.org/packages/zapj%2Fzap-php-framework) | v1.0.9 | z | zap php framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
