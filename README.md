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

## Latest list — 2026-11-08 18:20 UTC

New packages created between 2026-11-08 17:19 UTC and 2026-11-08 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T18-20-08-623447Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 17:27:47 | [jtech/dumper](https://www.nuget.org/packages/jtech%2Fdumper) | v0.1 | jauharimtikhan |  |
| 2026-11-08 17:28:59 | [roundly-consulting/imports-for-laravel](https://www.nuget.org/packages/roundly-consulting%2Fimports-for-laravel) | 1.0.0 | Andrej Mihaliak | Import CSV and XLSX files into Eloquent models: templates, column mapping, vali… |
| 2026-11-08 17:32:32 | [ernestdefoe/segue](https://www.nuget.org/packages/ernestdefoe%2Fsegue) | 1.0.0 | Ernest Defoe | Segue — a loading screen instead of the blank flash when your forum opens, with… |
| 2026-11-08 17:40:53 | [starbug/importer](https://www.nuget.org/packages/starbug%2Fimporter) | v0.9.0 | Ali Gangji | Starbug import pipeline. |
| 2026-11-08 17:42:33 | [roundly-consulting/safe-fetch-for-laravel](https://www.nuget.org/packages/roundly-consulting%2Fsafe-fetch-for-laravel) | 1.0.0 | Andrej Mihaliak | SSRF protection for Laravel's HTTP client: strict URL canonicalising, private a… |
| 2026-11-08 17:42:40 | [aisenseapi/aamio-sound](https://www.nuget.org/packages/aisenseapi%2Faamio-sound) | v0.1.0 | AI SENSE AS | Sound for aamio: play the write address of a scope as sound, so agents within e… |
| 2026-11-08 17:57:36 | [mistrfilda/redis](https://www.nuget.org/packages/mistrfilda%2Fredis) | v0.1.0 |  | Redis and Valkey connections, distributed locks and native PHP sessions with op… |
| 2026-11-08 18:16:29 | [bifrost-orbit/cms-sdk](https://www.nuget.org/packages/bifrost-orbit%2Fcms-sdk) | v0.2.0 |  | Read content from CMS Orbit: a PHP client for the delivery API, with SEO, sitem… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
