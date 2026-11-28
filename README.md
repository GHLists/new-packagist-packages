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

## Latest list — 2026-11-28 00:20 UTC

New packages created between 2026-11-27 23:20 UTC and 2026-11-28 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T00-20-11-960988Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 23:32:47 | [hassan-razhei/entity-ai](https://www.nuget.org/packages/hassan-razhei%2Fentity-ai) | v1.0.0 | Hassan-Razhei | Framework-agnostic Laravel AI infrastructure SDK: agents, RAG, streaming, failo… |
| 2026-11-27 23:35:22 | [pantono/scheduler](https://www.nuget.org/packages/pantono%2Fscheduler) | 1.0.1 | Chris Burton | Scheduler Module for pantono |
| 2026-11-27 23:48:40 | [maniaba/shield-ldap](https://www.nuget.org/packages/maniaba%2Fshield-ldap) | v1.0.0 |  | LDAP and Active Directory authentication for CodeIgniter Shield |
| 2026-11-28 00:14:41 | [uxf/mailing](https://www.nuget.org/packages/uxf%2Fmailing) | 3.91.1 | UXF | React Email rendering for Symfony Mailer: ReactEmail base class, node renderer,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
