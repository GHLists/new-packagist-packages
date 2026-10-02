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

## Latest list — 2026-10-02 08:21 UTC

New packages created between 2026-10-02 07:20 UTC and 2026-10-02 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T08-21-13-890824Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 07:21:26 | [nivoin/ship-ready](https://www.nuget.org/packages/nivoin%2Fship-ready) | v1.1.0 | nivoin | Static security, performance, and production-readiness auditor for Laravel 11,… |
| 2026-10-02 07:36:41 | [aldogtz/amadeus-soap](https://www.nuget.org/packages/aldogtz%2Famadeus-soap) | v2.0.0 | Aldo Gutierrez | Laravel wrapper for Amadeus Globalizer SOAP Web Services |
| 2026-10-02 07:39:15 | [ameax/laravel-glitchtip](https://www.nuget.org/packages/ameax%2Flaravel-glitchtip) | v0.1.0 | Michael Schmidt | Error tracking for Laravel with GlitchTip (or any Sentry compatible server): pr… |
| 2026-10-02 08:05:53 | [robyajo/laravel-security-monitor](https://www.nuget.org/packages/robyajo%2Flaravel-security-monitor) | v1.1.0 | Roby | Enterprise-grade headless self-hosted WAF, threat detection engine, zero-tolera… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
