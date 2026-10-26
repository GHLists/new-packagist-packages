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

## Latest list — 2026-10-26 21:21 UTC

New packages created between 2026-10-26 20:22 UTC and 2026-10-26 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T21-21-07-075003Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 20:26:07 | [iswilson/canadapost-api](https://www.nuget.org/packages/iswilson%2Fcanadapost-api) | v0.3.0 | Ian Wilson; Jace Bennest | Unofficial PHP library for communicating with Canada Post APIs. |
| 2026-10-26 20:32:38 | [tryhackx/flarum-homepage-blocks](https://www.nuget.org/packages/tryhackx%2Fflarum-homepage-blocks) | 2.10.0 | TryHackX | Customizable homepage blocks for tracker-style Flarum forums featuring dual sta… |
| 2026-10-26 20:52:55 | [wilycode/recaptcha-validator](https://www.nuget.org/packages/wilycode%2Frecaptcha-validator) | v0.1.0 | Simon Piter | Google reCAPTCHA v3 verification and a reusable WilyCode validator. |
| 2026-10-26 20:54:04 | [watchdiff-labs/watchdiff-laravel](https://www.nuget.org/packages/watchdiff-labs%2Fwatchdiff-laravel) | v0.1.0 |  | Laravel service provider for watchdiff-core - web change monitoring with Artisa… |
| 2026-10-26 20:59:37 | [lucacermenati/common-traits](https://www.nuget.org/packages/lucacermenati%2Fcommon-traits) | v0.1.1 | Luca Cermenati | Reusable traits and interfaces for Laravel applications. |
| 2026-10-26 21:03:11 | [lucacermenati/nova-global-filters](https://www.nuget.org/packages/lucacermenati%2Fnova-global-filters) | v1.0.0 | Luca Cermenati | Session-backed global filters for Laravel Nova 5 dashboards: define filters in… |
| 2026-10-26 21:06:49 | [steddle/vcrs](https://www.nuget.org/packages/steddle%2Fvcrs) | v0.1.0-beta.4 |  | The Verified Claimant Register Standard: the text, the annexes, the schemas, th… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
