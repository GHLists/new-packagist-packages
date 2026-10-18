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

## Latest list — 2026-10-18 14:18 UTC

New packages created between 2026-10-18 13:18 UTC and 2026-10-18 14:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T14-18-56-902375Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 13:20:56 | [schulit/openid-connect-provider-bundle](https://www.nuget.org/packages/schulit%2Fopenid-connect-provider-bundle) | 0.1.2 | Antonio J. García Lagar; All… | OpenID Connect provider Symfony bundle |
| 2026-10-18 13:22:07 | [slime-systems/php-slime](https://www.nuget.org/packages/slime-systems%2Fphp-slime) | v0.0.1 | Sarun Rattanasiri | Enterprise CQRS, Event Sourcing, and High-Assurance Token Infrastructure for Mo… |
| 2026-10-18 13:26:22 | [alfasix/alfakit](https://www.nuget.org/packages/alfasix%2Falfakit) | v0.1.0 | Alfa Six | The frontend-agnostic admin panel builder for Laravel. Define panels, resources… |
| 2026-10-18 13:34:01 | [eza/sdk](https://www.nuget.org/packages/eza%2Fsdk) | v0.1.0 |  | Eza Cloud for PHP: transactional email, PayEdge M-Pesa STK push and signed webh… |
| 2026-10-18 13:56:13 | [davidhirtz/website](https://www.nuget.org/packages/davidhirtz%2Fwebsite) | 3.0.2 |  | Website template for yii2-cms |
| 2026-10-18 14:17:24 | [phptailors/phpunit-recursive](https://www.nuget.org/packages/phptailors%2Fphpunit-recursive) | 2.1.0 | Paweł Tomulik | Support for recursive constraints |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
