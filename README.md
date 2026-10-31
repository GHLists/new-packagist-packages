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

## Latest list — 2026-10-31 08:20 UTC

New packages created between 2026-10-31 07:18 UTC and 2026-10-31 08:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T08-20-56-736501Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 07:23:55 | [nowo-tech/milkdown-editor-bundle](https://www.nuget.org/packages/nowo-tech%2Fmilkdown-editor-bundle) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Symfony form type for Markdown editing with Milkdown and a reduced Crepe build,… |
| 2026-10-31 07:39:40 | [atannex/bridge](https://www.nuget.org/packages/atannex%2Fbridge) | v1.0.0 | Atanga Leke Collins | Expose explicitly registered, validated and authorized Laravel operations to Ja… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
