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

## Latest list — 2026-11-25 17:20 UTC

New packages created between 2026-11-25 16:19 UTC and 2026-11-25 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-25T17-20-36-412345Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-25 16:35:37 | [varify-io/core](https://www.nuget.org/packages/varify-io%2Fcore) | v0.1.0 |  | Framework-agnostic core of the Varify server-side SDK: local evaluation, sticky… |
| 2026-11-25 16:35:37 | [varify-io/shopware](https://www.nuget.org/packages/varify-io%2Fshopware) | v0.1.0 |  | Varify server-side A/B testing for Shopware 6.7: assignments in Twig, cache-awa… |
| 2026-11-25 16:52:24 | [laveroadmin/config](https://www.nuget.org/packages/laveroadmin%2Fconfig) | v1.0.1 | Aleksandr Kireev | Config extension for LaveroAdmin |
| 2026-11-25 16:52:24 | [laveroadmin/wafu](https://www.nuget.org/packages/laveroadmin%2Fwafu) | v1.0.1 | Aleksandr Kireev | WAFU Firewall management extension for LaveroAdmin |
| 2026-11-25 17:03:42 | [brace/core](https://www.nuget.org/packages/brace%2Fcore) | v1.0.0 | Matthias Leuffen | Modular Microservice Framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
