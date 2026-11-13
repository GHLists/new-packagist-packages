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

## Latest list — 2026-11-13 09:19 UTC

New packages created between 2026-11-13 08:20 UTC and 2026-11-13 09:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T09-19-26-681811Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 08:22:09 | [beromir/neos-studio-entries-editor](https://www.nuget.org/packages/beromir%2Fneos-studio-entries-editor) | v1.0.0 | Henrik Reißig | The entries editor for Neos Studio: edit a list of entries (e.g. icon, heading… |
| 2026-11-13 08:45:27 | [youvision/think-store-weather](https://www.nuget.org/packages/youvision%2Fthink-store-weather) | v1.0.0 | Youvision | ThinkPHP 8 开发期工具箱：内置开发服务器、请求轨迹追踪与端口探测。 |
| 2026-11-13 08:54:07 | [el-choco/kobalt](https://www.nuget.org/packages/el-choco%2Fkobalt) | 0.1.0-alpha.14 | el-choco | A rounded social feed theme for Flarum 2 with a top widget shelf. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
