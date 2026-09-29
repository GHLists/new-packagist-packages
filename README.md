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

## Latest list — 2026-09-29 18:20 UTC

New packages created between 2026-09-29 17:20 UTC and 2026-09-29 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T18-20-24-605755Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 17:31:07 | [mage2kishan/module-image-seo](https://www.nuget.org/packages/mage2kishan%2Fmodule-image-seo) | 1.0.10 | Kishan Savaliya | Panth Image SEO — template-based alt/title generation for Magento 2 product ima… |
| 2026-09-29 17:49:16 | [kechankrisna/payway-partner](https://www.nuget.org/packages/kechankrisna%2Fpayway-partner) | v1.0.0 | Ke Chankrisna | ABA PayWay partner API client for PHP. Register merchants, decrypt the pushback… |
| 2026-09-29 17:52:27 | [smronju/nativephp-secure-storage](https://www.nuget.org/packages/smronju%2Fnativephp-secure-storage) | 1.0.0 | Mohammad Shoriful Islam Ronju | Implements NativePHP Mobile's SecureStorage::set()/get()/delete() on both platf… |
| 2026-09-29 18:11:15 | [payloadshield/symfonyps](https://www.nuget.org/packages/payloadshield%2Fsymfonyps) | 1.0.0 | Ganesh Kandu | Symfony bundle for encrypting and decrypting HTTP payloads |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
