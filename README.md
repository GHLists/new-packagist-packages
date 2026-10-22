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

## Latest list — 2026-10-22 11:20 UTC

New packages created between 2026-10-22 10:22 UTC and 2026-10-22 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T11-20-24-491863Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 10:26:17 | [contenir/contenir-preview-laminas-mvc](https://www.nuget.org/packages/contenir%2Fcontenir-preview-laminas-mvc) | v0.1.0 |  | Laminas MVC renderer for the Contenir preview protocol: answers the CMS's signe… |
| 2026-10-22 10:42:13 | [pinal-paramsoftware/laravel-rbac-suite](https://www.nuget.org/packages/pinal-paramsoftware%2Flaravel-rbac-suite) | v1.0.5 | Pinal; Parth | Enterprise-grade Role-Based Access Control (RBAC) and Multi-Layer Authenticatio… |
| 2026-10-22 11:02:30 | [emerson-ph/ai-team-setup](https://www.nuget.org/packages/emerson-ph%2Fai-team-setup) | v1.0.2 | Emerson | AI Team Setup for Laravel projects - Configure Claude Code, GitHub Copilot, Cur… |
| 2026-10-22 11:07:54 | [njamin/wp-ui](https://www.nuget.org/packages/njamin%2Fwp-ui) | v0.1.0 |  | The shared UI layer of WordPress projects: Alpine (CSP build) and Lucide icons. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
