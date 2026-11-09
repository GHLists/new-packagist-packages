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

## Latest list — 2026-11-09 09:20 UTC

New packages created between 2026-11-09 08:20 UTC and 2026-11-09 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-09T09-20-47-872475Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-09 08:27:25 | [flxlabs/silverstripe-cms-mcp](https://www.nuget.org/packages/flxlabs%2Fsilverstripe-cms-mcp) | v0.1.0 | FLX Labs; Icecaster | Exposes SilverStripe CMS content (fields, file uploads, draft/publish workflow)… |
| 2026-11-09 08:28:13 | [flxlabs/silverstripe-cms-mcp-pagesections](https://www.nuget.org/packages/flxlabs%2Fsilverstripe-cms-mcp-pagesections) | v0.1.0 | FLX Labs | Pagesection tools for silverstripe-cms-mcp |
| 2026-11-09 08:29:43 | [codecruz/currency-flow](https://www.nuget.org/packages/codecruz%2Fcurrency-flow) | v0.1.0 | codecruz | Official ECB euro foreign exchange reference rates, with historical lookups and… |
| 2026-11-09 08:31:06 | [fluffydiscord/sylius-customer-group-rules-bundle](https://www.nuget.org/packages/fluffydiscord%2Fsylius-customer-group-rules-bundle) | v1.0.0 | FluffyDiscord | Customer group inheritance and allowed payment and shipping methods per group f… |
| 2026-11-09 08:49:58 | [scify/laravel-health-endpoint](https://www.nuget.org/packages/scify%2Flaravel-health-endpoint) | v0.1.0 | SciFY | A token-protected, rate-limited /health endpoint for Laravel, built on spatie/l… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
