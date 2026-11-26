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

## Latest list — 2026-11-26 18:20 UTC

New packages created between 2026-11-26 17:22 UTC and 2026-11-26 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T18-20-49-32235Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 17:22:57 | [ghimire/laravel-saas](https://www.nuget.org/packages/ghimire%2Flaravel-saas) | 0.1.0 |  | All-in-one modular Laravel 8-13 multi-tenant SaaS engine, billing, subscription… |
| 2026-11-26 17:29:26 | [atom-fm/validation](https://www.nuget.org/packages/atom-fm%2Fvalidation) | v0.1.0 |  | Attribute and schema validation for PHP |
| 2026-11-26 17:32:47 | [tuxweb-it/pyroshape](https://www.nuget.org/packages/tuxweb-it%2Fpyroshape) | v0.9.3 | Dino Ciuffetti | Reusable backend toolkit for Pyroshape applications |
| 2026-11-26 17:39:04 | [rasuvaeff/laravel-mcp](https://www.nuget.org/packages/rasuvaeff%2Flaravel-mcp) | v0.1.0 | Victor Razuvaev | Laravel integration of the rasuvaeff/mcp server |
| 2026-11-26 17:39:04 | [rasuvaeff/symfony-mcp](https://www.nuget.org/packages/rasuvaeff%2Fsymfony-mcp) | v0.1.0 | Victor Razuvaev | Symfony integration of the rasuvaeff/mcp server |
| 2026-11-26 17:55:59 | [kongono/ai](https://www.nuget.org/packages/kongono%2Fai) | v1.22.0 | Anthony Iovanna | Kongono v1 standalone PHP 8.5 multi-provider AI SDK (OpenAI, Anthropic Claude,… |
| 2026-11-26 17:55:59 | [kongono/security](https://www.nuget.org/packages/kongono%2Fsecurity) | v1.22.0 | Anthony Iovanna | Kongono v1 standalone PHP 8.5 security & passwordless auth primitives: HKDF XCh… |
| 2026-11-26 17:55:59 | [kongono/validation](https://www.nuget.org/packages/kongono%2Fvalidation) | v1.22.0 | Anthony Iovanna | Kongono v1 zero-bloat PHP 8.5 attribute-driven readonly DTO validator (nested D… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
