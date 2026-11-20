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

## Latest list — 2026-11-20 17:21 UTC

New packages created between 2026-11-20 16:20 UTC and 2026-11-20 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T17-21-17-332633Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 16:23:54 | [postalkit/postalkit-php](https://www.nuget.org/packages/postalkit%2Fpostalkit-php) | v0.1.0 |  | PHP and Laravel client for the PostalKit API: Mexican postal codes (SEPOMEX), c… |
| 2026-11-20 16:35:12 | [inboundr/inboundr](https://www.nuget.org/packages/inboundr%2Finboundr) | v0.1.0 | Inboundr | PHP SDK for the Inboundr API: receive email over signed webhooks, read and repl… |
| 2026-11-20 16:45:07 | [codenyra/precognition-plus](https://www.nuget.org/packages/codenyra%2Fprecognition-plus) | v0.1.1 | CodeNyra | Checks common Laravel FormRequest rules in the browser for Precognition forms,… |
| 2026-11-20 16:56:04 | [inboundr/inboundr-laravel](https://www.nuget.org/packages/inboundr%2Finboundr-laravel) | v0.1.0 | Inboundr | Laravel integration for Inboundr: a verified webhook route that turns inbound e… |
| 2026-11-20 17:20:13 | [alibabacloud/qwenb2bmed-20261116](https://www.nuget.org/packages/alibabacloud%2Fqwenb2bmed-20261116) | 1.0.0 | Alibaba Cloud SDK | Alibaba Cloud QwenB2BMed (20261116) SDK Library for PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
