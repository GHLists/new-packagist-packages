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

## Latest list — 2026-10-18 19:19 UTC

New packages created between 2026-10-18 18:19 UTC and 2026-10-18 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T19-19-38-306481Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 18:22:07 | [numberotp/numberotp](https://www.nuget.org/packages/numberotp%2Fnumberotp) | v0.1.1 | NumberOTP | Official NumberOTP API client — virtual phone numbers for SMS / OTP verification |
| 2026-10-18 18:23:24 | [1994/abandoned-cart-statamic](https://www.nuget.org/packages/1994%2Fabandoned-cart-statamic) | v1.0.1 | 1994 | Abandoned cart recovery for Cargo: reminder emails, with a link that brings the… |
| 2026-10-18 18:27:32 | [pr3slaff/psst](https://www.nuget.org/packages/pr3slaff%2Fpsst) | v1.0.0 | pr3slaff | Deliberate, fail-silent Laravel events and authenticated health metrics. |
| 2026-10-18 18:42:04 | [1994/reviews-craft](https://www.nuget.org/packages/1994%2Freviews-craft) | 1.0.0 | 1994 | Reviews and star ratings for Craft CMS, collected on your own site: moderation,… |
| 2026-10-18 18:44:52 | [alantiller/database](https://www.nuget.org/packages/alantiller%2Fdatabase) | v1.0.0 | Alan Tiller | A Medoo database wrapper with versioned migrations and database management for… |
| 2026-10-18 18:46:54 | [saurabhg/module-ai-product-recommend](https://www.nuget.org/packages/saurabhg%2Fmodule-ai-product-recommend) | 1.0.0 |  | AI Product Recommendation & Personalization: behavioral + semantic hybrid recom… |
| 2026-10-18 18:49:59 | [jaggedjax/psp](https://www.nuget.org/packages/jaggedjax%2Fpsp) | v0.1.0 |  | PHP Starter Project - Lightweight common utilities to help you get going |
| 2026-10-18 19:02:23 | [njdigitallab/laraauth](https://www.nuget.org/packages/njdigitallab%2Flaraauth) | v1.0.1 | Jenry Ollivierre | An authentication package for laravel |
| 2026-10-18 19:06:42 | [itaja/itaja-laravel](https://www.nuget.org/packages/itaja%2Fitaja-laravel) | v0.1.0 |  | Itaja for Laravel: declare what you sell in code, push it, receive webhooks as… |
| 2026-10-18 19:10:01 | [rmb32/kevin](https://www.nuget.org/packages/rmb32%2Fkevin) | v1.3.0 | Roger Barnfather | Save tons of tokens! Get your A.I. to use Kevin for filesystem tasks in PHP pro… |
| 2026-10-18 19:11:45 | [edwin-ortizp/laravel-markdown](https://www.nuget.org/packages/edwin-ortizp%2Flaravel-markdown) | v0.1.0 |  | Framework-independent Markdown editor UI and safe viewer for Laravel Blade, wit… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
