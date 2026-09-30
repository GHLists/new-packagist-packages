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

## Latest list — 2026-09-30 22:21 UTC

New packages created between 2026-09-30 21:21 UTC and 2026-09-30 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-30T22-21-02-856972Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-30 21:21:47 | [mambusrl/bper-avvisi-pagopa](https://www.nuget.org/packages/mambusrl%2Fbper-avvisi-pagopa) | v1.0.0 |  | Client PHP per il WS IUVOnline 1.4 di BPER Banca / BPS: generazione, variazione… |
| 2026-09-30 21:28:18 | [webdna/typesense-sync](https://www.nuget.org/packages/webdna%2Ftypesense-sync) | 1.0.0-beta.1 | webdna | Keep Craft content in a Typesense search index, and give search pages a safe, f… |
| 2026-09-30 21:32:12 | [siberfx/laravel-mutex-lock](https://www.nuget.org/packages/siberfx%2Flaravel-mutex-lock) | 1.0.1 | Selim Görmüş | Laravel integration for php-lock/lock: database-backed mutexes for MySQL/MariaD… |
| 2026-09-30 21:44:43 | [laraxgram/sentinel](https://www.nuget.org/packages/laraxgram%2Fsentinel) | v1.0.0 | laraXgram | Watch over your LaraGram bot: updates, webhooks, Telegram API calls, exceptions… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
