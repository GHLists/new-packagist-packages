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

## Latest list — 2026-10-14 08:19 UTC

New packages created between 2026-10-14 07:20 UTC and 2026-10-14 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T08-19-24-55369Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 07:20:58 | [iptrust/sdk](https://www.nuget.org/packages/iptrust%2Fsdk) | v0.1.0 | IP Trust | Official PHP SDK for the IP Trust API: IP geolocation, ASN, company, hosting, b… |
| 2026-10-14 07:29:11 | [software-technologies-limited/sms](https://www.nuget.org/packages/software-technologies-limited%2Fsms) | v0.0.3 | James Kabz | Laravel package for integrating sms notifications |
| 2026-10-14 07:38:33 | [websign-dev/sillbeam](https://www.nuget.org/packages/websign-dev%2Fsillbeam) | v0.1.0 |  | Modular architecture extension for Symfony applications, organized around Modul… |
| 2026-10-14 07:39:21 | [welcomattic/messenger-central](https://www.nuget.org/packages/welcomattic%2Fmessenger-central) | v0.1.0 | Mathieu Santostefano | A terminal UI to drive Symfony Messenger workers during development |
| 2026-10-14 07:53:14 | [novwyatt/laravel-login-guard](https://www.nuget.org/packages/novwyatt%2Flaravel-login-guard) | v0.1.0 | NovWyatt | Brute-force login protection for Laravel: progressive lockouts per IP and usern… |
| 2026-10-14 07:57:07 | [sendkuy/sdk](https://www.nuget.org/packages/sendkuy%2Fsdk) | v1.0.0 |  | PHP SDK for the SendKuy API: send WhatsApp, SMS and email from your own code. |
| 2026-10-14 07:57:11 | [sabroan/psr-15](https://www.nuget.org/packages/sabroan%2Fpsr-15) | 1.0.0 |  | A lightweight PSR-15 server handler |
| 2026-10-14 08:03:00 | [sendkuy/laravel](https://www.nuget.org/packages/sendkuy%2Flaravel) | v1.0.0 |  | SendKuy for Laravel: WhatsApp, SMS and email notifications, a facade, and signe… |
| 2026-10-14 08:07:24 | [sabroan/http-emitter-interface](https://www.nuget.org/packages/sabroan%2Fhttp-emitter-interface) | 1.0.0 |  | A PHP interface for emitting PSR-7 HTTP responses |
| 2026-10-14 08:07:36 | [ciphera/craft-pulse-analytics](https://www.nuget.org/packages/ciphera%2Fcraft-pulse-analytics) | v1.0.0 | Ciphera | Privacy-first web analytics for Craft CMS. No cookies, no personal data, and th… |
| 2026-10-14 08:16:07 | [rewi.sh/craft-mcp](https://www.nuget.org/packages/rewi.sh%2Fcraft-mcp) | 1.0.0 | rewi.sh | MCP - All in one. An MCP server for Craft CMS with content tools and a control… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
