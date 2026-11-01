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

## Latest list — 2026-11-01 00:20 UTC

New packages created between 2026-10-31 23:19 UTC and 2026-11-01 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-01T00-20-51-920894Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 23:30:39 | [cacheerphp/laravel](https://www.nuget.org/packages/cacheerphp%2Flaravel) | v1.0.1 | Silvio Silva | A Laravel cache driver backed by CacheerPHP: keep using Cache:: and get Cacheer… |
| 2026-10-31 23:39:33 | [mj-zana/skeleton-api](https://www.nuget.org/packages/mj-zana%2Fskeleton-api) | v2.9.0 |  | A starting point for a Zana JSON API: modules, bearer tokens, problem JSON erro… |
| 2026-10-31 23:51:11 | [mtubis/html-translator-bundle](https://www.nuget.org/packages/mtubis%2Fhtml-translator-bundle) | v0.1.0 | Magdalena Tubis | Symfony bundle for mtubis/html-translator: translate HTML with LLMs (OpenAI, An… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
