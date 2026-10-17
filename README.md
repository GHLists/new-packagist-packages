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

## Latest list — 2026-10-17 20:21 UTC

New packages created between 2026-10-17 19:18 UTC and 2026-10-17 20:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T20-21-49-795644Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 19:32:25 | [saurabhg/module-preorder](https://www.nuget.org/packages/saurabhg%2Fmodule-preorder) | 1.0.0 |  | Pre-order / backorder for out-of-stock and upcoming products (Luma + Hyva ready… |
| 2026-10-17 19:37:13 | [tigger/tigger](https://www.nuget.org/packages/tigger%2Ftigger) | v1.0.0 |  | A tiny, Express.js-inspired micro-framework for PHP 8.3+ with zero dependencies. |
| 2026-10-17 19:42:58 | [mertbag96/laravel-domain-migrator](https://www.nuget.org/packages/mertbag96%2Flaravel-domain-migrator) | v0.2.0 | Mert Bağ | Analyze, migrate and enforce domain boundaries in Laravel MVC apps. |
| 2026-10-17 19:44:46 | [arronrees/content-governance](https://www.nuget.org/packages/arronrees%2Fcontent-governance) | v1.0.1 | Arron Rees | Track review and expiry of Statamic entries: owners, attestations and reminders. |
| 2026-10-17 19:51:35 | [pieceofcake2/image](https://www.nuget.org/packages/pieceofcake2%2Fimage) | v1.0.0 |  | CakePHP 2 plugin that validates uploaded images by their contents: JPEG, PNG, G… |
| 2026-10-17 19:59:38 | [roundly-consulting/tickets-for-laravel](https://www.nuget.org/packages/roundly-consulting%2Ftickets-for-laravel) | 1.0.0 | Andrej Mihaliak | Headless helpdesk ticketing core: categories, swappable statuses, replies and i… |
| 2026-10-17 20:00:36 | [filagora/filagora-push](https://www.nuget.org/packages/filagora%2Ffilagora-push) | v0.1.0 |  | Web push for Filagora: browser subscriptions with the safety checks, stale clea… |
| 2026-10-17 20:16:28 | [pieceofcake2/security-sca](https://www.nuget.org/packages/pieceofcake2%2Fsecurity-sca) | v1.0.0 |  | Software composition analysis of an application: the known vulnerabilities of i… |
| 2026-10-17 20:16:43 | [pieceofcake2/security-sast](https://www.nuget.org/packages/pieceofcake2%2Fsecurity-sast) | v1.0.0 |  | Static application security testing of a CakePHP 2 application with Semgrep or… |
| 2026-10-17 20:16:57 | [pieceofcake2/security-dast](https://www.nuget.org/packages/pieceofcake2%2Fsecurity-dast) | v1.0.0 |  | Dynamic application security testing of a running CakePHP 2 application with th… |
| 2026-10-17 20:18:02 | [stefanak-michal/grafeo-php](https://www.nuget.org/packages/stefanak-michal%2Fgrafeo-php) | v1.0.0 | Michal Stefanak | FFI implementation to run Grafeo embedded in PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
