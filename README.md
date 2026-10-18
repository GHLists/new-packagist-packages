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

## Latest list — 2026-10-18 07:19 UTC

New packages created between 2026-10-18 06:19 UTC and 2026-10-18 07:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T07-19-31-893784Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 06:22:30 | [tezz/auth-sdk](https://www.nuget.org/packages/tezz%2Fauth-sdk) | v1.0.0 | TezzCorp Pvt. Ltd. | Official PHP SDK for Tezz Auth |
| 2026-10-18 06:35:58 | [malikad/laravel-tenant-guard](https://www.nuget.org/packages/malikad%2Flaravel-tenant-guard) | v1.0.0 | Malik Adnan | AST static analysis guard for Laravel multi-tenant SaaS applications preventing… |
| 2026-10-18 06:49:03 | [kandita/paydita](https://www.nuget.org/packages/kandita%2Fpaydita) | v1.0.0 |  | Laravel client for Paydita, the internal central payment API of PT. Kandita Dig… |
| 2026-10-18 07:07:38 | [webx-ui/module-debug](https://www.nuget.org/packages/webx-ui%2Fmodule-debug) | v0.78.0 | WebX UI | A debug bar at the bottom of a WebX UI site's pages, for an administrator and n… |
| 2026-10-18 07:12:03 | [phattarachai/worktree-prompt](https://www.nuget.org/packages/phattarachai%2Fworktree-prompt) | v1.0.0 | Phattarachai | Set up a git worktree of a Laravel project in one command — real vendor, .env,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
