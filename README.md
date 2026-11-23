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

## Latest list — 2026-11-23 01:19 UTC

New packages created between 2026-11-23 00:18 UTC and 2026-11-23 01:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-23T01-19-49-06629Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-23 00:20:22 | [davereid/drupal-gitlab-api-docs](https://www.nuget.org/packages/davereid%2Fdrupal-gitlab-api-docs) | 1.0.0 | Dave Reid | Generates API docs for a Drupal module's MkDocs site with phpDocumentor, includ… |
| 2026-11-23 01:15:53 | [mgamadeus/ddd-clouddrive](https://www.nuget.org/packages/mgamadeus%2Fddd-clouddrive) | 0.1.0-rc.1 | Marius-Eugen Gerdan | Cloud drive for mgamadeus/ddd: spaces with host-owned rights, versioned files i… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
