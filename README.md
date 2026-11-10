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

## Latest list — 2026-11-10 02:21 UTC

New packages created between 2026-11-10 01:20 UTC and 2026-11-10 02:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T02-21-59-843698Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 01:21:07 | [raneomik/tracy-dark-mode](https://www.nuget.org/packages/raneomik%2Ftracy-dark-mode) | v0.1.0 |  | Dark theme for the Tracy bar, its panels and the bluescreen, with a toggle |
| 2026-11-10 01:23:14 | [pirulug/qbgen](https://www.nuget.org/packages/pirulug%2Fqbgen) | 0.0.1 | Pirulug | Libreria PHP para la generacion y renderizado de codigos QR y codigos de barras… |
| 2026-11-10 01:40:04 | [solophp/image](https://www.nuget.org/packages/solophp%2Fimage) | v1.0.0-RC1 | Vitaliy Olos | Immutable GD images for PHP: EXIF orientation, bounded resizing, JPEG/PNG/WebP… |
| 2026-11-10 01:57:17 | [mgamadeus/ddd-design-studio](https://www.nuget.org/packages/mgamadeus%2Fddd-design-studio) | 0.1.0 | Marius-Eugen Gerdan | Design review studio for mgamadeus/ddd — shows the design boards of a checkout… |
| 2026-11-10 02:02:24 | [puggan/untrusted-value](https://www.nuget.org/packages/puggan%2Funtrusted-value) | v0.1.0 | Thorbjörn Puggan Sundragon | Turn untrusted input values into type-safe values, with optional validation. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
