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

## Latest list — 2026-09-28 10:26 UTC

New packages created between 2026-09-28 09:23 UTC and 2026-09-28 10:26 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T10-26-27-109288Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 09:24:58 | [skorlok/tacupmanager](https://www.nuget.org/packages/skorlok%2Ftacupmanager) | 1.0.1 | Skorlok | Generate a result page for TA cups |
| 2026-09-28 09:28:03 | [xddesigners/silverstripe-qr-code-generator](https://www.nuget.org/packages/xddesigners%2Fsilverstripe-qr-code-generator) | 6.1.0 | Remy Vaartjes | Create QR codes with an embedded logo and short redirect URLs, managed in the S… |
| 2026-09-28 09:40:08 | [osama-98/laravel-skills](https://www.nuget.org/packages/osama-98%2Flaravel-skills) | 1.0 | Osama Sadah | A collection of Laravel Boost guidelines and agent skills (HyperPay/OPPWA, Back… |
| 2026-09-28 09:53:28 | [huoxin/user-handles](https://www.nuget.org/packages/huoxin%2Fuser-handles) | 1.0.0 | huoxin | Display @username handles alongside nicknames across the forum. |
| 2026-09-28 09:54:32 | [dev1191/filament-nepali-address](https://www.nuget.org/packages/dev1191%2Ffilament-nepali-address) | v1.0.0 | Dev Raj Thapa | A comprehensive Nepali address plugin for Filament (v4 & v5) providing cascadin… |
| 2026-09-28 09:59:44 | [andriichuk/laravel-billing](https://www.nuget.org/packages/andriichuk%2Flaravel-billing) | 0.1.0 | Serhii Andriichuk | Vendor-agnostic subscription billing primitives for Laravel. |
| 2026-09-28 10:08:41 | [jundayw/composer-version-plugin](https://www.nuget.org/packages/jundayw%2Fcomposer-version-plugin) | v1.0.0 | jundayw | A Composer plugin for semantic version bumping, Git commit and tag automation. |
| 2026-09-28 10:10:58 | [schaefersoft/laravel-seq](https://www.nuget.org/packages/schaefersoft%2Flaravel-seq) | v1.0.0 | Luca Schäfer | Structured logging to Seq for Laravel. Ships batched CLEF events after the resp… |
| 2026-09-28 10:13:49 | [lbonnet/seo-bundle](https://www.nuget.org/packages/lbonnet%2Fseo-bundle) | v0.1.0 | lbonnet | A Symfony bundle that crawls a site once to audit its links, on-page content an… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
