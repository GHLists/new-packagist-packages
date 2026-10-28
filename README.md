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

## Latest list — 2026-10-28 02:21 UTC

New packages created between 2026-10-28 01:20 UTC and 2026-10-28 02:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T02-21-37-916254Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 01:20:39 | [jackfinal/clike-editor](https://www.nuget.org/packages/jackfinal%2Fclike-editor) | v1.0.1 | song | Several c-lick language editor extensions for laravel-admin based on code-mirror |
| 2026-10-28 01:44:44 | [afurgeri/laravel-api-keys](https://www.nuget.org/packages/afurgeri%2Flaravel-api-keys) | v0.1.0 |  | Hashed API keys with a request guard, abilities, rotation and revocation for La… |
| 2026-10-28 01:51:30 | [google/cloud-observability](https://www.nuget.org/packages/google%2Fcloud-observability) | v0.1.0 |  | Google Cloud Observability Client for PHP |
| 2026-10-28 01:51:34 | [soerenmeier/meierlabs-seo](https://www.nuget.org/packages/soerenmeier%2Fmeierlabs-seo) | v0.1.0-alpha.0 | Sören Meier | SEO for headless Craft CMS sites built with crelte. |
| 2026-10-28 01:58:26 | [grafite/cognitive-load](https://www.nuget.org/packages/grafite%2Fcognitive-load) | v1.0.1 | Matt Lantz | An easy to run tooling for analyzing the cognitive load of the code in a Larave… |
| 2026-10-28 02:15:55 | [alibabacloud/openagent-20260801](https://www.nuget.org/packages/alibabacloud%2Fopenagent-20260801) | 1.0.0 | Alibaba Cloud SDK | Alibaba Cloud OpenAgent (20260801) SDK Library for PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
