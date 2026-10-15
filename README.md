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

## Latest list — 2026-10-15 16:20 UTC

New packages created between 2026-10-15 15:20 UTC and 2026-10-15 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T16-20-41-931515Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 15:20:47 | [1994/sign-off-statamic](https://www.nuget.org/packages/1994%2Fsign-off-statamic) | v1.2.1 | 1994 | Multi-step editorial sign-off for Statamic Pro: editors submit changes for revi… |
| 2026-10-15 15:22:30 | [evopixel/socialiteproviders-evopixel](https://www.nuget.org/packages/evopixel%2Fsocialiteproviders-evopixel) | 1.0.0 | EvoPixel | EvoPixel Account OAuth2 provider for Laravel Socialite |
| 2026-10-15 15:26:13 | [automattic/jetpack-cookie-consent](https://www.nuget.org/packages/automattic%2Fjetpack-cookie-consent) | v0.1.0 |  | GDPR cookie-consent banner, CCPA opt-out, and consent logging for WordPress. |
| 2026-10-15 15:36:11 | [erseco/autofirma-intermediate-server](https://www.nuget.org/packages/erseco%2Fautofirma-intermediate-server) | v1.9.3 | Ernesto Serrano | Framework-agnostic PHP implementation of the AutoFirma intermediate server prot… |
| 2026-10-15 15:37:37 | [pollora/block-bindings](https://www.nuget.org/packages/pollora%2Fblock-bindings) | v0.1.0 | Amphibee | WordPress Block Bindings declared with attributes: a #[BlockBinding] class is a… |
| 2026-10-15 15:43:14 | [ekumanov/flarum-ext-spam-alerts](https://www.nuget.org/packages/ekumanov%2Fflarum-ext-spam-alerts) | v1.0.0 | ekumanov | Emails chosen moderators whenever FoF Anti-Spam automatically flags or holds a… |
| 2026-10-15 15:55:21 | [pype/framework](https://www.nuget.org/packages/pype%2Fframework) | v0.1.0 |  | The pype core: a lightweight, pipeline-first PHP framework. |
| 2026-10-15 15:55:28 | [pype/pype](https://www.nuget.org/packages/pype%2Fpype) | v0.1.0 |  | Starter application for the pype framework. |
| 2026-10-15 15:57:55 | [watermarkws/watermark-php](https://www.nuget.org/packages/watermarkws%2Fwatermark-php) | v0.1.0 |  | PHP client for the Watermark API: watermark, resize and convert images, videos… |
| 2026-10-15 16:00:39 | [ludoguenet/laravel-standards](https://www.nuget.org/packages/ludoguenet%2Flaravel-standards) | v0.1.0 | Ludovic Guénet | Engineering standards, guidelines and agent skills for Laravel projects, delive… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
