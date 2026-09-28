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

## Latest list — 2026-09-28 07:23 UTC

New packages created between 2026-09-28 06:22 UTC and 2026-09-28 07:23 UTC.

[Full CSV](data/new-packagist-packages-2026-09-28T07-23-03-926521Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-28 07:02:10 | [cors/symfony-ai-506-platform](https://www.nuget.org/packages/cors%2Fsymfony-ai-506-platform) | 0.1 | CORS GmbH | 506.ai platform bridge for Symfony AI |
| 2026-09-28 07:03:41 | [amdadulhaq/bangla-slug-laravel](https://www.nuget.org/packages/amdadulhaq%2Fbangla-slug-laravel) | v1.0.0 | Amdadul Haq | Readable Banglish URL slugs from Bangla text for Laravel: phonetic transliterat… |
| 2026-09-28 07:10:32 | [wexample/php-api-entity](https://www.nuget.org/packages/wexample%2Fphp-api-entity) | 1.0.1 | Wexample | Client-side entities, repositories and envelope for APIs served by wexample/sym… |
| 2026-09-28 07:12:28 | [cloud-castle/gui](https://www.nuget.org/packages/cloud-castle%2Fgui) | v0.1.0 | CloudCastle | Production-ready PHP 8.1+ package (CloudCastle GUI). |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
