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

## Latest list — 2026-10-26 19:19 UTC

New packages created between 2026-10-26 18:19 UTC and 2026-10-26 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T19-19-19-572548Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 18:24:29 | [ngoni/dischub-php](https://www.nuget.org/packages/ngoni%2Fdischub-php) | v1.0.0 | Ngonidzashe Sendama | A Laravel package for integrating with the Dischub payments API |
| 2026-10-26 18:29:56 | [noldors/phpcsfixer-rules](https://www.nuget.org/packages/noldors%2Fphpcsfixer-rules) | v0.0.1 |  | Shared PHP-CS-Fixer preset and multiline layout rules. |
| 2026-10-26 18:32:09 | [juniwalk/security](https://www.nuget.org/packages/juniwalk%2Fsecurity) | v0.1.1 | Martin Procházka | Extended security tools for Nette, starting with flexible ACL. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
