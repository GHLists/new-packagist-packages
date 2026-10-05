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

## Latest list — 2026-10-05 12:19 UTC

New packages created between 2026-10-05 11:18 UTC and 2026-10-05 12:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-05T12-19-11-131487Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 11:34:22 | [mage2kishan/module-extra-fee](https://www.nuget.org/packages/mage2kishan%2Fmodule-extra-fee) | 1.1.7 | Kishan Savaliya | Panth Extra Fee — add configurable extra fees and surcharges to Magento 2 check… |
| 2026-10-05 11:35:12 | [silarhi/llms-txt-bundle](https://www.nuget.org/packages/silarhi%2Fllms-txt-bundle) | v1.1.1 | Guillaume Sainthillier | Build, dump and serve an llms.txt file from your Symfony application, the Prest… |
| 2026-10-05 11:57:14 | [abdelhmed/sentinel-ai](https://www.nuget.org/packages/abdelhmed%2Fsentinel-ai) | v1.0.1 | Abdelhamed Fathy | AI-powered error dashboard for Laravel: captures exceptions, explains them with… |
| 2026-10-05 12:10:31 | [limegreentangerine/aws_hosting](https://www.nuget.org/packages/limegreentangerine%2Faws_hosting) | 1.0.0 | Lee Jones | ConcreteCMS tools for AWS hosted deployments |
| 2026-10-05 12:15:25 | [mage2kishan/magento2-claude-ai](https://www.nuget.org/packages/mage2kishan%2Fmagento2-claude-ai) | 1.9.3 | Kishan Savaliya | Magento 2 Automation with Claude AI - natural-language store management. Update… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
