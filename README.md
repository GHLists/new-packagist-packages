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

## Latest list — 2026-11-18 02:22 UTC

New packages created between 2026-11-18 01:20 UTC and 2026-11-18 02:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T02-22-05-572979Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 01:23:55 | [jeffersongoncalves/filament-us-privacy](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-us-privacy) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-us-privacy: the personal data inventory and the rul… |
| 2026-11-18 01:25:39 | [jeffersongoncalves/filament-us-privacy-opt-out](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-us-privacy-opt-out) | 2.0.0 |  |  |
| 2026-11-18 01:27:16 | [jeffersongoncalves/filament-us-privacy-requests](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-us-privacy-requests) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-us-privacy-requests: consumer requests under the US… |
| 2026-11-18 01:28:48 | [jeffersongoncalves/filament-us-privacy-notices](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-us-privacy-notices) | 2.0.0 |  |  |
| 2026-11-18 01:30:24 | [jeffersongoncalves/filament-us-privacy-assessments](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-us-privacy-assessments) | 2.0.0 |  |  |
| 2026-11-18 01:31:57 | [jeffersongoncalves/filament-us-privacy-vendors](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-us-privacy-vendors) | 2.0.0 |  |  |
| 2026-11-18 01:33:31 | [jeffersongoncalves/filament-us-privacy-minors](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-us-privacy-minors) | 3.0.0 | Jefferson Gonçalves | Filament plugin for laravel-us-privacy-minors: age checks, parent or guardian l… |
| 2026-11-18 01:45:23 | [jeffersongoncalves/laravel-quebec](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-quebec) | 1.0.0 | Jefferson Gonçalves | Quebec Law 25 (private sector privacy act) for Laravel: a personal information… |
| 2026-11-18 01:56:57 | [jeffersongoncalves/laravel-quebec-retention](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-quebec-retention) | 1.0.0 | Jefferson Gonçalves | Retention for Quebec Law 25: destroy or anonymize personal information once its… |
| 2026-11-18 01:57:26 | [jeffersongoncalves/laravel-quebec-audit-log](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-quebec-audit-log) | 1.0.0 | Jefferson Gonçalves | Audit log for Quebec Law 25: who viewed, changed, exported or deleted whose per… |
| 2026-11-18 01:57:59 | [jeffersongoncalves/laravel-quebec-consent](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-quebec-consent) | 1.0.0 | Jefferson Gonçalves | Consent for Quebec Law 25: a manifest, free and enlightened consent per specifi… |
| 2026-11-18 01:58:40 | [atellitech/mcp-hyperf](https://www.nuget.org/packages/atellitech%2Fmcp-hyperf) | v1.0.0 |  | Streamable HTTP MCP server (tools, prompts and resources) that plugs into an ex… |
| 2026-11-18 02:00:26 | [hhr0815hhr/tsf](https://www.nuget.org/packages/hhr0815hhr%2Ftsf) | 0.7.0 |  | TSF — TypePHP Server Framework：用 TypePHP(AOT) + PHP 构建高性能游戏服务器 |
| 2026-11-18 02:14:33 | [usmrip/turnstile-waiting](https://www.nuget.org/packages/usmrip%2Fturnstile-waiting) | v1.0.0 | usmrip | Universal Cloudflare Turnstile & Waiting Ticker module for HTML, PHP, JavaScrip… |
| 2026-11-18 02:15:39 | [artisan-toolbox/dapter](https://www.nuget.org/packages/artisan-toolbox%2Fdapter) | 1.0.0-alpha.1 | Allan Mariucci Carvalho | Data adapter foundations for Laravel and Inertia applications. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
