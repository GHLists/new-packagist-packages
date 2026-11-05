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

## Latest list — 2026-11-05 17:19 UTC

New packages created between 2026-11-05 16:20 UTC and 2026-11-05 17:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T17-19-04-062542Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 16:43:58 | [happenv-com/filament-model-search](https://www.nuget.org/packages/happenv-com%2Ffilament-model-search) | v0.1.0 | Happenv sp. z o.o.; webard | Filament integration for happenv-com/laravel-model-search: a command palette, t… |
| 2026-11-05 16:54:09 | [augustash/mna_offers](https://www.nuget.org/packages/augustash%2Fmna_offers) | 1.0.3 |  | Schedules the offers on Minnesota Air dealer sites from one screen and imports… |
| 2026-11-05 16:58:06 | [getodden/botguard](https://www.nuget.org/packages/getodden%2Fbotguard) | v0.1.0 |  | Progressive bot protection for Laravel forms: honeypot, timing, rate limits, so… |
| 2026-11-05 16:59:38 | [payerurl/telegram-crypto-gateway-instant-payout](https://www.nuget.org/packages/payerurl%2Ftelegram-crypto-gateway-instant-payout) | 1.0.1 | Rashiqul Rony | telegram crypto payment gateway laravel |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
