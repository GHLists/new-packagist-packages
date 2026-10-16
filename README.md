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

## Latest list — 2026-10-16 08:21 UTC

New packages created between 2026-10-16 07:20 UTC and 2026-10-16 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T08-21-05-25994Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 07:21:08 | [saij/wp-app-starter](https://www.nuget.org/packages/saij%2Fwp-app-starter) | v0.1.0 |  | Creates a theme, child theme or plugin built with wp-app-framework: composer cr… |
| 2026-10-16 07:23:21 | [wexample/php-git](https://www.nuget.org/packages/wexample%2Fphp-git) | 1.0.1 |  |  |
| 2026-10-16 07:24:05 | [wexample/symfony-git](https://www.nuget.org/packages/wexample%2Fsymfony-git) | 1.0.1 |  |  |
| 2026-10-16 07:24:34 | [wexample/symfony-git-ds](https://www.nuget.org/packages/wexample%2Fsymfony-git-ds) | 1.0.1 |  |  |
| 2026-10-16 07:49:22 | [qiangvei/magento2-theme-amazon](https://www.nuget.org/packages/qiangvei%2Fmagento2-theme-amazon) | 1.0.0 |  | Amazon style theme for Magento 2.4 |
| 2026-10-16 08:01:39 | [bakslash/static-site-bundle](https://www.nuget.org/packages/bakslash%2Fstatic-site-bundle) | v0.1.0 | Mathias Arlaud | Generate a static site by prerendering Symfony routes. |
| 2026-10-16 08:07:30 | [chatsong/voice-note](https://www.nuget.org/packages/chatsong%2Fvoice-note) | 1.0.0 |  | Voice Note en Audio Demo recorder voor Chatsong |
| 2026-10-16 08:07:31 | [iqual/icms_mcp](https://www.nuget.org/packages/iqual%2Ficms_mcp) | v1.0.0 |  | Drupal MCP tools for AI-powered, transactional ICMS content migration and impor… |
| 2026-10-16 08:12:24 | [iqual/pagedesigner_export](https://www.nuget.org/packages/iqual%2Fpagedesigner_export) | v1.0.0 |  | Exports and imports Pagedesigner element trees with full translation support |
| 2026-10-16 08:18:37 | [hypervel/guzzle](https://www.nuget.org/packages/hypervel%2Fguzzle) | 8.2.0.1 | Graham Campbell; Michael Dowl… | Hypervel's fork of Guzzle, a PHP HTTP client library |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
