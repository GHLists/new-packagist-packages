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

## Latest list — 2026-10-13 12:19 UTC

New packages created between 2026-10-13 11:19 UTC and 2026-10-13 12:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T12-19-29-437636Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 11:19:39 | [vinrish/laravel-modules-react-starter-kit](https://www.nuget.org/packages/vinrish%2Flaravel-modules-react-starter-kit) | v1.0.1 |  | The skeleton application for the Laravel framework. |
| 2026-10-13 11:26:43 | [agrekom/customization-email-template](https://www.nuget.org/packages/agrekom%2Fcustomization-email-template) | v1.0.0 |  | Customization for Magento email templates |
| 2026-10-13 11:36:32 | [givanov95/laravel-shipping](https://www.nuget.org/packages/givanov95%2Flaravel-shipping) | v0.1.0 | Georgi Ivanov | The delivery contract between a Laravel shop and its delivery methods: one inte… |
| 2026-10-13 11:52:36 | [hyperf-apex/wecom](https://www.nuget.org/packages/hyperf-apex%2Fwecom) | v0.1.1 | lbg-sys | Apex WeCom (企业微信) toolkit for Hyperf: multi-corp account resolver, shared EasyW… |
| 2026-10-13 12:03:08 | [darvis/supplydrive-api](https://www.nuget.org/packages/darvis%2Fsupplydrive-api) | v1.0.0 | Arvid de Jong | Laravel client for the Supplydrive Portal API: fetch the delivery status of PEP… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
