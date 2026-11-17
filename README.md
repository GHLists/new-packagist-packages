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

## Latest list — 2026-11-17 00:19 UTC

New packages created between 2026-11-16 23:19 UTC and 2026-11-17 00:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T00-19-28-0101Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 23:28:43 | [jeffersongoncalves/filament-lgpd-incidents](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-lgpd-incidents) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-lgpd-incidents: register LGPD security incidents, a… |
| 2026-11-16 23:28:54 | [triploide/toolbox](https://www.nuget.org/packages/triploide%2Ftoolbox) | 1.0.2 | Maximiliano Yañez | A Laravel CRUD toolkit that auto-resolves controllers, dataproviders, repositor… |
| 2026-11-16 23:39:19 | [jeffersongoncalves/filament-lgpd-records](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-lgpd-records) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-lgpd-records: manage your LGPD records of processin… |
| 2026-11-16 23:39:23 | [emielburgman/symfony-comments](https://www.nuget.org/packages/emielburgman%2Fsymfony-comments) | v1.0.0 | Emiel Burgman | The shared half of a blog comment system for Symfony: the Doctrine columns as a… |
| 2026-11-16 23:42:43 | [joshua-barbosa/azure-blob-sdk](https://www.nuget.org/packages/joshua-barbosa%2Fazure-blob-sdk) | v0.1.0 | Joshua Barbosa | SDK PHP para o Azure Blob Storage, integrado ao Laravel: API fluente, driver de… |
| 2026-11-16 23:46:50 | [jeffersongoncalves/filament-lgpd-audit-log](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-lgpd-audit-log) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-lgpd-audit-log: browse who viewed, changed, exporte… |
| 2026-11-16 23:48:35 | [wavykit/inertia](https://www.nuget.org/packages/wavykit%2Finertia) | v0.1.0 |  | Share WavyKit pages, breadcrumbs, and menus with Inertia, with TypeScript types. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
