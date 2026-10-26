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

## Latest list — 2026-10-26 13:21 UTC

New packages created between 2026-10-26 12:23 UTC and 2026-10-26 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T13-21-44-04117Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 12:32:52 | [pstaender/blueprintcms](https://www.nuget.org/packages/pstaender%2Fblueprintcms) | 0.1.0-alpha.1 | Philipp Staender | Blueprint CMS – a flat file CMS inspired by Kirby |
| 2026-10-26 12:36:06 | [magicoli/container-tools](https://www.nuget.org/packages/magicoli%2Fcontainer-tools) | 0.1.0-alpha.1 | Olivier van Helden | PHP library and command-line adapter for managing containers with Podman. |
| 2026-10-26 12:48:33 | [kolossusai/chat-codeigniter](https://www.nuget.org/packages/kolossusai%2Fchat-codeigniter) | v1.0.0 | Kolossus AI | Add a KolossusAI chat assistant to your CodeIgniter 4 site with one command. |
| 2026-10-26 13:02:10 | [vagebond/inertia-typegen](https://www.nuget.org/packages/vagebond%2Finertia-typegen) | v0.1.0 | Gianluca Riggio | Generate TypeScript types and route helpers for Inertia pages from Scramble's O… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
