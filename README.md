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

## Latest list — 2026-11-19 10:21 UTC

New packages created between 2026-11-19 09:20 UTC and 2026-11-19 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T10-21-37-38035Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 09:29:32 | [yu-laravel/dns-check](https://www.nuget.org/packages/yu-laravel%2Fdns-check) | v1.0.0 | Yuriy Akishin | Laravel Livewire tool that checks a domain's DNS and mail records: nameservers,… |
| 2026-11-19 09:29:32 | [yu-laravel/link-preview](https://www.nuget.org/packages/yu-laravel%2Flink-preview) | v1.0.0 | Yuriy Akishin | Laravel Livewire tool that shows how a link looks when shared in messengers and… |
| 2026-11-19 09:29:32 | [yu-laravel/page-speed](https://www.nuget.org/packages/yu-laravel%2Fpage-speed) | v1.0.0 | Yuriy Akishin | Laravel Livewire tool that checks page speed and Core Web Vitals through the Go… |
| 2026-11-19 09:29:32 | [yu-laravel/schema-validator](https://www.nuget.org/packages/yu-laravel%2Fschema-validator) | v1.0.0 | Yuriy Akishin | Laravel Livewire tool that validates Schema.org structured data (JSON-LD and mi… |
| 2026-11-19 09:29:32 | [yu-laravel/security-check](https://www.nuget.org/packages/yu-laravel%2Fsecurity-check) | v1.0.0 | Yuriy Akishin | Laravel Livewire tool that checks a site's SSL certificate, HTTPS redirect and… |
| 2026-11-19 09:29:32 | [yu-laravel/seo-meta-analyzer](https://www.nuget.org/packages/yu-laravel%2Fseo-meta-analyzer) | v1.0.0 | Yuriy Akishin | Laravel Livewire tool that checks a page's title, description and other meta ta… |
| 2026-11-19 09:29:32 | [yu-laravel/web-tools-core](https://www.nuget.org/packages/yu-laravel%2Fweb-tools-core) | v1.0.0 | Yuriy Akishin | Shared core for the yu-laravel web tools: SSRF-safe page fetcher, TLS inspector… |
| 2026-11-19 09:29:32 | [yu-laravel/webmcp-analyzer](https://www.nuget.org/packages/yu-laravel%2Fwebmcp-analyzer) | v1.0.0 | Yuriy Akishin | Laravel Livewire tool that checks how a page exposes WebMCP tools to AI agents. |
| 2026-11-19 10:03:27 | [ikongdev/font-awesome](https://www.nuget.org/packages/ikongdev%2Ffont-awesome) | v1.1.0 | Jericho Umayam | Using FontAwesome Enum in Filament |
| 2026-11-19 10:10:43 | [fedor/work-orchestrator](https://www.nuget.org/packages/fedor%2Fwork-orchestrator) | v0.4.0 |  | Finite concurrent and parallel work orchestration with managed subprocess lifec… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
