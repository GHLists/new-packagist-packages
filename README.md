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

## Latest list — 2026-11-24 12:21 UTC

New packages created between 2026-11-24 11:18 UTC and 2026-11-24 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T12-21-50-286871Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 11:25:26 | [lexflame/intelfield](https://www.nuget.org/packages/lexflame%2Fintelfield) | v0.1.0 |  | Browser form controls: jQuery fields, date/time pickers, buttons and AJAX conne… |
| 2026-11-24 11:29:59 | [opencultureconsulting/updater](https://www.nuget.org/packages/opencultureconsulting%2Fupdater) | v1.0.0 | Open Culture Consulting; Seba… | A self-update command for Composer-based applications. |
| 2026-11-24 11:31:22 | [serversmtp/serversmtp-laravel](https://www.nuget.org/packages/serversmtp%2Fserversmtp-laravel) | v0.1.0 | Think AI SRL | ServerSMTP mail transport and automation events for Laravel |
| 2026-11-24 11:51:27 | [jellyhaus/vite](https://www.nuget.org/packages/jellyhaus%2Fvite) | 2026.11.3 | Jason Millis | Vite Integration for Vanilla PHP Projects |
| 2026-11-24 11:58:00 | [jeffersongoncalves/laravel-scanner-guard-haproxy](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-scanner-guard-haproxy) | 1.0.0 | Jefferson Gonçalves | HAProxy denylist sink for laravel-scanner-guard: writes banned IPs as an ACL fi… |
| 2026-11-24 11:58:15 | [jeffersongoncalves/laravel-scanner-guard-aws-waf](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-scanner-guard-aws-waf) | 1.0.0 | Jefferson Gonçalves | AWS WAF denylist sink for laravel-scanner-guard: keeps IP sets in sync so a web… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
