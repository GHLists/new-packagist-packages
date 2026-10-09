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

## Latest list — 2026-10-09 23:20 UTC

New packages created between 2026-10-09 22:21 UTC and 2026-10-09 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T23-20-40-813334Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 22:23:05 | [usamamuneerchaudhary/laravel-slipway](https://www.nuget.org/packages/usamamuneerchaudhary%2Flaravel-slipway) | 1.2 | Usama Muneer Chaudhary | Define your CI/CD pipeline once in config/slipway.php and compile it to GitHub… |
| 2026-10-09 22:39:07 | [toreador/flarum-mail-audit](https://www.nuget.org/packages/toreador%2Fflarum-mail-audit) | v1.0.1 | Toreador | Records every outgoing Flarum email in the database and lets admins inspect rec… |
| 2026-10-09 22:56:27 | [scottoffen/markdown-converter](https://www.nuget.org/packages/scottoffen%2Fmarkdown-converter) | v1.0.0 | Scott Offen | Converts Markdown to safe HTML, with GitHub-style tables, images, and alerts. |
| 2026-10-09 23:03:20 | [fbpkg/laravel-guards](https://www.nuget.org/packages/fbpkg%2Flaravel-guards) | v0.1.0 | Farzad Sharifi | Authentication guards and session management for Laravel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
