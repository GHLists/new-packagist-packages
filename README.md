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

## Latest list — 2026-11-26 15:20 UTC

New packages created between 2026-11-26 14:20 UTC and 2026-11-26 15:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T15-20-20-474342Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 14:30:18 | [sightpress/module-template](https://www.nuget.org/packages/sightpress%2Fmodule-template) | 0.1.0 |  | A starting point for a SightPress module: SightPress is a powerful CMS for ever… |
| 2026-11-26 14:37:27 | [vivomedia/neos-notfound](https://www.nuget.org/packages/vivomedia%2Fneos-notfound) | 1.0.0 |  | Neos CMS package that renders a normal editable page for 404 errors, aware of c… |
| 2026-11-26 14:48:20 | [goodport/laravel-ai-resilience](https://www.nuget.org/packages/goodport%2Flaravel-ai-resilience) | v1.0.0 | goodport | Rate limiting and retries for Laravel AI agent prompts. |
| 2026-11-26 14:51:58 | [mirror-and-mountain/meros-portal](https://www.nuget.org/packages/mirror-and-mountain%2Fmeros-portal) | v1.0.0 | tmw-mm | Customer Portals for Meros-powered WordPress sites. |
| 2026-11-26 15:07:15 | [dynamikasolucoesweb/laravel-captcha](https://www.nuget.org/packages/dynamikasolucoesweb%2Flaravel-captcha) | v1.0.0 | Dynamika Soluções Web | One captcha API for Laravel: Cloudflare Turnstile, hCaptcha and Google reCAPTCH… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
