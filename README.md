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

## Latest list — 2026-11-19 08:19 UTC

New packages created between 2026-11-19 07:21 UTC and 2026-11-19 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T08-19-37-684864Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 07:29:09 | [cartwright-jp/php-imap-mcp](https://www.nuget.org/packages/cartwright-jp%2Fphp-imap-mcp) | v0.1.0 | Kazuki Aruga (Cartwright) | Remote MCP server in PHP for reading, searching and drafting IMAP mail on share… |
| 2026-11-19 07:39:32 | [stolt/hyde-llms-txt](https://www.nuget.org/packages/stolt%2Fhyde-llms-txt) | v0.9.0 | Raphael Stolt | A HydePHP extension that generates an llms.txt file from site content during a… |
| 2026-11-19 07:49:44 | [poppy/faker](https://www.nuget.org/packages/poppy%2Ffaker) | 4.3.1-rc.1 | Mark Zhao; François Zaninotto | Poppy Faker is a PHP library that generates fake data for zh user. |
| 2026-11-19 08:04:40 | [anamcoollzz/laravel-stisla-package](https://www.nuget.org/packages/anamcoollzz%2Flaravel-stisla-package) | v1.0.1 |  | Publishable Laravel Stisla admin panel, auth, RBAC, and modular app starter pac… |
| 2026-11-19 08:04:43 | [mertaydin/laravel-server-security-update-monitor](https://www.nuget.org/packages/mertaydin%2Flaravel-server-security-update-monitor) | v0.1.4 | Mert Aydın | Monitor Linux server package updates and security patches from a Laravel dashbo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
