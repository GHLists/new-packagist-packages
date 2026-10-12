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

## Latest list — 2026-10-12 18:18 UTC

New packages created between 2026-10-12 17:19 UTC and 2026-10-12 18:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-12T18-18-57-833306Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-12 17:33:48 | [wexample/symfony-remote-peppol](https://www.nuget.org/packages/wexample%2Fsymfony-remote-peppol) | 1.0.1 |  |  |
| 2026-10-12 17:34:48 | [tmonier/sylius-purchase-approval-plugin](https://www.nuget.org/packages/tmonier%2Fsylius-purchase-approval-plugin) | v1.0.1 | Thibaut Monier | Purchase approval for Sylius 2 B2B company accounts: order and approval limits… |
| 2026-10-12 17:35:42 | [woit/si-llms-txt](https://www.nuget.org/packages/woit%2Fsi-llms-txt) | 1.0.3 | Siva | LLMs.txt & Markdown for AI |
| 2026-10-12 17:39:34 | [se7enxweb/expai](https://www.nuget.org/packages/se7enxweb%2Fexpai) | v0.0.1.0 | 7x | Exponential Intelligence (Powered by Claude from Anthropic): a writing assistan… |
| 2026-10-12 17:40:26 | [zcwilt/forumkit-logs](https://www.nuget.org/packages/zcwilt%2Fforumkit-logs) | v0.1.0 |  | Email logs for ForumKit. |
| 2026-10-12 17:45:56 | [wexample/symfony-accounting-ds](https://www.nuget.org/packages/wexample%2Fsymfony-accounting-ds) | 1.0.1 |  |  |
| 2026-10-12 17:46:59 | [wexample/symfony-accounting-demo](https://www.nuget.org/packages/wexample%2Fsymfony-accounting-demo) | 1.0.1 |  |  |
| 2026-10-12 17:49:55 | [pharaonic/php-fingerprint](https://www.nuget.org/packages/pharaonic%2Fphp-fingerprint) | 8.0.0 | Moamen Eltouny (Raggi) | Deterministic fingerprints and ordered signatures for PHP data: canonical map o… |
| 2026-10-12 17:54:12 | [wexample/symfony-remote-ecb](https://www.nuget.org/packages/wexample%2Fsymfony-remote-ecb) | 1.0.1 |  |  |
| 2026-10-12 18:01:55 | [sezer/monolith-modular](https://www.nuget.org/packages/sezer%2Fmonolith-modular) | v1.0.2 | Hussien Attia | Modular monolith scaffolding and Artisan generators for Laravel |
| 2026-10-12 18:08:01 | [phpmystic/typic](https://www.nuget.org/packages/phpmystic%2Ftypic) | v0.1.0 |  | Modern, code-first, attribute-driven GraphQL framework for PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
