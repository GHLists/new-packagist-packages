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

## Latest list — 2026-10-08 17:22 UTC

New packages created between 2026-10-08 16:19 UTC and 2026-10-08 17:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T17-22-06-985442Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 16:22:53 | [lindor03/project-memory](https://www.nuget.org/packages/lindor03%2Fproject-memory) | 1.3.0 |  | Local-first project memory and code intelligence for Laravel applications. |
| 2026-10-08 16:25:48 | [arnipay/sdk-php](https://www.nuget.org/packages/arnipay%2Fsdk-php) | 1.6.1 |  | SDK for integrating with the Arnipay payment processing system |
| 2026-10-08 16:25:48 | [geekwalletsrl/arnipay-sdk](https://www.nuget.org/packages/geekwalletsrl%2Farnipay-sdk) | 1.6.1 |  | SDK for integrating with the Arnipay payment processing system |
| 2026-10-08 16:30:48 | [tsi/rtly-kit](https://www.nuget.org/packages/tsi%2Frtly-kit) | v0.1.1 | Ehsan Enaloo | RTLY-Kit: the definitive RTL kit for PHP — Jalali, Hijri, Hebrew calendars, Ira… |
| 2026-10-08 16:37:45 | [dasformt/kirby-consent](https://www.nuget.org/packages/dasformt%2Fkirby-consent) | v1.0.1 | dasformt | Einwilligung mit Platzhalter für externe Dienste in Kirby |
| 2026-10-08 16:37:45 | [dasformt/kirby-favicons](https://www.nuget.org/packages/dasformt%2Fkirby-favicons) | v1.0.0 | dasformt | Favicons, Apple Touch Icon und Webmanifest aus dem Kirby-Panel |
| 2026-10-08 16:42:16 | [crawlora/bbb](https://www.nuget.org/packages/crawlora%2Fbbb) | v0.1.0 |  | Better Business Bureau client for the Crawlora hosted API |
| 2026-10-08 16:52:17 | [janalis/custos](https://www.nuget.org/packages/janalis%2Fcustos) | v0.1.0 |  | Fast PHP inspector and fixer (178 inspections with quick-fixes), shipped as a p… |
| 2026-10-08 17:00:32 | [wexample/symfony-notification](https://www.nuget.org/packages/wexample%2Fsymfony-notification) | 1.0.1 |  |  |
| 2026-10-08 17:00:59 | [wexample/symfony-notification-ds](https://www.nuget.org/packages/wexample%2Fsymfony-notification-ds) | 1.0.1 |  |  |
| 2026-10-08 17:01:25 | [wexample/symfony-notification-demo](https://www.nuget.org/packages/wexample%2Fsymfony-notification-demo) | 1.0.1 |  |  |
| 2026-10-08 17:01:51 | [wexample/symfony-signature](https://www.nuget.org/packages/wexample%2Fsymfony-signature) | 1.0.1 |  |  |
| 2026-10-08 17:02:16 | [wexample/symfony-signature-ds](https://www.nuget.org/packages/wexample%2Fsymfony-signature-ds) | 1.0.1 |  |  |
| 2026-10-08 17:02:42 | [wexample/symfony-signature-demo](https://www.nuget.org/packages/wexample%2Fsymfony-signature-demo) | 1.0.1 |  |  |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
