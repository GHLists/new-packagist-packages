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

## Latest list — 2026-10-02 22:19 UTC

New packages created between 2026-10-02 21:22 UTC and 2026-10-02 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T22-19-33-029114Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 21:27:45 | [sympress/starter](https://www.nuget.org/packages/sympress%2Fstarter) | v1.0.0 |  | SymPress Starter for WordPress projects |
| 2026-10-02 21:28:50 | [sympress/demo](https://www.nuget.org/packages/sympress%2Fdemo) | v1.0.0 |  | Reference WordPress website demonstrating structured development with SymPress… |
| 2026-10-02 22:02:33 | [siol-data/linkml-connector](https://www.nuget.org/packages/siol-data%2Flinkml-connector) | v2.0.5 |  | DFC LinkML Semantic Object Connector for PHP |
| 2026-10-02 22:14:03 | [stanislas-poisson/french-postal-code](https://www.nuget.org/packages/stanislas-poisson%2Ffrench-postal-code) | 4.0.0 | Stanislas Poisson | The regions, departments, communes and postal codes of France, with one GPS poi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
