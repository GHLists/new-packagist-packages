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

## Latest list — 2026-10-10 07:18 UTC

New packages created between 2026-10-10 06:20 UTC and 2026-10-10 07:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T07-18-53-335369Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 06:40:01 | [novora/kaizen-bundle](https://www.nuget.org/packages/novora%2Fkaizen-bundle) | v1.0.0 | Novora Labs | Lean continuous improvement for Symfony applications |
| 2026-10-10 07:00:59 | [keenthekeen/oauth-helper](https://www.nuget.org/packages/keenthekeen%2Foauth-helper) | v0.1.0 |  | OAuth 2.0 / OpenID Connect helpers for Laravel apps (internal use) |
| 2026-10-10 07:10:52 | [naf/alexa](https://www.nuget.org/packages/naf%2Falexa) | v0.1.0 | Flo Knapp | Alexa+ MCP integration, OAuth setup and diagnostics for NAF. |
| 2026-10-10 07:11:09 | [vondry/bolt-skills](https://www.nuget.org/packages/vondry%2Fbolt-skills) | v1.0.0 | Tomáš Vondráček | Collection of AI agent skills, workflows, and runbooks for Bolt CMS |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
