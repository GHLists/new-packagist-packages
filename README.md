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

## Latest list — 2026-10-19 10:23 UTC

New packages created between 2026-10-19 09:21 UTC and 2026-10-19 10:23 UTC.

[Full CSV](data/new-packagist-packages-2026-10-19T10-23-04-567841Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-19 09:22:12 | [rkwebforge/bladewell](https://www.nuget.org/packages/rkwebforge%2Fbladewell) | v1.0.0 | Krishnaprasad R | Wrong name: Bladewell is bladewell/bladewell. Install it with composer require… |
| 2026-10-19 09:33:04 | [wazzapo/wazzapo-php](https://www.nuget.org/packages/wazzapo%2Fwazzapo-php) | v0.1.0 |  | PHP SDK для API Wazzapo v2: WhatsApp Business API, переписки, контакты, сделки,… |
| 2026-10-19 09:34:50 | [weldist/laravel-passport-client-scopes](https://www.nuget.org/packages/weldist%2Flaravel-passport-client-scopes) | v1.0.0 | X-Adam | Per-client default scopes and RFC 6750 insufficient_scope responses for Laravel… |
| 2026-10-19 09:44:34 | [xchert/object-schema](https://www.nuget.org/packages/xchert%2Fobject-schema) | v1.0.0 | Dustin Simon | Format-independent schemas for data structures. |
| 2026-10-19 09:49:04 | [victorio/support](https://www.nuget.org/packages/victorio%2Fsupport) | v0.1.0 |  | Shared helpers for Victorio packages. |
| 2026-10-19 09:52:46 | [jlqiumu/click-captcha](https://www.nuget.org/packages/jlqiumu%2Fclick-captcha) | 1.0.1 | wood秋木 |  |
| 2026-10-19 09:52:57 | [vanderlee/comprehend-laravel](https://www.nuget.org/packages/vanderlee%2Fcomprehend-laravel) | 1.0.1 |  | Laravel validation rules for Comprehend grammars |
| 2026-10-19 10:18:55 | [wuninsu/nativephp-mobile-scanner](https://www.nuget.org/packages/wuninsu%2Fnativephp-mobile-scanner) | v0.1.0 | Fuseini Abdul-Hafiz | QR code and barcode scanning for NativePHP Mobile apps. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
