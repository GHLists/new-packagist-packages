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

## Latest list — 2026-09-27 13:19 UTC

New packages created between 2026-09-27 12:20 UTC and 2026-09-27 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-09-27T13-19-51-99246Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-27 12:23:48 | [venusian/surface](https://www.nuget.org/packages/venusian%2Fsurface) | 0.8.0 | Angel Gonzalez | The Venusian Display Panel Framework. |
| 2026-09-27 12:29:41 | [mammatus/http-server-contracts](https://www.nuget.org/packages/mammatus%2Fhttp-server-contracts) | 0.1.0 |  | Contracts for the HTTP server |
| 2026-09-27 12:41:01 | [mammatus/http-server-webroot](https://www.nuget.org/packages/mammatus%2Fhttp-server-webroot) | 0.1.2 |  | HTTP Server webroot implementations |
| 2026-09-27 12:51:19 | [webx-ui/module-press](https://www.nuget.org/packages/webx-ui%2Fmodule-press) | v0.44.0 | WebX UI | Press for the WebX UI admin panel: the outlets that wrote about the site — a lo… |
| 2026-09-27 12:56:15 | [ipf/newsman](https://www.nuget.org/packages/ipf%2Fnewsman) | 1.0.0 |  | Newsman subscription extension with Mailman integration |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
