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

## Latest list — 2026-09-27 17:22 UTC

New packages created between 2026-09-27 16:19 UTC and 2026-09-27 17:22 UTC.

[Full CSV](data/new-packagist-packages-2026-09-27T17-22-15-860812Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-27 16:23:45 | [greatcode/gcurl](https://www.nuget.org/packages/greatcode%2Fgcurl) | v0.1.1 | Greatcode | Native PHP C extension and client wrapping libcurl-impersonate for browser fing… |
| 2026-09-27 16:36:07 | [dealerweb/einvoice](https://www.nuget.org/packages/dealerweb%2Feinvoice) | v1.1.0 |  | E-invoicing in pure PHP: read, validate, visualize and create XRechnung, ZUGFeR… |
| 2026-09-27 16:40:29 | [elephentity/codegen-graphql-php](https://www.nuget.org/packages/elephentity%2Fcodegen-graphql-php) | v0.1.0-alpha.1 |  | Standalone GraphQL PHP manifest generator for Elephentity. Build-time only. |
| 2026-09-27 16:40:29 | [elephentity/codegen-sqlite](https://www.nuget.org/packages/elephentity%2Fcodegen-sqlite) | v0.1.0-alpha.1 |  | SQLite storage manifest and schema generator for Elephentity. Build-time only. |
| 2026-09-27 16:48:40 | [rareform/craft-mailer](https://www.nuget.org/packages/rareform%2Fcraft-mailer) | 1.0.0 | Rareform | Send personalized emails to users, user groups and any address from the Craft c… |
| 2026-09-27 16:53:46 | [celema/server](https://www.nuget.org/packages/celema%2Fserver) | 0.1.0 | Ernst | Celema development server commands |
| 2026-09-27 16:57:37 | [nowo-tech/page-builder-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fpage-builder-kit-bundle) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Visual Symfony page builder powered by GrapesJS, with Doctrine persistence, loc… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
