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

## Latest list — 2026-11-19 17:19 UTC

New packages created between 2026-11-19 16:19 UTC and 2026-11-19 17:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T17-19-40-230615Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 16:30:06 | [juaniquillo/laravel-package-template](https://www.nuget.org/packages/juaniquillo%2Flaravel-package-template) | v0.1.0 | :author_name | :package_description |
| 2026-11-19 16:42:39 | [yu-laravel/similar-words](https://www.nuget.org/packages/yu-laravel%2Fsimilar-words) | v1.0.0 | Yuriy Akishin | Laravel Livewire tool that finds words and phrases with the closest embedding v… |
| 2026-11-19 17:14:32 | [alibabacloud/qwenb2bchat-20261105](https://www.nuget.org/packages/alibabacloud%2Fqwenb2bchat-20261105) | 1.0.0 | Alibaba Cloud SDK | Alibaba Cloud QwenB2BChat (20261105) SDK Library for PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
