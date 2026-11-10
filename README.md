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

## Latest list — 2026-11-10 17:20 UTC

New packages created between 2026-11-10 16:20 UTC and 2026-11-10 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T17-20-15-144005Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 16:22:50 | [ernestdefoe/predictions](https://www.nuget.org/packages/ernestdefoe%2Fpredictions) | 1.0.0 | Ernest Defoe | Predictions: members call it before it happens. Multiple choice, yes/no and clo… |
| 2026-11-10 16:25:10 | [ernestdefoe/secret-santa](https://www.nuget.org/packages/ernestdefoe%2Fsecret-santa) | 1.0.0 | Ernest Defoe | Secret Santa: gift exchanges for your community. Sign-ups with wishlists, an au… |
| 2026-11-10 16:25:33 | [astral-php/astral-nova-css](https://www.nuget.org/packages/astral-php%2Fastral-nova-css) | 1.0.0 |  | Framework-agnostic CSS design system and theme assets for Astral applications. |
| 2026-11-10 16:25:48 | [astral-php/astral-nova-icons](https://www.nuget.org/packages/astral-php%2Fastral-nova-icons) | 1.0.0 |  | Optional Nova SVG icon sprite and sizing CSS for Astral applications. |
| 2026-11-10 16:26:15 | [astral-php/astral-template-nova](https://www.nuget.org/packages/astral-php%2Fastral-template-nova) | 1.0.0 |  | Nova-based layouts and reusable PHP view partials for Astral applications. |
| 2026-11-10 16:38:15 | [anuarhdz/craft-r2](https://www.nuget.org/packages/anuarhdz%2Fcraft-r2) | 0.1.0 | anuarhdz | Cloudflare R2 filesystem for Craft CMS. |
| 2026-11-10 16:46:52 | [kasevvlad/idempotency](https://www.nuget.org/packages/kasevvlad%2Fidempotency) | v0.1.0 | kasevvlad | Idempotency-Key header support for Laravel and Symfony: safe retries for POST/P… |
| 2026-11-10 16:57:29 | [ernestdefoe/garage](https://www.nuget.org/packages/ernestdefoe%2Fgarage) | 1.0.0 | Ernest Defoe | Garage: members show off their builds (cars, PCs, keyboards, guitars, gardens,… |
| 2026-11-10 17:00:03 | [zerofront/module-zero-ai-assistant](https://www.nuget.org/packages/zerofront%2Fmodule-zero-ai-assistant) | 1.3.9 | Roman Pasichnyk | Zero for Magento Open Source: an AI assistant in the admin for the catalog, con… |
| 2026-11-10 17:00:03 | [zerofront/module-zero-mcp](https://www.nuget.org/packages/zerofront%2Fmodule-zero-mcp) | 1.3.9 | Roman Pasichnyk | Zero for Magento Open Source: the store as a connector in Claude (an MCP server… |
| 2026-11-10 17:04:04 | [pecl/krb5](https://www.nuget.org/packages/pecl%2Fkrb5) | v1.3.0 |  | Kerberos/GSSPI and KAdmin bindings for PHP |
| 2026-11-10 17:05:55 | [totalcms/starter-events](https://www.nuget.org/packages/totalcms%2Fstarter-events) | v1.0.0 | Joe Workman | Lantern Row Market: an events site for Total CMS, with news posts, a season of… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
