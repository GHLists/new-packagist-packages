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

## Latest list — 2026-11-23 15:22 UTC

New packages created between 2026-11-23 14:20 UTC and 2026-11-23 15:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T15-22-38-591633Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 14:35:21 | [p6g9yhk6/relay_tracking](https://www.nuget.org/packages/p6g9yhk6%2Frelay_tracking) | 1.0.0 | P6g9YHK6 | Per recipient delivery tracking of sent mail (delivered, opened, clicked, bounc… |
| 2026-11-23 14:50:29 | [alexandrebulete/ddd-media-bundle](https://www.nuget.org/packages/alexandrebulete%2Fddd-media-bundle) | 1.0.0 | Alexandre Bulete | A media library as a reusable DDD Bounded Context: files on Flysystem, resized… |
| 2026-11-23 14:57:35 | [webpatser/resonate-upstream](https://www.nuget.org/packages/webpatser%2Fresonate-upstream) | v0.1.0 | Christoph Kempen | Subscribe a Resonate server to external sockets (Socket.IO v4 or plain websocke… |
| 2026-11-23 15:06:53 | [filafly/filament-tabler-icons](https://www.nuget.org/packages/filafly%2Ffilament-tabler-icons) | v1.0.0 | Nolan Nordlund | Tabler Icons pack for Filament Icons: replaces every Filament UI icon with Tabl… |
| 2026-11-23 15:13:39 | [drupal/display_builder_ai_recipe](https://www.nuget.org/packages/drupal%2Fdisplay_builder_ai_recipe) | 1.0.0-alpha1 | Jean Valverde | Adds the Display Builder AI assistant to a Display Builder site, with an AI pro… |
| 2026-11-23 15:15:45 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.48.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
