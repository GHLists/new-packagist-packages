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

## Latest list — 2026-11-02 01:20 UTC

New packages created between 2026-11-02 00:18 UTC and 2026-11-02 01:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-02T01-20-30-36152Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-02 00:28:54 | [anthonyiles/worktree-isolation](https://www.nuget.org/packages/anthonyiles%2Fworktree-isolation) | v0.6.0 |  | Gives every git worktree of a PHP project its own dependencies, env files and d… |
| 2026-11-02 00:33:27 | [trevweb/mymobileworkers-api-client](https://www.nuget.org/packages/trevweb%2Fmymobileworkers-api-client) | v1.0.1 | Trevor | PHP HTTP API client for the MyMobileWorkers API |
| 2026-11-02 00:37:58 | [kitloom/filament-skeleton](https://www.nuget.org/packages/kitloom%2Ffilament-skeleton) | v1.13.0 |  | Grow on Laravel, run it with AI: the kitloom site with the Filament admin edito… |
| 2026-11-02 00:38:04 | [kitloom/nova-skeleton](https://www.nuget.org/packages/kitloom%2Fnova-skeleton) | v1.13.0 |  | Grow on Laravel, run it with AI: the kitloom site with the Laravel Nova admin e… |
| 2026-11-02 00:51:49 | [gitpcl/probe](https://www.nuget.org/packages/gitpcl%2Fprobe) | v0.8.1 |  | Agent-first Laravel testing runtime: warm PHP workers, compact JSON probes, sel… |
| 2026-11-02 01:09:49 | [oliverkroener/ok-cookiebot](https://www.nuget.org/packages/oliverkroener%2Fok-cookiebot) | 3.1.0 | Oliver Kroener | Provides a backend module to manage privacy cookie consent scripts for Cookiebo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
