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

## Latest list — 2026-10-04 23:19 UTC

New packages created between 2026-10-04 22:19 UTC and 2026-10-04 23:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T23-19-17-626412Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 22:24:33 | [mage2kishan/module-hreflang](https://www.nuget.org/packages/mage2kishan%2Fmodule-hreflang) | 1.0.26 | Kishan Savaliya | Panth Hreflang — multi-language/multi-region hreflang link tags for Magento 2 w… |
| 2026-10-04 22:35:11 | [justinholtweb/craft-tape](https://www.nuget.org/packages/justinholtweb%2Fcraft-tape) | 5.0.0 | Justin Holt | Conversion tracking for Craft CMS — Google Ads, GA4, Meta, TikTok and a dozen m… |
| 2026-10-04 22:55:45 | [mage2kishan/module-robots-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-robots-seo) | 1.3.5 | Kishan Savaliya | Panth Robots SEO — dedicated robots.txt, X-Robots-Tag, and LLM-bot (GPTBot, Cla… |
| 2026-10-04 23:17:30 | [mage2kishan/module-eu-withdrawal](https://www.nuget.org/packages/mage2kishan%2Fmodule-eu-withdrawal) | 1.1.9 | Kishan Savaliya | Panth EU Withdrawal Button - a clear, accessible digital withdrawal (cancellati… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
