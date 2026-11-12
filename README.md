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

## Latest list — 2026-11-12 15:20 UTC

New packages created between 2026-11-12 14:21 UTC and 2026-11-12 15:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T15-20-12-771441Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 14:25:56 | [youvision/think-version](https://www.nuget.org/packages/youvision%2Fthink-version) | v1.0.0 | indiboy-create; AI | ThinkPHP 8 运行环境体检组件：查看框架版本与已安装的 Composer 依赖包。 |
| 2026-11-12 14:29:36 | [hihaho/hihaho-php](https://www.nuget.org/packages/hihaho%2Fhihaho-php) | v0.1.0 | hihaho | PHP and Laravel SDK for the hihaho API |
| 2026-11-12 14:30:19 | [prima-assicurazioni/patch-manager](https://www.nuget.org/packages/prima-assicurazioni%2Fpatch-manager) | 1.0.0 | Matteo Giachino; Mattia Basone | A library to manage patch requests |
| 2026-11-12 14:35:40 | [helsingborg-stad/acf-phone-number-field](https://www.nuget.org/packages/helsingborg-stad%2Facf-phone-number-field) | 1.0.0 |  | International phone number field for Advanced Custom Fields. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
