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

## Latest list — 2026-10-20 18:19 UTC

New packages created between 2026-10-20 17:21 UTC and 2026-10-20 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T18-19-15-598377Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 17:45:55 | [goletter/hyperf-akm](https://www.nuget.org/packages/goletter%2Fhyperf-akm) | v1.0.0 | goletter | 蓝瀚媒体代理业务 OpenAPI。Token 轮询与公共异常复用 |
| 2026-10-20 17:48:28 | [fiscalapi-br/fiscalapi-php](https://www.nuget.org/packages/fiscalapi-br%2Ffiscalapi-php) | v0.1.0 | FiscalAPI | SDK da FiscalAPI (Brasil): Inscrição Estadual, CNPJ, certidões, NF-e, SIGEF, CN… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
