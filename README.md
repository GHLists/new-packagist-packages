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

## Latest list — 2026-11-26 14:20 UTC

New packages created between 2026-11-26 13:20 UTC and 2026-11-26 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T14-20-40-919855Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 13:21:02 | [restruct/silverstripe-video-consent-gate](https://www.nuget.org/packages/restruct%2Fsilverstripe-video-consent-gate) | 0.1.0 | Restruct | YouTube and Vimeo embeds that make no request to YouTube or Vimeo before consen… |
| 2026-11-26 13:21:15 | [searchjet/laravel-searchjet](https://www.nuget.org/packages/searchjet%2Flaravel-searchjet) | v2.0.0 | SearchJet | Laravel client for the SearchJet search API: search, document indexing and sear… |
| 2026-11-26 13:22:35 | [data-health/data-health-filament](https://www.nuget.org/packages/data-health%2Fdata-health-filament) | v0.1.0 | Jascha Gerles | A Filament interface for managing Data Health findings |
| 2026-11-26 13:30:21 | [pecotamic/glide-versioning](https://www.nuget.org/packages/pecotamic%2Fglide-versioning) | 1.0.0 | Werner Freytag | Cache busting for statically cached Glide images in Statamic |
| 2026-11-26 13:31:59 | [solution25/typo3-ai-connector](https://www.nuget.org/packages/solution25%2Ftypo3-ai-connector) | v0.1.0 | Solution25 | AI connector - Connects a TYPO3 site to AI clients such as Claude through the S… |
| 2026-11-26 13:34:13 | [arkhan0072-dev/laravel-zatca](https://www.nuget.org/packages/arkhan0072-dev%2Flaravel-zatca) | v0.3.0 | Abdulrehman Khan | ZATCA (Fatoora) e-invoicing for Laravel: a concurrency-safe invoice chain, onbo… |
| 2026-11-26 13:35:39 | [aclips/class-override](https://www.nuget.org/packages/aclips%2Fclass-override) | v1.0.2 |  | Runtime PHP class overriding with inheritance |
| 2026-11-26 13:43:47 | [doolat/balanced-brackets](https://www.nuget.org/packages/doolat%2Fbalanced-brackets) | v1.0.0 |  | Validates balanced brackets: (), [], {} |
| 2026-11-26 13:51:22 | [nedbb/secure-upload](https://www.nuget.org/packages/nedbb%2Fsecure-upload) | v1.0.0 | nedbb | A small, secure-by-default file upload library |
| 2026-11-26 14:04:59 | [qiick/laravel-settings](https://www.nuget.org/packages/qiick%2Flaravel-settings) | v0.1.0-beta.1 | Qiick | Scoped, typed settings and encrypted secrets for qiick Laravel products. |
| 2026-11-26 14:06:20 | [trongio/php-ts-types](https://www.nuget.org/packages/trongio%2Fphp-ts-types) | v0.1.0 |  | Generate TypeScript types from PHP classes: a small structural type model, a de… |
| 2026-11-26 14:07:54 | [bmailu/bmailu](https://www.nuget.org/packages/bmailu%2Fbmailu) | v0.1.0 |  | Official PHP SDK for the Bmailu Email API |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
