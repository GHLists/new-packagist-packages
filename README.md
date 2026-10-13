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

## Latest list — 2026-10-13 11:19 UTC

New packages created between 2026-10-13 10:21 UTC and 2026-10-13 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T11-19-04-562586Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 10:34:12 | [qiangvei/magento2-module-scroll-top](https://www.nuget.org/packages/qiangvei%2Fmagento2-module-scroll-top) | 1.0.0 |  | Magento 2 Scroll To Top Floating Button Module |
| 2026-10-13 10:36:20 | [tryhackx/flarum-topic-rating](https://www.nuget.org/packages/tryhackx%2Fflarum-topic-rating) | 2.5.0 | TryHackX | Interactive 5-star topic rating system for Flarum with half-star precision, liv… |
| 2026-10-13 10:41:52 | [tiknil/backups](https://www.nuget.org/packages/tiknil%2Fbackups) | 0.1.0 | Giorgio Balduzzi | Custom backup management |
| 2026-10-13 10:46:36 | [tryhackx/flarum-thumb-sliders](https://www.nuget.org/packages/tryhackx%2Fflarum-thumb-sliders) | 2.1.7 | TryHackX | Extracts images automatically from the first post to display an animated, lazy-… |
| 2026-10-13 10:46:53 | [mariopereira/fedex](https://www.nuget.org/packages/mariopereira%2Ffedex) | v0.0.2 | Mário Pereira | A PHP interface to the Fedex's APIs |
| 2026-10-13 10:51:59 | [tablekit/filament-tablekit](https://www.nuget.org/packages/tablekit%2Ffilament-tablekit) | v5.0.0 |  | Saved table views (filters, search, sort, columns, grouping) with a favorites b… |
| 2026-10-13 10:57:50 | [bckp/translator-neon](https://www.nuget.org/packages/bckp%2Ftranslator-neon) | v1.0.0 | Radovan Kepák | Versioned NEON translation source for bckp/translator-core 3 |
| 2026-10-13 11:06:52 | [tcgunel/omnipay-odeal](https://www.nuget.org/packages/tcgunel%2Fomnipay-odeal) | v1.0.0 | Tolga Can Günel; Omnipay Cont… | Omnipay extension for Ödeal - 3D/Non-3D virtual POS payments, pay-by-link, canc… |
| 2026-10-13 11:08:55 | [shimomo/keirin-news-collector](https://www.nuget.org/packages/shimomo%2Fkeirin-news-collector) | 0.1.0 | shimomo | Collects the latest Keirin news from official feeds and APIs. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
