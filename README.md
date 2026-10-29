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

## Latest list — 2026-10-29 13:19 UTC

New packages created between 2026-10-29 12:21 UTC and 2026-10-29 13:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T13-19-08-223912Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 12:27:17 | [nogrod/dhl-auth-php-sdk](https://www.nuget.org/packages/nogrod%2Fdhl-auth-php-sdk) | v0.1.0 | OpenAPI-Generator contributors | This API describes how API client can obtain a token which is used to access va… |
| 2026-10-29 12:29:04 | [tmonier/sylius-b2b-predictive-analytics-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-b2b-predictive-analytics-plugin) | v0.1.0 | Thibaut Monier | Predictive reorder analytics for Sylius 2 B2B: median interval calculation betw… |
| 2026-10-29 12:53:40 | [bbwdadfg/birthdaywebsite-url-tools](https://www.nuget.org/packages/bbwdadfg%2Fbirthdaywebsite-url-tools) | v0.1.0 | wangneo276-lgtm | Birthday Website Maker helps you create a personalized birthday website with ph… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
