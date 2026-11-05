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

## Latest list — 2026-11-05 02:19 UTC

New packages created between 2026-11-05 01:20 UTC and 2026-11-05 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T02-19-03-23589Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 01:26:45 | [webware/query-param-router](https://www.nuget.org/packages/webware%2Fquery-param-router) | 1.0.0-alpha.3 | Joey (aka Tyrsson) Smith | Mezzio router that matches routes on query parameters as well as path and HTTP… |
| 2026-11-05 01:26:45 | [webware/smf-legacy-router](https://www.nuget.org/packages/webware%2Fsmf-legacy-router) | 1.0.0-alpha.3 | Joey (aka Tyrsson) Smith | Mezzio router that matches routes on query parameters as well as path and HTTP… |
| 2026-11-05 01:29:34 | [email-validation/sdk](https://www.nuget.org/packages/email-validation%2Fsdk) | v1.0.0 | email-validation.org | Official PHP client for the email-validation.org email validation API. |
| 2026-11-05 01:37:55 | [waffle-commons/testing](https://www.nuget.org/packages/waffle-commons%2Ftesting) | 0.1.0-beta7 | Leslie Petrimaux | Kernel testing bridge for the Waffle framework: in-process request dispatch thr… |
| 2026-11-05 01:39:38 | [waffle-commons/openapi](https://www.nuget.org/packages/waffle-commons%2Fopenapi) | 0.1.0-beta7 | Leslie Petrimaux | OpenAPI 3.1 document generation for the Waffle framework, built from #[Route] a… |
| 2026-11-05 01:39:46 | [waffle-commons/serializer](https://www.nuget.org/packages/waffle-commons%2Fserializer) | 0.1.0-beta7 | Leslie Petrimaux | Compiled, reflection-free DTO serialization and Accept-header content negotiati… |
| 2026-11-05 01:45:58 | [waffle-commons/queue](https://www.nuget.org/packages/waffle-commons%2Fqueue) | 0.1.0-beta7 | Leslie Petrimaux | Background job processing for the Waffle framework: a Redis Streams driver with… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
