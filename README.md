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

## Latest list — 2026-11-17 16:20 UTC

New packages created between 2026-11-17 15:21 UTC and 2026-11-17 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T16-20-47-440547Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 15:22:29 | [spyck/automation-bundle](https://www.nuget.org/packages/spyck%2Fautomation-bundle) | 1.0.0 | Willem Verspyck | Automation Bundle for Symfony |
| 2026-11-17 15:31:00 | [tornado-engine/github](https://www.nuget.org/packages/tornado-engine%2Fgithub) | v0.1.2 |  | Tornado Engine module: connect a GitHub account, and publish modules to GitHub… |
| 2026-11-17 15:33:03 | [youvision/think-enum](https://www.nuget.org/packages/youvision%2Fthink-enum) | v1.0 | youvision | 基于 ThinkPHP 8 的枚举增强工具，更方便地在项目中定义并使用枚举 |
| 2026-11-17 15:37:27 | [wonder-image/rsvp](https://www.nuget.org/packages/wonder-image%2Frsvp) | v2.1.0 |  | RSVP plugin for wonder-image/new-site projects. |
| 2026-11-17 15:51:05 | [darvis/laravel-mfa](https://www.nuget.org/packages/darvis%2Flaravel-mfa) | v1.1.0 | Arvid de Jong | Login that survives an outage: two factor authentication (2FA), magic link, ema… |
| 2026-11-17 15:52:25 | [drupal-security/scanner](https://www.nuget.org/packages/drupal-security%2Fscanner) | 1.0.0 | Mayank Gupta | Psalm taint-analysis security scanner for Drupal — finds XSS, SQL injection, RC… |
| 2026-11-17 15:52:50 | [upassist/neos-ui-thememode](https://www.nuget.org/packages/upassist%2Fneos-ui-thememode) | v1.0.0 |  | Light, dark and auto theme mode for the Neos CMS backend (content UI and backen… |
| 2026-11-17 15:54:37 | [brandcom/silverstripe-userforms-submission-cleanup](https://www.nuget.org/packages/brandcom%2Fsilverstripe-userforms-submission-cleanup) | v1.0.1 | brandcom | Deletes Silverstripe userforms submissions older than a retention window, inclu… |
| 2026-11-17 15:56:29 | [jeffersongoncalves/laravel-ccpa](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-ccpa) | 1.0.0 | Jefferson Gonçalves | CCPA/CPRA toolkit core for Laravel: declare personal information on Eloquent mo… |
| 2026-11-17 15:58:37 | [happenv-com/filament-search](https://www.nuget.org/packages/happenv-com%2Ffilament-search) | v0.1.0 | Happenv sp. z o.o.; webard | A Cmd+K palette for Filament panels that renders results from pluggable sources. |
| 2026-11-17 16:05:34 | [jeffersongoncalves/laravel-ccpa-opt-out](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-ccpa-opt-out) | 1.0.0 | Jefferson Gonçalves | CCPA/CPRA opt-out ledger for Laravel: Do Not Sell or Share (§1798.120) and Limi… |
| 2026-11-17 16:14:18 | [rusender/rusender-php](https://www.nuget.org/packages/rusender%2Frusender-php) | v0.1.0 | RuSender | Official PHP SDK for the RuSender public API |
| 2026-11-17 16:15:07 | [jeffersongoncalves/laravel-ccpa-requests](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-ccpa-requests) | 1.0.0 | Jefferson Gonçalves | CCPA/CPRA consumer requests for Laravel: right to know, delete and correct, ver… |
| 2026-11-17 16:15:49 | [jeffersongoncalves/laravel-ccpa-retention](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-ccpa-retention) | 1.0.0 | Jefferson Gonçalves | CCPA/CPRA retention for Laravel (§1798.100(a)(3)): deidentify personal informat… |
| 2026-11-17 16:16:22 | [jeffersongoncalves/laravel-ccpa-audit-log](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-ccpa-audit-log) | 1.0.0 | Jefferson Gonçalves | CCPA/CPRA audit log for Laravel: tamper-evident, hash-chained record of who vie… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
