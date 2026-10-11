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

## Latest list — 2026-10-11 03:19 UTC

New packages created between 2026-10-11 02:18 UTC and 2026-10-11 03:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T03-19-38-253527Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 02:33:04 | [aichouchm/magento2-module-attribute-import](https://www.nuget.org/packages/aichouchm%2Fmagento2-module-attribute-import) | v1.0.0 | Mehdi Aichouch | Magento 2 module for bulk importing product attribute options from CSV files vi… |
| 2026-10-11 02:39:13 | [hotkv/client](https://www.nuget.org/packages/hotkv%2Fclient) | v1.0.0 | HotKV Ltd | A high-performance PHP client for HotKV, a RESP2/RESP3-compatible in-memory dat… |
| 2026-10-11 03:01:49 | [nicklambourne/slackblocks](https://www.nuget.org/packages/nicklambourne%2Fslackblocks) | v2.7.0 |  | Native, validated Slack Block Kit values for PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
