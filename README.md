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

## Latest list — 2026-10-16 14:20 UTC

New packages created between 2026-10-16 13:20 UTC and 2026-10-16 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T14-20-52-692747Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 13:24:33 | [everysize/checkout-oscommerce](https://www.nuget.org/packages/everysize%2Fcheckout-oscommerce) | 1.0.1 | everysize GmbH | everysize Checkout – Erweiterung für osCommerce 4 |
| 2026-10-16 13:24:36 | [everysize/checkout-phoenix-cart](https://www.nuget.org/packages/everysize%2Fcheckout-phoenix-cart) | 1.0.0 | everysize GmbH | everysize Checkout – Add-on für CE Phoenix Cart |
| 2026-10-16 13:41:24 | [tyhp/io](https://www.nuget.org/packages/tyhp%2Fio) | 805.0.2 |  | Tyhp runtime io (PHP 8.5) — HTTP, processes, files, sockets, Redis, and databas… |
| 2026-10-16 13:43:49 | [astral-php/astral-shop](https://www.nuget.org/packages/astral-php%2Fastral-shop) | 1.0.0 |  | Astral Shop — boutique e-commerce démo (en développement) |
| 2026-10-16 13:46:07 | [tyhp/parallel](https://www.nuget.org/packages/tyhp%2Fparallel) | 805.0.2 |  | Tyhp runtime parallel (PHP 8.5) — process pool for isolated CPU work |
| 2026-10-16 13:53:38 | [zeliard91/parse-php-sdk](https://www.nuget.org/packages/zeliard91%2Fparse-php-sdk) | 2.5.0 | Parse | Parse PHP SDK (fork with PHP 8.4+ support) |
| 2026-10-16 14:03:30 | [dwivedianuj9118/mediaflow-laravel](https://www.nuget.org/packages/dwivedianuj9118%2Fmediaflow-laravel) | v1.0.0-beta.1 | Anuj Dwivedi | Universal media management infrastructure and UI for Laravel applications |
| 2026-10-16 14:14:55 | [unione-repo/unione-laravel](https://www.nuget.org/packages/unione-repo%2Funione-laravel) | 2.1.2 |  | UniOne Web API for Laravel: API client, mail transport, webhooks |
| 2026-10-16 14:15:07 | [unione-repo/unione-symfony-bundle](https://www.nuget.org/packages/unione-repo%2Funione-symfony-bundle) | 2.1.2 |  | UniOne Web API for Symfony: API client services, Symfony Mailer transport, webh… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
