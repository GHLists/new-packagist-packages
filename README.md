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

## Latest list — 2026-10-20 07:20 UTC

New packages created between 2026-10-20 06:20 UTC and 2026-10-20 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-20T07-20-53-242879Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-20 07:04:15 | [billsensei/moodle-mod_peerreview](https://www.nuget.org/packages/billsensei%2Fmoodle-mod_peerreview) | v0.19.9 |  | Peer review activity for Moodle: students assess each other with scores, scales… |
| 2026-10-20 07:10:54 | [roundly-consulting/events-for-laravel](https://www.nuget.org/packages/roundly-consulting%2Fevents-for-laravel) | 1.0.0 | Andrej Mihaliak | Real-world events for any Eloquent app: reusable venues with near-me search, ti… |
| 2026-10-20 07:16:15 | [wishbox/russian-post-client](https://www.nuget.org/packages/wishbox%2Frussian-post-client) | v0.1.1 | Nekrasov Vitaliy | Extensible PHP client for the Russian Post Otpravka API. |
| 2026-10-20 07:16:29 | [kybdev/lara-ai-assistant](https://www.nuget.org/packages/kybdev%2Flara-ai-assistant) | v0.1.1 | Package Author | A reusable Laravel AI Assistant package for model discovery, authorized data re… |
| 2026-10-20 07:16:53 | [wexample/symfony-platform-ds](https://www.nuget.org/packages/wexample%2Fsymfony-platform-ds) | 1.0.1 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
