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

## Latest list — 2026-09-29 10:20 UTC

New packages created between 2026-09-29 09:21 UTC and 2026-09-29 10:20 UTC.

[Full CSV](data/new-packagist-packages-2026-09-29T10-20-14-958617Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-29 09:46:48 | [adimiuprix/coinmarketcap](https://www.nuget.org/packages/adimiuprix%2Fcoinmarketcap) | 1.0.0 | Igor Sazonov | CoinMarketCap API Client for Laravel |
| 2026-09-29 09:56:05 | [smtping/mautic-email-verifier](https://www.nuget.org/packages/smtping%2Fmautic-email-verifier) | v1.0.0 | SMTPing | SMTPing Email Verifier for Mautic: verify contacts, block risky addresses on fo… |
| 2026-09-29 10:14:21 | [shibuj/laravel-ai-chat-assistant](https://www.nuget.org/packages/shibuj%2Flaravel-ai-chat-assistant) | v0.1.0 | Shibu J | A BotMan-powered, tool-calling AI chat widget for Laravel with a swappable AI d… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
