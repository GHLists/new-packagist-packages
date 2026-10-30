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

## Latest list — 2026-10-30 16:19 UTC

New packages created between 2026-10-30 15:22 UTC and 2026-10-30 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T16-19-16-680494Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 15:28:28 | [akawaka/sylius-cms-plugin](https://www.nuget.org/packages/akawaka%2Fsylius-cms-plugin) | v1.0.0 |  | CMS pages with a block-based page builder and live multi-device preview for Syl… |
| 2026-10-30 15:29:24 | [mage2kishan/module-ai-visibility](https://www.nuget.org/packages/mage2kishan%2Fmodule-ai-visibility) | 1.1.0 | Kishan Savaliya | Panth AI Visibility - analytics for Magento 2 that counts AI crawler requests (… |
| 2026-10-30 15:35:11 | [sylvainallignol/minify-html](https://www.nuget.org/packages/sylvainallignol%2Fminify-html) | v1.0.1 | Sylvain Allignol | Enable minify HTML output for Kirby |
| 2026-10-30 15:51:07 | [survos/duckdb-bundle](https://www.nuget.org/packages/survos%2Fduckdb-bundle) | 2.45.8 |  | Read-only DuckDB PDO connections and explicit named local or S3 sources for Sym… |
| 2026-10-30 15:52:28 | [sadpcd/laravel-error-reporter](https://www.nuget.org/packages/sadpcd%2Flaravel-error-reporter) | v1.1.0 | SADPCD | Resilient 500 Error Reporter with Flood Protection, Livewire/Inertia Context, a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
