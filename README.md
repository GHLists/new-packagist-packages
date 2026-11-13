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

## Latest list — 2026-11-13 18:19 UTC

New packages created between 2026-11-13 17:20 UTC and 2026-11-13 18:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T18-19-33-503948Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 17:27:59 | [tornado-engine/cron](https://www.nuget.org/packages/tornado-engine%2Fcron) | v0.1.0 |  | Tornado Engine core-module: scheduled jobs. Modules register jobs; admins choos… |
| 2026-11-13 17:34:47 | [largerio/laravel-concurrency-limit](https://www.nuget.org/packages/largerio%2Flaravel-concurrency-limit) | v1.0.0 | Louis | Cap in-flight HTTP requests and concurrent queued jobs per user, tenant or key… |
| 2026-11-13 17:59:14 | [dotenvx/phpdotenvx-ext](https://www.nuget.org/packages/dotenvx%2Fphpdotenvx-ext) | v0.1.0 |  | Native PHP extension for Dotenvx |
| 2026-11-13 17:59:26 | [larwell/laravel-quick-mcp](https://www.nuget.org/packages/larwell%2Flaravel-quick-mcp) | v1.0.0 | Ishrafil Khan | Effortless Model Context Protocol (MCP) server integration for Laravel applicat… |
| 2026-11-13 18:01:31 | [tornado-engine/broker](https://www.nuget.org/packages/tornado-engine%2Fbroker) | v0.1.0 |  | Tornado Engine module: lets Claude work with directory data through pseudonyms,… |
| 2026-11-13 18:01:34 | [webwizardsusa/rich-editor-plus-embed](https://www.nuget.org/packages/webwizardsusa%2Frich-editor-plus-embed) | v0.1.0 | Jamie Holly | oEmbed embeds for Rich Editor Plus: paste a YouTube, Vimeo, X or other supporte… |
| 2026-11-13 18:04:15 | [jonatasfenske/datalayer](https://www.nuget.org/packages/jonatasfenske%2Fdatalayer) | v1.0.0 | Robson V. Leite; Jonatas Fens… | Abstração de persistência PHP 8.5 com QueryBuilder fluente, Soft Deletes, Relac… |
| 2026-11-13 18:07:41 | [jonatasfenske/router](https://www.nuget.org/packages/jonatasfenske%2Frouter) | v1.0.0 | Robson V. Leite; Jonatas Fens… | Roteamento MVC PHP 8.5 com atributos #[Route], Rate Limiting, CORS automático,… |
| 2026-11-13 18:08:07 | [jonatasfenske/uploader](https://www.nuget.org/packages/jonatasfenske%2Fuploader) | v1.0.0 | Robson V. Leite; Jonatas Fens… | Upload seguro de arquivos PHP 8.5 com validação MIME real via finfo_file, sanit… |
| 2026-11-13 18:08:28 | [jonatasfenske/cropper](https://www.nuget.org/packages/jonatasfenske%2Fcropper) | v1.0.0 | Robson V. Leite; Jonatas Fens… | Crop inteligente de imagens PHP 8.5 com Focal Point, suporte AVIF/WebP nativo,… |
| 2026-11-13 18:08:42 | [youvision/think-store](https://www.nuget.org/packages/youvision%2Fthink-store) | v1.4.0 | indiboy-create; AI | ThinkPHP 8 商店扩展：查询主项目中已安装的 think-store-* 发布包。 |
| 2026-11-13 18:08:47 | [jonatasfenske/optimizer](https://www.nuget.org/packages/jonatasfenske%2Foptimizer) | v1.0.0 | Robson V. Leite; Jonatas Fens… | SEO e meta tags PHP 8.5 com Schema.org JSON-LD, Open Graph, Twitter Cards, Site… |
| 2026-11-13 18:09:05 | [jonatasfenske/paginator](https://www.nuget.org/packages/jonatasfenske%2Fpaginator) | v1.0.0 | Robson V. Leite; Jonatas Fens… | Paginação PHP 8.5 com suporte offset-based e cursor-based, templates Bootstrap/… |
| 2026-11-13 18:09:24 | [jonatasfenske/validator](https://www.nuget.org/packages/jonatasfenske%2Fvalidator) | v1.0.0 | Robson V. Leite; Jonatas Fens… | Validação declarativa PHP 8.5 com 30+ rules, mensagens em português, regras cus… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
