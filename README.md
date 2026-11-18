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

## Latest list — 2026-11-18 14:21 UTC

New packages created between 2026-11-18 13:20 UTC and 2026-11-18 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T14-21-09-335488Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 13:30:20 | [el-choco/error-analyzer](https://www.nuget.org/packages/el-choco%2Ferror-analyzer) | v0.1.0-alpha.2 | el-choco | Group Flarum log errors, identify packages mentioned in stack traces, and prepa… |
| 2026-11-18 13:30:23 | [tornado-engine/notifications](https://www.nuget.org/packages/tornado-engine%2Fnotifications) | v0.1.0 |  | Tornado Engine core-module: the notification bell in the menu bar, with modules… |
| 2026-11-18 13:49:57 | [qiick/laravel-oidc](https://www.nuget.org/packages/qiick%2Flaravel-oidc) | 1.0.0-beta.1 | Qiick | OpenID Connect client for Laravel: PKCE, id_token validation, logout, role mapp… |
| 2026-11-18 13:55:19 | [phactorial/phactorial](https://www.nuget.org/packages/phactorial%2Fphactorial) | v0.18.0 | One Learning Community | Math typesetting in plain PHP: reads TeX and MathML, writes SVG, PNG, MathML, T… |
| 2026-11-18 13:59:20 | [gadwinn/framework](https://www.nuget.org/packages/gadwinn%2Fframework) | v0.1.0 |  | Lightweight PSR-7/PSR-15 framework assembling the gadwinn/* packages. |
| 2026-11-18 14:01:22 | [phactorial/commonmark](https://www.nuget.org/packages/phactorial%2Fcommonmark) | v0.18.0 | One Learning Community | GitHub's math syntax for league/commonmark, typeset on the server as SVG or Mat… |
| 2026-11-18 14:02:25 | [gadwinn/skeleton](https://www.nuget.org/packages/gadwinn%2Fskeleton) | v0.1.0 |  | Starting project for gadwinn/framework applications. |
| 2026-11-18 14:17:35 | [kafyx-3/laravel-datatables-export](https://www.nuget.org/packages/kafyx-3%2Flaravel-datatables-export) | v1.0.0 | kafyx-3 | Shortcut DataTables v2 + Export buttons tanpa jQuery untuk Laravel. |
| 2026-11-18 14:19:49 | [bertrapp/corretor-php](https://www.nuget.org/packages/bertrapp%2Fcorretor-php) | v0.2.0 |  | Padrão de código verificável por ferramenta: analisa projetos Laravel e Node/Ty… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
