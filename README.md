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

## Latest list — 2026-10-08 12:18 UTC

New packages created between 2026-10-08 11:18 UTC and 2026-10-08 12:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T12-18-52-719439Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 11:29:09 | [connetation/t3wtk-quickstart-shell](https://www.nuget.org/packages/connetation%2Ft3wtk-quickstart-shell) | 3.1.1 | Connetation Web Engineering G… | DDEV quickstart for TYPO3 14 projects built on the Connetation TYPO3 Web Toolki… |
| 2026-10-08 11:44:04 | [jevo/jrelations](https://www.nuget.org/packages/jevo%2Fjrelations) | 1.0.2 |  | Двосторонні зв’язки між ресурсами для Evolution CMS |
| 2026-10-08 11:45:22 | [laranex/laravel-money](https://www.nuget.org/packages/laranex%2Flaravel-money) | v4.0.0-alpha.1 | Nay Thu Khant | Money for Laravel: exact, currency-aware amounts with arithmetic, percentages,… |
| 2026-10-08 11:45:44 | [laranex/php-myanmar-payments](https://www.nuget.org/packages/laranex%2Fphp-myanmar-payments) | v4.0.0-alpha.1 | Nay Thu Khant | PHP SDK for Myanmar payment gateways: KBZ Pay, Wave Money, AYA Pay, Yoma MMQR a… |
| 2026-10-08 11:51:28 | [stougeiro/view](https://www.nuget.org/packages/stougeiro%2Fview) | v1.0.0 | stougeiro | A light, engine-agnostic view layer for PHP. It resolves view identifiers (dot… |
| 2026-10-08 11:54:15 | [onkud/data-structures](https://www.nuget.org/packages/onkud%2Fdata-structures) | v1.0.0 | Onur Kudret | Stack, Queue, and LinkedList implementations with Laravel and Symfony support |
| 2026-10-08 12:08:14 | [jobmetric/laravel-post](https://www.nuget.org/packages/jobmetric%2Flaravel-post) | v1.0.1 | Majid Mohammadian | This is a post management package for Laravel that you can use in your projects. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
