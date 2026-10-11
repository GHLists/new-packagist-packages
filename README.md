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

## Latest list — 2026-10-11 16:19 UTC

New packages created between 2026-10-11 15:21 UTC and 2026-10-11 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T16-19-50-248411Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 15:22:28 | [hershel-theodore-layton/hack-compiler](https://www.nuget.org/packages/hershel-theodore-layton%2Fhack-compiler) | v0.0.0 |  | Hack Compiler |
| 2026-10-11 15:36:47 | [bhekor/paymish-php](https://www.nuget.org/packages/bhekor%2Fpaymish-php) | v1.0.0 | Ibidapo Adeolu | Official-style PHP SDK for the Paymish payment gateway API |
| 2026-10-11 15:41:12 | [dereuromark/cakephp-i18n-lint](https://www.nuget.org/packages/dereuromark%2Fcakephp-i18n-lint) | 0.1.0 | Mark Scherer | Keeps CakePHP translation catalogs honest: POT drift check, PO sync and PO lint… |
| 2026-10-11 15:55:30 | [jeffersongoncalves/pest-plugin-database-migrations](https://www.nuget.org/packages/jeffersongoncalves%2Fpest-plugin-database-migrations) | 1.0.0 | Jefferson Gonçalves | Load a package's migrations in tests in the exact order declared by its spatie/… |
| 2026-10-11 16:02:11 | [easyswoole/ip-access](https://www.nuget.org/packages/easyswoole%2Fip-access) | 1.0.1 |  | a simple white/black access manager |
| 2026-10-11 16:14:30 | [mageenv/module-dynamic-cart-progress-hyva](https://www.nuget.org/packages/mageenv%2Fmodule-dynamic-cart-progress-hyva) | 1.0.0 |  | Hyva storefront integration for MageEnv Dynamic Cart Progress - Alpine.js Mini… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
