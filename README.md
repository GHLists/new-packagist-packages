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

## Latest list — 2026-10-12 15:22 UTC

New packages created between 2026-10-12 14:21 UTC and 2026-10-12 15:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T15-22-01-00992Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 14:37:38 | [echo-fusion/framework](https://www.nuget.org/packages/echo-fusion%2Fframework) | v1.2.1 | Amir Shadanfar | The EchoFusion framework: a kernel that boots configuration, modules, service p… |
| 2026-10-12 14:45:37 | [cosmira/nginx-pushstream-broadcaster](https://www.nuget.org/packages/cosmira%2Fnginx-pushstream-broadcaster) | v1.0.0 | Alexandr Chernyaev | Laravel broadcast driver and HTTP publisher for nginx Push Stream. |
| 2026-10-12 14:51:14 | [echo-fusion/echo-fusion](https://www.nuget.org/packages/echo-fusion%2Fecho-fusion) | v1.1.0 | Amir Shadanfar | The EchoFusion application skeleton. Start a project with: composer create-proj… |
| 2026-10-12 14:51:18 | [r-portal/t-field](https://www.nuget.org/packages/r-portal%2Ft-field) | v1.0.0 | rochev yakov | Common contracts for the fields |
| 2026-10-12 14:59:58 | [pollora/attributes](https://www.nuget.org/packages/pollora%2Fattributes) | v0.1.0 | Amphibee | PHP attributes to declare WordPress post types, taxonomies, hooks, REST routes,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
