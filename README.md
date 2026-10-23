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

## Latest list — 2026-10-23 12:18 UTC

New packages created between 2026-10-23 11:21 UTC and 2026-10-23 12:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-23T12-18-47-563586Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-23 11:34:05 | [stewart-php/phpstan](https://www.nuget.org/packages/stewart-php%2Fphpstan) | v1.8.0 |  | PHPStan rules that check Home Assistant entity IDs and action names against a S… |
| 2026-10-23 11:37:37 | [julienbohy/cyberkh-starter-template](https://www.nuget.org/packages/julienbohy%2Fcyberkh-starter-template) | v1.1.0 |  | Symfony 8.1 starter template: PHP 8.5, Doctrine/PostgreSQL, users with email ve… |
| 2026-10-23 11:38:19 | [openglacier/glacierdb](https://www.nuget.org/packages/openglacier%2Fglacierdb) | v0.1.0 | OpenGlacier contributors | PHP driver for glacierdb with core-managed .ogid identities |
| 2026-10-23 11:53:54 | [shahinmoyshan/pusher-php-server](https://www.nuget.org/packages/shahinmoyshan%2Fpusher-php-server) | v7.3.1 |  | Pusher Client fine-tuned for tinymvc/spark php framework |
| 2026-10-23 12:04:34 | [ez-php/sms](https://www.nuget.org/packages/ez-php%2Fsms) | 2.5.10 | Andreas Uretschnig | SMS delivery (Twilio, Vonage, Log, Null drivers) over ez-php/http-client |
| 2026-10-23 12:13:44 | [haoa/mix-http-message](https://www.nuget.org/packages/haoa%2Fmix-http-message) | v3.0.32 | liu,jian | Http message library based on PSR-7 / PSR-17 standard, support Swoole, WorkerMan |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
