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

## Latest list — 2026-10-18 22:21 UTC

New packages created between 2026-10-18 21:19 UTC and 2026-10-18 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T22-21-18-182275Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 21:26:29 | [ernestdefoe/earshot](https://www.nuget.org/packages/ernestdefoe%2Fearshot) | 1.0.1 | Ernest Defoe | Podcasts that live in your forum: every episode is a discussion, the player kee… |
| 2026-10-18 21:29:39 | [stoneholl/module-order-coupon-grid-filter](https://www.nuget.org/packages/stoneholl%2Fmodule-order-coupon-grid-filter) | v1.0.0 | Stoneholl | Coupon code, coupon usage, and discount amount fields for the Magento Open Sour… |
| 2026-10-18 21:30:16 | [anun333/oe-module-care-management](https://www.nuget.org/packages/anun333%2Foe-module-care-management) | v0.1.0 | anun333 | Care management for OpenEMR: enrollment with CMS's consent elements, monthly ti… |
| 2026-10-18 21:31:04 | [kinetis/vector](https://www.nuget.org/packages/kinetis%2Fvector) | v0.9.1 | Alon Noy | A schema-driven admin platform for Kinetis applications: a compiled resource re… |
| 2026-10-18 21:31:31 | [offmania9/boostack-framework](https://www.nuget.org/packages/offmania9%2Fboostack-framework) | 6.3.9 | Stefano Spagnolo; Alessio Deb… | The Boostack core framework. |
| 2026-10-18 21:35:51 | [northstar/cipher-php](https://www.nuget.org/packages/northstar%2Fcipher-php) | v1.1.0 | Northstar Technologies | Northstar Cipher PHP SDK: field-level encryption backed by attested enclaves. |
| 2026-10-18 21:35:54 | [northstar/cipher-laravel](https://www.nuget.org/packages/northstar%2Fcipher-laravel) | v1.1.0 | Northstar Technologies | Northstar Cipher for Laravel: transparent, batched field-level encryption and b… |
| 2026-10-18 21:45:11 | [siberfx/samsa](https://www.nuget.org/packages/siberfx%2Fsamsa) | v1.1.0 | Siberfx | Kafka's model of topics, partitions, offsets and consumer groups inside Laravel… |
| 2026-10-18 21:58:22 | [falak/apm-laravel](https://www.nuget.org/packages/falak%2Fapm-laravel) | v0.1.0 |  | Falak APM for Laravel: Nightwatch-style request, query, job, cache, mail, notif… |
| 2026-10-18 22:06:49 | [zip-fa/toon](https://www.nuget.org/packages/zip-fa%2Ftoon) | v3.3.2 | Helge Sverre | Token-Oriented Object Notation - A compact data format for reducing token consu… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
