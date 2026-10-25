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

## Latest list — 2026-10-25 07:21 UTC

New packages created between 2026-10-25 06:21 UTC and 2026-10-25 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T07-21-00-747197Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 06:35:28 | [atannex/billing](https://www.nuget.org/packages/atannex%2Fbilling) | v1.0.0 | Atanga Leke Collins | Payments for Laravel across Stripe, MTN Mobile Money, Orange Money, PayPal and… |
| 2026-10-25 06:55:19 | [jsonscraper/instagram-mcp-server](https://www.nuget.org/packages/jsonscraper%2Finstagram-mcp-server) | 0.1.2 |  | Official Instagram Scraper API MCP server for ChatGPT, Codex and MCP clients |
| 2026-10-25 06:55:32 | [jsonscraper/tiktok-mcp-server](https://www.nuget.org/packages/jsonscraper%2Ftiktok-mcp-server) | 0.1.2 |  | Official TikTok Scraper API MCP server for ChatGPT, Codex and MCP clients |
| 2026-10-25 06:57:09 | [atannex/share](https://www.nuget.org/packages/atannex%2Fshare) | v1.1.0 | Atanga Leke Collins | Share anything to any platform from Laravel: models, links, text or files to 35… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
