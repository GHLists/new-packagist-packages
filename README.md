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

## Latest list — 2026-11-08 16:20 UTC

New packages created between 2026-11-08 15:19 UTC and 2026-11-08 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T16-20-51-007346Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 15:27:33 | [deltamichael/mention-permissions](https://www.nuget.org/packages/deltamichael%2Fmention-permissions) | 0.1.0 | DeltaMichael | Restrict user mentions by Flarum group permissions. |
| 2026-11-08 15:30:18 | [jovian/venusian-ogx](https://www.nuget.org/packages/jovian%2Fvenusian-ogx) | v0.11.0 | Angel Gonzalez | The 'opengl' rendering engine for Venusian Surface: a GpuDevice over ext-opengl… |
| 2026-11-08 15:30:18 | [jovian/venusian-opengl](https://www.nuget.org/packages/jovian%2Fvenusian-opengl) | v0.11.0 | Angel Gonzalez | The 'opengl' rendering engine for Venusian Surface: a GpuDevice over ext-opengl… |
| 2026-11-08 15:31:16 | [jovian/venusian-glfw](https://www.nuget.org/packages/jovian%2Fvenusian-glfw) | v0.11.0 | Angel Gonzalez | The 'glfw' stager for Venusian Surface: staged windows on GLFW 3.4 through ext-… |
| 2026-11-08 15:32:32 | [jovian/venusian-sdl3](https://www.nuget.org/packages/jovian%2Fvenusian-sdl3) | v0.11.0 | Angel Gonzalez | The 'sdl3' rendering engine for Venusian Surface: a GpuDevice over ext-sdl3's S… |
| 2026-11-08 15:34:41 | [jovian/venusian-metal](https://www.nuget.org/packages/jovian%2Fvenusian-metal) | v0.11.0 | Angel Gonzalez | The 'metal' rendering engine for Venusian Surface: a GpuDevice over ext-metal t… |
| 2026-11-08 15:36:17 | [jovian/venusian-vulkan](https://www.nuget.org/packages/jovian%2Fvenusian-vulkan) | v0.11.0 | Angel Gonzalez | The 'vulkan' rendering engine for Venusian Surface: a GpuDevice over ext-vulkan… |
| 2026-11-08 16:14:14 | [kwaadpepper/laravel-storage-manager](https://www.nuget.org/packages/kwaadpepper%2Flaravel-storage-manager) | v0.1.0-beta.1 | Jérémy Munsch | A Laravel file manager that can handle multiple storages |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
