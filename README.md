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

## Latest list — 2026-10-31 15:21 UTC

New packages created between 2026-10-31 14:20 UTC and 2026-10-31 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T15-21-16-597888Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 14:35:08 | [bbwdadfg/bazicalculator-url-tools](https://www.nuget.org/packages/bbwdadfg%2Fbazicalculator-url-tools) | v0.1.1 | wangneo276-lgtm | Free BaZi calculator: Four Pillars, Day Master, Ten Gods, Five Elements and Luc… |
| 2026-10-31 14:47:49 | [rem42/shadcn-admin-ui](https://www.nuget.org/packages/rem42%2Fshadcn-admin-ui) | v1.0.0 | Rem42 | Tailwind CSS + shadcn/ui (Symfony UX Toolkit) admin theme for Sylius Stack, a d… |
| 2026-10-31 14:48:53 | [siteation/magento2-commerce365-debugbar](https://www.nuget.org/packages/siteation%2Fmagento2-commerce365-debugbar) | 1.0.0 | Siteation | Commerce365 section for Siteation_DebugBar: customer prices, Hub and Business C… |
| 2026-10-31 14:59:56 | [tenma/image](https://www.nuget.org/packages/tenma%2Fimage) | v0.1.0 |  | Image size and scaled WebP copies on Tenma, decoded off the event loop by a nat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
