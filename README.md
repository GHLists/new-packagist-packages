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

## Latest list — 2026-11-12 13:21 UTC

New packages created between 2026-11-12 12:19 UTC and 2026-11-12 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T13-21-17-769287Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 12:24:03 | [comprestack/sdk](https://www.nuget.org/packages/comprestack%2Fsdk) | v0.1.0 | Comprestack | Official PHP SDK for the Comprestack image optimization API |
| 2026-11-12 12:34:42 | [relwave/relwave-php](https://www.nuget.org/packages/relwave%2Frelwave-php) | v1.0.0 | mgsoft | Official PHP SDK for the Relwave /api/v1 transactional and audience API. |
| 2026-11-12 12:37:48 | [innmind/frame](https://www.nuget.org/packages/innmind%2Fframe) | 1.0.0 | Baptiste Langlade |  |
| 2026-11-12 12:48:03 | [openupi/gateway](https://www.nuget.org/packages/openupi%2Fgateway) | v0.1.0 |  | PHP server SDK for the OpenUPI merchant gateway: create orders, read them, refu… |
| 2026-11-12 12:57:13 | [humanmade/elasticpress-verify-index](https://www.nuget.org/packages/humanmade%2Felasticpress-verify-index) | 0.1.0 | Human Made | WP-CLI command that checks a random sample of posts against the ElasticPress in… |
| 2026-11-12 12:58:08 | [limegreentangerine/seo_kit](https://www.nuget.org/packages/limegreentangerine%2Fseo_kit) | 1.0.0 | Dave Hendy | SEO kit for Concrete5 |
| 2026-11-12 13:03:14 | [proxyverity/proxy-checker-widget](https://www.nuget.org/packages/proxyverity%2Fproxy-checker-widget) | v1.0.0 | ProxyVerity | Embeddable proxy checker widget: one script tag puts a working HTTP/HTTPS/SOCKS… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
