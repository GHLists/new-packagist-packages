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

## Latest list — 2026-11-18 05:20 UTC

New packages created between 2026-11-18 04:20 UTC and 2026-11-18 05:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T05-20-32-809679Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 04:22:31 | [hampel/paypal-api](https://www.nuget.org/packages/hampel%2Fpaypal-api) | 0.1.0 | Simon Hampel | A PHP client for the PayPal REST API - transaction search, captures and refunds… |
| 2026-11-18 04:52:59 | [robsontaviano/meadow](https://www.nuget.org/packages/robsontaviano%2Fmeadow) | 1.0.2 | Robson Tenório | Gorgeous UI components for Livewire powered by daisyUI and Tailwind |
| 2026-11-18 05:00:26 | [hampel/paypal-api-laravel](https://www.nuget.org/packages/hampel%2Fpaypal-api-laravel) | 0.1.0 | Simon Hampel | Laravel service provider, manager and facade for the PayPal REST API client, wi… |
| 2026-11-18 05:04:13 | [jeffersongoncalves/laravel-quebec-requests](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-quebec-requests) | 1.0.0 | Jefferson Gonçalves | Requests under Quebec Law 25: access, rectification, deletion, de-indexation, p… |
| 2026-11-18 05:09:10 | [jeffersongoncalves/laravel-quebec-incidents](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-quebec-incidents) | 1.0.0 | Jefferson Gonçalves | Confidentiality incidents under Quebec Law 25: the mandatory incident register,… |
| 2026-11-18 05:13:12 | [jeffersongoncalves/laravel-quebec-governance](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-quebec-governance) | 1.0.0 | Jefferson Gonçalves | Governance under Quebec Law 25: the person in charge of the protection of perso… |
| 2026-11-18 05:17:29 | [jeffersongoncalves/laravel-quebec-vendors](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-quebec-vendors) | 1.0.0 | Jefferson Gonçalves | Vendors under Quebec Law 25: service providers with a written mandate contract… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
