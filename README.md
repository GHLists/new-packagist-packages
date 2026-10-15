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

## Latest list — 2026-10-15 08:21 UTC

New packages created between 2026-10-15 07:21 UTC and 2026-10-15 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T08-21-23-82043Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 07:34:19 | [phatnt93/phalcon-validation](https://www.nuget.org/packages/phatnt93%2Fphalcon-validation) | v1.0.1 | Phat Nguyen | A fast, extensible and expressive PHP data validation and sanitization library… |
| 2026-10-15 07:35:01 | [enaxon/reqtide-guzzle](https://www.nuget.org/packages/enaxon%2Freqtide-guzzle) | v0.1.0 | Ehsan Enaloo | Guzzle integration for Reqtide: retries, deadlines, rate limits, circuit breaki… |
| 2026-10-15 07:35:01 | [enaxon/reqtide-redis](https://www.nuget.org/packages/enaxon%2Freqtide-redis) | v0.1.0 | Ehsan Enaloo | Redis state backends for Reqtide: shared rate limits, circuit breakers, bulkhea… |
| 2026-10-15 07:41:18 | [webx-ui/module-tasks](https://www.nuget.org/packages/webx-ui%2Fmodule-tasks) | v0.73.0 | WebX UI | A queue of work between people and AI agents for the WebX UI admin panel: tasks… |
| 2026-10-15 07:46:24 | [pteal79/wysiwyg-editor](https://www.nuget.org/packages/pteal79%2Fwysiwyg-editor) | 1.0.2 | vipertecpro; Peter Teal | A fully native, hand-written WYSIWYG rich text editor for NativePHP Mobile — wr… |
| 2026-10-15 07:49:41 | [pieceofcake2/phpcs-cakephp2](https://www.nuget.org/packages/pieceofcake2%2Fphpcs-cakephp2) | v1.0.0 |  | PHP_CodeSniffer ruleset for CakePHP 2 applications and plugins, based on the Ca… |
| 2026-10-15 08:01:40 | [reachweb/statamic-tolk](https://www.nuget.org/packages/reachweb%2Fstatamic-tolk) | v1.0.0 | Iosif Chatzimichail | Translate multi-site Statamic content into its localizations with large languag… |
| 2026-10-15 08:06:56 | [adems/dapur](https://www.nuget.org/packages/adems%2Fdapur) | 0.1.0 |  | Dapur AdeMS, tempat Ade M Saragih untuk bermain dan belajar membuat website |
| 2026-10-15 08:09:25 | [fallahalireza/laravel-kavenegar](https://www.nuget.org/packages/fallahalireza%2Flaravel-kavenegar) | v0.1.0 | Alireza Fallah | درایور تمیز، توسعه‌پذیر و تست‌پذیر ارسال پیامک کاوه‌نگار برای لاراول (Notificat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
