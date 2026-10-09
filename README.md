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

## Latest list — 2026-10-09 17:21 UTC

New packages created between 2026-10-09 16:20 UTC and 2026-10-09 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T17-21-14-355897Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 16:22:06 | [fostercommerce/commerce-net-terms](https://www.nuget.org/packages/fostercommerce%2Fcommerce-net-terms) | 1.0.0 | Foster Commerce | Net Terms is a Craft Commerce payment gateway that bills orders on net terms, t… |
| 2026-10-09 16:22:18 | [aybarsm/apache-apisix-admin-api](https://www.nuget.org/packages/aybarsm%2Fapache-apisix-admin-api) | v0.1.0 | Murat Aybars | Framework-agnostic, typed, resource-oriented PHP client for the Apache APISIX A… |
| 2026-10-09 16:33:38 | [ojessecruz/resend-inbox](https://www.nuget.org/packages/ojessecruz%2Fresend-inbox) | v0.1.0 | jessecruz | Framework-agnostic core of a Resend-powered shared inbox: webhook parsing, conv… |
| 2026-10-09 16:34:07 | [ojessecruz/laravel-resend-inbox](https://www.nuget.org/packages/ojessecruz%2Flaravel-resend-inbox) | v0.1.0 | jessecruz | A shared inbox for your Laravel admin on top of Resend inbound email: conversat… |
| 2026-10-09 16:36:16 | [pixelfix/installer](https://www.nuget.org/packages/pixelfix%2Finstaller) | v0.1.0 |  | Global CLI installer for PixelFix applications |
| 2026-10-09 16:40:53 | [naf/flow](https://www.nuget.org/packages/naf%2Fflow) | v0.1.0 | Flo Knapp | Reactive JavaScript components and HTML updates for NAF, automatically integrat… |
| 2026-10-09 16:59:15 | [humanmade/hm-facet-blocks](https://www.nuget.org/packages/humanmade%2Fhm-facet-blocks) | v0.1.0 | Human Made | Blocks for filtering content already on the page by facets |
| 2026-10-09 17:07:35 | [duva-mail/laravel](https://www.nuget.org/packages/duva-mail%2Flaravel) | v0.1.0 | 9573-4562 Québec inc. | Laravel mail transport for Duva, the transactional email API hosted in Canada. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
