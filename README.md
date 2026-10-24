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

## Latest list — 2026-10-24 18:21 UTC

New packages created between 2026-10-24 17:27 UTC and 2026-10-24 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-24T18-21-32-530771Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-24 17:35:33 | [noldors/phpstan-extension](https://www.nuget.org/packages/noldors%2Fphpstan-extension) | v0.2.0 |  | Custom PHPStan rules for PHP and Laravel projects. |
| 2026-10-24 17:37:55 | [bad_cluster/runway-console-app](https://www.nuget.org/packages/bad_cluster%2Frunway-console-app) | 1.0.0 | BaD ClusteR | Console applications for Runway: commands, input parsing, formatted output, tab… |
| 2026-10-24 17:55:31 | [drupal/varbase_ai_vdb_milvus](https://www.nuget.org/packages/drupal%2Fvarbase_ai_vdb_milvus) | 1.0.0-alpha1 | Vardot | Connects a Varbase site to a Milvus or Zilliz Cloud vector database for AI Sear… |
| 2026-10-24 17:55:40 | [trianity/laravel-mautic](https://www.nuget.org/packages/trianity%2Flaravel-mautic) | v1.0.0 | Istvan Holbok | Explicit, model-independent Laravel integration for the Mautic REST API. |
| 2026-10-24 17:56:18 | [drupal/varbase_ai_chatbot_base](https://www.nuget.org/packages/drupal%2Fvarbase_ai_chatbot_base) | 1.0.0-alpha1 | Vardot | A visitor chatbot for Varbase 11 that answers only from the site's own content,… |
| 2026-10-24 17:56:47 | [drupal/varbase_ai_answers_base](https://www.nuget.org/packages/drupal%2Fvarbase_ai_answers_base) | 1.0.0-alpha1 | Vardot | Ask AI for Varbase: a public question box that answers from the site's own cont… |
| 2026-10-24 17:57:25 | [drupal/varbase_ai_content_review_base](https://www.nuget.org/packages/drupal%2Fvarbase_ai_content_review_base) | 1.0.0-alpha1 | Vardot | AI content review for Varbase 11: four review agents and one rule for every con… |
| 2026-10-24 17:58:07 | [drupal/varbase_ai_content_operations_base](https://www.nuget.org/packages/drupal%2Fvarbase_ai_content_operations_base) | 1.0.0-alpha1 | Vardot | A content operations assistant for the editors of a Varbase 11 site: audits bro… |
| 2026-10-24 17:59:36 | [drupal/varbase_ai_mcp_server_base](https://www.nuget.org/packages/drupal%2Fvarbase_ai_mcp_server_base) | 1.0.0-alpha1 | Vardot | Varbase AI MCP Server: an MCP server for external assistants (Claude.ai and sim… |
| 2026-10-24 18:08:14 | [thekaziomar/laravel-atomic-cache](https://www.nuget.org/packages/thekaziomar%2Flaravel-atomic-cache) | v1.0.1 | Kazi Omar Faruk | A simple, stampede-proof, and tag-aware caching package for Laravel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
