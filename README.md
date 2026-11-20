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

## Latest list — 2026-11-20 20:19 UTC

New packages created between 2026-11-20 19:19 UTC and 2026-11-20 20:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T20-19-20-172018Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 19:30:29 | [kba-team/cakephp2-graylog](https://www.nuget.org/packages/kba-team%2Fcakephp2-graylog) | v1.0.0 |  | Graylog engine for CakePHP 2 |
| 2026-11-20 19:32:57 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.39.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-20 20:01:03 | [plutuss/static-text-filamentphp](https://www.nuget.org/packages/plutuss%2Fstatic-text-filamentphp) | v1.0.0 |  | Manage Static Text Laravel pages and localized content blocks in a Filament pan… |
| 2026-11-20 20:14:11 | [overclokk/auryn](https://www.nuget.org/packages/overclokk%2Fauryn) | v1.5.0 | Daniel Lowrey; Levi Morrison;… | Fork of rdlowrey/auryn with proxy support thanks to Ocramius/ProxyManager\|Frien… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
