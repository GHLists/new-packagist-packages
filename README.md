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

## Latest list — 2026-10-28 16:21 UTC

New packages created between 2026-10-28 15:19 UTC and 2026-10-28 16:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T16-21-15-47708Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 15:29:17 | [tpetry/laravel-multi-region](https://www.nuget.org/packages/tpetry%2Flaravel-multi-region) | 1.0.0 | tpetry | Middleware to create multi-region applications with read-after-write consistency |
| 2026-10-28 15:35:01 | [a2ztools/api](https://www.nuget.org/packages/a2ztools%2Fapi) | v1.0.0 | A2Z Tools | Free API client for website checks: SSL certificate expiry, DNS, WHOIS (RDAP),… |
| 2026-10-28 15:42:04 | [ghispi/tree-transform](https://www.nuget.org/packages/ghispi%2Ftree-transform) | v0.1.0 | ghispi | Efficient, streaming filtering and transformation of trees (nested set, adjacen… |
| 2026-10-28 15:44:16 | [pushinbr/pam-native-contacts](https://www.nuget.org/packages/pushinbr%2Fpam-native-contacts) | v0.1.0 |  | Device contacts and the SMS composer for PAM Native: paged contact reads, the n… |
| 2026-10-28 15:44:16 | [pushinbr/pam-native-location](https://www.nuget.org/packages/pushinbr%2Fpam-native-location) | v0.1.0 |  | Device location for PAM Native: current and last known position, watches, and t… |
| 2026-10-28 15:44:16 | [pushinbr/pam-native-sensors](https://www.nuget.org/packages/pushinbr%2Fpam-native-sensors) | v0.1.0 |  | Motion sensors for PAM Native: one-shot reads and throttled watches of the acce… |
| 2026-10-28 15:48:54 | [cloakwp/media-offload](https://www.nuget.org/packages/cloakwp%2Fmedia-offload) | v0.1.0-beta.1 |  | Store WordPress attachments in S3-compatible object storage. |
| 2026-10-28 15:50:40 | [shaarifsabah/laravel-watchman](https://www.nuget.org/packages/shaarifsabah%2Flaravel-watchman) | v1.0.0 |  | Sanctions screening for Laravel: a native PHP port of Moov Watchman (OFAC, CSL,… |
| 2026-10-28 15:52:19 | [makallio85/rocksoftware-cakephp-db-sanitizer](https://www.nuget.org/packages/makallio85%2Frocksoftware-cakephp-db-sanitizer) | v1.0.0 |  | CakePHP 5 plugin that masks a copy of a production database: per-column rules w… |
| 2026-10-28 15:52:36 | [hnraytek/flame-tp](https://www.nuget.org/packages/hnraytek%2Fflame-tp) | v1.0.0 | haoshuaioo | Flame TP skeleton. Install modules to grow your app. |
| 2026-10-28 16:05:13 | [ilbronza/media-manager](https://www.nuget.org/packages/ilbronza%2Fmedia-manager) | v0.1.0 | Davide Bronzini | Filesystem-backed Laravel media catalogue with stable identities and reconcilia… |
| 2026-10-28 16:16:14 | [josbeir/cakephp-interact](https://www.nuget.org/packages/josbeir%2Fcakephp-interact) | 0.1.0 |  | Reactive server-rendered PHP islands for CakePHP. |
| 2026-10-28 16:19:34 | [artisan-build/bonfire](https://www.nuget.org/packages/artisan-build%2Fbonfire) | 0.2.0 |  | A chat package inspired by Campfire from 37 Signals |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
