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

## Latest list — 2026-11-27 23:20 UTC

New packages created between 2026-11-27 22:20 UTC and 2026-11-27 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T23-20-35-320151Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 22:27:28 | [b4n1/b4n1-audit](https://www.nuget.org/packages/b4n1%2Fb4n1-audit) | v0.1.6 | Bani Montoya | Sovereign security audit - static analysis engine |
| 2026-11-27 22:32:56 | [neo-digital/contao-indexnow-bundle](https://www.nuget.org/packages/neo-digital%2Fcontao-indexnow-bundle) | v1.0.0 | NEO Digital | IndexNow for Contao 5: tells Bing, Yandex, Seznam, Naver and Yep within minutes… |
| 2026-11-27 22:38:10 | [debuss-a/piccolo-database](https://www.nuget.org/packages/debuss-a%2Fpiccolo-database) | 0.1.0 | Alexandre Debusschère | Database access through stored procedures only for Piccolo: a class per procedu… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
