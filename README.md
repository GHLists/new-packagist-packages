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

## Latest list — 2026-11-26 05:19 UTC

New packages created between 2026-11-26 04:19 UTC and 2026-11-26 05:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T05-19-23-709109Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 04:36:29 | [hipdevteam/ion-mu](https://www.nuget.org/packages/hipdevteam%2Fion-mu) | v3.6.0 | ION | ION MU — WordPress mu-plugin that fire-and-forgets activity events to Site Inte… |
| 2026-11-26 04:42:17 | [yuandianxitong/plugin-kernel](https://www.nuget.org/packages/yuandianxitong%2Fplugin-kernel) | v1.0.0 |  | Shared plugin kernel for Yuandian Webman applications |
| 2026-11-26 04:56:52 | [athenanetworks/abr](https://www.nuget.org/packages/athenanetworks%2Fabr) | 1.0 |  | A clean, modern, object-oriented client for the Australian Business Register (A… |
| 2026-11-26 05:05:59 | [hamzaahmadaslam/dbdelta-dryrun](https://www.nuget.org/packages/hamzaahmadaslam%2Fdbdelta-dryrun) | v1.0.0 | Hamza Ahmad Aslam | A WP-CLI command that creates CREATE TABLE statements under a scratch prefix, r… |
| 2026-11-26 05:06:00 | [hamzaahmadaslam/option-churn](https://www.nuget.org/packages/hamzaahmadaslam%2Foption-churn) | v1.0.0 | Hamza Ahmad Aslam | Development plugin for WordPress: counts how often each option is rewritten acr… |
| 2026-11-26 05:06:02 | [hamzaahmadaslam/woo-note-triage](https://www.nuget.org/packages/hamzaahmadaslam%2Fwoo-note-triage) | v1.0.0 | Hamza Ahmad Aslam | WooCommerce plugin that sorts the notes customers write at checkout into gift m… |
| 2026-11-26 05:10:24 | [diepxuan/laravel-catalog](https://www.nuget.org/packages/diepxuan%2Flaravel-catalog) | 2.7.3 | Tran Ngoc Duc | Catalog package for DXPanel |
| 2026-11-26 05:10:53 | [diepxuan/laravel-simba](https://www.nuget.org/packages/diepxuan%2Flaravel-simba) | 1.2.5 | Tran Ngoc Duc | Laravel Integration With Simba |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
