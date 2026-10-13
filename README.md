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

## Latest list — 2026-10-13 08:21 UTC

New packages created between 2026-10-13 07:20 UTC and 2026-10-13 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-13T08-21-39-716847Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-13 07:23:20 | [zeimoto/compute](https://www.nuget.org/packages/zeimoto%2Fcompute) | v0.1.0 | zeimoto | Model-bound metadata, identity, indexing, and PWA resolution. |
| 2026-10-13 07:27:03 | [zeimoto/contact](https://www.nuget.org/packages/zeimoto%2Fcontact) | v0.1.0 | zeimoto | Contact form rendering, submission validation, and email delivery. |
| 2026-10-13 07:30:10 | [wexample/symfony-workspace](https://www.nuget.org/packages/wexample%2Fsymfony-workspace) | 1.0.1 |  |  |
| 2026-10-13 07:31:09 | [zeimoto/panel](https://www.nuget.org/packages/zeimoto%2Fpanel) | v0.1.0 | zeimoto | Content-language indicators and validation highlights for the Kirby Panel. |
| 2026-10-13 07:31:30 | [wexample/symfony-workspace-demo](https://www.nuget.org/packages/wexample%2Fsymfony-workspace-demo) | 1.0.1 |  |  |
| 2026-10-13 07:43:43 | [symfony/ux-inspector](https://www.nuget.org/packages/symfony%2Fux-inspector) | v3.6.0 | Simon André; Symfony Community | Browser inspector for Symfony UX components: Stimulus, LiveComponent and Turbo |
| 2026-10-13 07:43:43 | [symfony/ux-router](https://www.nuget.org/packages/symfony%2Fux-router) | v3.6.0 | Hugo Alliaume; Symfony Commun… | Exposes Symfony Routes directly to JavaScript. |
| 2026-10-13 07:45:37 | [caturseptian/laravel-indonesia-territory](https://www.nuget.org/packages/caturseptian%2Flaravel-indonesia-territory) | v1.0.1 | Catur Septian | Indonesian administrative regions (Kemendagri codes) for Laravel: provinces, re… |
| 2026-10-13 07:50:20 | [software-technologies-limited/stl-date-picker-widget](https://www.nuget.org/packages/software-technologies-limited%2Fstl-date-picker-widget) | v2.0.1 | Software Technologies Limited… | Framework-agnostic PHP date picker and date range components. |
| 2026-10-13 07:53:06 | [vortech/laravel-trace](https://www.nuget.org/packages/vortech%2Flaravel-trace) | v0.2.0 | Mate Papp | One-way, change-based synchronization of published Eloquent data between two La… |
| 2026-10-13 07:54:42 | [nxi/factro-sdk](https://www.nuget.org/packages/nxi%2Ffactro-sdk) | 1.0.0 | NXI GmbH & Co. KG | Unofficial PHP SDK for the factro Core API, built on Symfony components |
| 2026-10-13 08:01:39 | [silvershop/bundles](https://www.nuget.org/packages/silvershop%2Fbundles) | 1.0.0 | SilverShop Contributors | Bundle products for SilverShop: sell a product that groups other products and a… |
| 2026-10-13 08:02:46 | [wexample/symfony-design-system-effects](https://www.nuget.org/packages/wexample%2Fsymfony-design-system-effects) | 1.0.1 |  |  |
| 2026-10-13 08:03:32 | [software-technologies-limited/stl-editable-widget](https://www.nuget.org/packages/software-technologies-limited%2Fstl-editable-widget) | v2.0.0 | Software Technologies Limited… | Framework-agnostic inline editing components for PHP applications. |
| 2026-10-13 08:04:51 | [pollora/wp-rest](https://www.nuget.org/packages/pollora%2Fwp-rest) | v0.1.0 | Amphibee | WordPress REST API routes declared with PHP attributes: a controller class, #[W… |
| 2026-10-13 08:04:55 | [pollora/wp-cli](https://www.nuget.org/packages/pollora%2Fwp-cli) | v0.1.0 | Amphibee | WP-CLI commands declared with PHP attributes: a class with #[WpCli], subcommand… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
