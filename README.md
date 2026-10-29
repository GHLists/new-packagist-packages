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

## Latest list — 2026-10-29 18:20 UTC

New packages created between 2026-10-29 17:21 UTC and 2026-10-29 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T18-20-53-122232Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 17:22:38 | [handersonsilva/laravel-bruno-docs](https://www.nuget.org/packages/handersonsilva%2Flaravel-bruno-docs) | v1.0.0 |  | Serve a Bruno collection as a Swagger UI page in Laravel. |
| 2026-10-29 17:33:43 | [dmlab/module-price-explain](https://www.nuget.org/packages/dmlab%2Fmodule-price-explain) | 0.0.1 |  | Explains why a Magento 2 cart or order costs what it costs: item price layers,… |
| 2026-10-29 18:03:59 | [jacobtobies/glass](https://www.nuget.org/packages/jacobtobies%2Fglass) | v1.0.1 | Jacob Tobies | Glass: a frosted-glass skin for Roundcube Webmail, based on Elastic, with adjus… |
| 2026-10-29 18:04:44 | [generoi/gds-llms](https://www.nuget.org/packages/generoi%2Fgds-llms) | v0.1.0 | Genero | Serves /llms.txt and a markdown version of every page for language models |
| 2026-10-29 18:18:31 | [tinect/passkeys](https://www.nuget.org/packages/tinect%2Fpasskeys) | 1.0.0 | tinect | Passkey (WebAuthn) login for storefront customers |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
