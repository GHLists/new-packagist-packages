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

## Latest list — 2026-10-30 21:21 UTC

New packages created between 2026-10-30 20:22 UTC and 2026-10-30 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T21-21-10-687232Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 20:44:26 | [ramon/tag-experts](https://www.nuget.org/packages/ramon%2Ftag-experts) | v0.0.1 | Ramon Guilherme | Recognise members as experts in tags: endorsements, review, and highlighted exp… |
| 2026-10-30 20:44:47 | [ramon/saved-searches](https://www.nuget.org/packages/ramon%2Fsaved-searches) | v0.0.1 | Ramon Guilherme | Save a search and get notified when new discussions or replies match it. |
| 2026-10-30 21:02:00 | [hryvinskyi/magento2-bot-verification-pack](https://www.nuget.org/packages/hryvinskyi%2Fmagento2-bot-verification-pack) | 1.0.0 | Volodymyr Hryvinskyi | Bot Verification for Magento 2 with the Google and Bing crawlers: catches reque… |
| 2026-10-30 21:03:13 | [ramon/composer](https://www.nuget.org/packages/ramon%2Fcomposer) | v0.0.1 | Ramon Guilherme | Side-by-side live preview in the Flarum 2 composer. |
| 2026-10-30 21:09:06 | [tualo/oauth2](https://www.nuget.org/packages/tualo%2Foauth2) | 0.1.1 |  | OAuth 2.0 and OpenID Connect authorization server for Tualo Office |
| 2026-10-30 21:11:00 | [filippotoso/driver-vonage-whatsapp](https://www.nuget.org/packages/filippotoso%2Fdriver-vonage-whatsapp) | v1.0.2 | Filippo Toso | Vonage WhatsApp driver for BotMan |
| 2026-10-30 21:14:16 | [darvis/laravel-uploads](https://www.nuget.org/packages/darvis%2Flaravel-uploads) | v1.0.0 | Arvid de Jong | One Upload model for every file in a Laravel app: attach files to any model in… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
