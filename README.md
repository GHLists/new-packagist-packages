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

## Latest list — 2026-10-02 07:20 UTC

New packages created between 2026-10-02 06:22 UTC and 2026-10-02 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T07-20-24-814458Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 06:30:23 | [mage2kishan/module-live-activity](https://www.nuget.org/packages/mage2kishan%2Fmodule-live-activity) | 1.0.12 | Kishan Savaliya | Live Activity & Social Proof notifications for Magento 2. Shows real-time custo… |
| 2026-10-02 06:50:58 | [vectorbross/vb_multilingual](https://www.nuget.org/packages/vectorbross%2Fvb_multilingual) | 1.0.0 |  | Config actions that apply the Vector BROSS translation defaults to every transl… |
| 2026-10-02 06:50:58 | [vectorbross/vb_multilingual_deepl_recipe](https://www.nuget.org/packages/vectorbross%2Fvb_multilingual_deepl_recipe) | 1.0.0 |  | The complete multilingual setup with machine translation of content by TMGMT an… |
| 2026-10-02 06:50:58 | [vectorbross/vb_multilingual_recipe](https://www.nuget.org/packages/vectorbross%2Fvb_multilingual_recipe) | 1.0.0 |  | Adds languages and makes every translatable entity type translatable. |
| 2026-10-02 07:08:29 | [akibeo/kirby-umami](https://www.nuget.org/packages/akibeo%2Fkirby-umami) | 1.0.0 | Wannes Debusschere | Umami analytics for Kirby CMS: tracker script with CSP nonce, server-side event… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
