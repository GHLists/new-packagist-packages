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

## Latest list — 2026-10-24 15:19 UTC

New packages created between 2026-10-24 14:19 UTC and 2026-10-24 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T15-19-51-842837Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 14:20:54 | [gzxy/qiniu-php-sdk](https://www.nuget.org/packages/gzxy%2Fqiniu-php-sdk) | v7.15.0 | gzxy | Qiniu Resource (Cloud) Storage SDK for PHP |
| 2026-10-24 14:33:48 | [kris-ro/php-republic-core](https://www.nuget.org/packages/kris-ro%2Fphp-republic-core) | v1.0.0 |  | Core engine for PHP Republic MVC Framework |
| 2026-10-24 14:40:23 | [yasser-elgammal/green-auth-jwt](https://www.nuget.org/packages/yasser-elgammal%2Fgreen-auth-jwt) | v1.0.0 | Yasser Elgammal | Optional JWT authentication adapter for Green Framework v3.0 |
| 2026-10-24 14:58:52 | [xelyos/mail-rp](https://www.nuget.org/packages/xelyos%2Fmail-rp) | v1.0.0 | Team Xelyos | PHP SDK for the Mail RP API |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
