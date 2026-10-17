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

## Latest list — 2026-10-17 21:20 UTC

New packages created between 2026-10-17 20:21 UTC and 2026-10-17 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T21-20-10-732845Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 20:24:40 | [sascha-mueller/contao-little-canary](https://www.nuget.org/packages/sascha-mueller%2Fcontao-little-canary) | v1.0.0 | Sascha Müller | Little Canary – minimal single-page demo theme for Contao 5.7. Check that your… |
| 2026-10-17 20:42:44 | [stefanak-michal/grafeo-php](https://www.nuget.org/packages/stefanak-michal%2Fgrafeo-php) | v0.5.44 | Michal Stefanak | FFI implementation to run Grafeo embedded in PHP |
| 2026-10-17 20:45:49 | [1994/social-images-core](https://www.nuget.org/packages/1994%2Fsocial-images-core) | v1.0.0 | 1994 | The shared core of 1994's Social Images products: the template format, the page… |
| 2026-10-17 20:52:16 | [shire-studio/laravel-starter-kit-cli](https://www.nuget.org/packages/shire-studio%2Flaravel-starter-kit-cli) | v1.0.1 |  | Create new projects from the Shire Studio Laravel starter kit and keep existing… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
