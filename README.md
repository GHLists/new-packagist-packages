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

## Latest list — 2026-11-05 14:21 UTC

New packages created between 2026-11-05 13:21 UTC and 2026-11-05 14:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T14-21-47-442036Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 13:24:56 | [crabphp/crab](https://www.nuget.org/packages/crabphp%2Fcrab) | v0.1.1 |  | A starting point for an application on the Crab framework |
| 2026-11-05 13:30:46 | [nobuhiko/eccube-cloud-logging](https://www.nuget.org/packages/nobuhiko%2Feccube-cloud-logging) | v0.1.0 | KIMOTO Nobuhiko | EC-CUBE を Cloud Run などで動かすときのログ（Cloud Logging の JSON・個人情報を伏せる・リクエストの trace）。Mon… |
| 2026-11-05 13:44:06 | [blutrixx/nativephp-geo-location](https://www.nuget.org/packages/blutrixx%2Fnativephp-geo-location) | v1.1.0 | Blutrixx | NativePHP Mobile plugin: location in the foreground and in the background. A fo… |
| 2026-11-05 13:46:47 | [js199069/laravel-persian-rag](https://www.nuget.org/packages/js199069%2Flaravel-persian-rag) | v0.1.0 | js199069 | Persian RAG for Laravel: OCR-aware extraction, hybrid pgvector search, role-bas… |
| 2026-11-05 13:52:56 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.16.0 |  | The skeleton application for the Laravel framework. |
| 2026-11-05 14:03:25 | [bdevs/supabase-laravel](https://www.nuget.org/packages/bdevs%2Fsupabase-laravel) | v0.1.0 | BlackDevs; Md Mahabubul Alam | Laravel package for integrating with Supabase (Auth, Storage, Edge Functions). |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
