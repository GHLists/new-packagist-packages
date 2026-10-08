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

## Latest list — 2026-10-08 16:19 UTC

New packages created between 2026-10-08 15:21 UTC and 2026-10-08 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T16-19-51-338225Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 15:32:18 | [bahricanli/eyazisma](https://www.nuget.org/packages/bahricanli%2Feyazisma) | v0.1.0 | Bahri Meriç Canlı | e-Yazışma Paketi (EYP 2.x) oluşturma, okuma ve doğrulama; Laravel desteğiyle |
| 2026-10-08 15:38:08 | [anjan-talukdar/laravel-api-mail](https://www.nuget.org/packages/anjan-talukdar%2Flaravel-api-mail) | v1.0.0 | Anjan Talukdar | Multi-provider HTTP API Mail driver and fluent message builder for Laravel (Hos… |
| 2026-10-08 15:40:19 | [vipertecpro/pausewall-usage](https://www.nuget.org/packages/vipertecpro%2Fpausewall-usage) | v1.0.0 | Vipul Walia (vipertecpro) | Read-only app usage for NativePHP: how long each app was used today or over the… |
| 2026-10-08 15:50:18 | [amphibee/meiliscout](https://www.nuget.org/packages/amphibee%2Fmeiliscout) | 2.0.0 | AmphiBee | Intégration de Meilisearch dans WordPress avec une approche modulaire et expres… |
| 2026-10-08 16:08:13 | [goletter/hyperf-card](https://www.nuget.org/packages/goletter%2Fhyperf-card) | v1.0.0 | goletter | Hyperf 多平台发卡 SDK（Airwallex / Slash / Lampay / Photonpay / Wasabi），含 Factory、Bun… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
