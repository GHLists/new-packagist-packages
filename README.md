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

## Latest list — 2026-10-02 18:21 UTC

New packages created between 2026-10-02 17:20 UTC and 2026-10-02 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T18-21-08-237732Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 17:21:25 | [manuxi/sulu-conditional-validation-bundle](https://www.nuget.org/packages/manuxi%2Fsulu-conditional-validation-bundle) | v1.0.0 | Manuel Bertrams | Sulu admin forms: mandatory fields and block entries are only checked where the… |
| 2026-10-02 17:24:44 | [1994/ghostwriter-statamic](https://www.nuget.org/packages/1994%2Fghostwriter-statamic) | v1.0.0 | 1994 | Learns a site's tone of voice and image style from what it has published, then… |
| 2026-10-02 17:31:41 | [vexed/vexed](https://www.nuget.org/packages/vexed%2Fvexed) | 0.1.0 | Woody Gilk | Variable API Problem (RFC 9457) data structure |
| 2026-10-02 17:36:12 | [ua0leg/yii2-combo-tree](https://www.nuget.org/packages/ua0leg%2Fyii2-combo-tree) | 1.0.9 | Oleg | Yii2 Combo Tree Select Extension |
| 2026-10-02 17:47:50 | [mage2kishan/module-faq](https://www.nuget.org/packages/mage2kishan%2Fmodule-faq) | 1.3.6 | Kishan Savaliya | Advanced FAQ Module with multi-level assignment capabilities |
| 2026-10-02 17:52:06 | [mage2kishan/module-blog](https://www.nuget.org/packages/mage2kishan%2Fmodule-blog) | 1.3.9 | Kishan Savaliya | Panth_Blog - SEO-grade blog module for Magento 2 with first-class AEO/AIO suppo… |
| 2026-10-02 17:52:19 | [lcmialichi/php-gpu-tensors](https://www.nuget.org/packages/lcmialichi%2Fphp-gpu-tensors) | v0.1.0-beta.2 |  | Native PHP extension for NVIDIA GPU tensors, CUDA-accelerated computing, and ma… |
| 2026-10-02 17:56:12 | [mage2kishan/module-testimonials](https://www.nuget.org/packages/mage2kishan%2Fmodule-testimonials) | 1.2.7 |  | Advanced Testimonials module with slider, individual pages, categories, SEO, an… |
| 2026-10-02 17:58:14 | [momotombo/nativephp-settings](https://www.nuget.org/packages/momotombo%2Fnativephp-settings) | v1.0.0 | Momotombo | Local typed settings for NativePHP Mobile applications. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
