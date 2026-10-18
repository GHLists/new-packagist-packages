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

## Latest list — 2026-10-18 12:19 UTC

New packages created between 2026-10-18 11:21 UTC and 2026-10-18 12:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-18T12-19-29-440716Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-18 11:35:32 | [cryptolike/sdk](https://www.nuget.org/packages/cryptolike%2Fsdk) | v0.2.0 | CryptoLike team | Official server-side SDK for the CryptoLike merchant API: signed requests, auto… |
| 2026-10-18 11:35:33 | [laraveladmin/think-schedule](https://www.nuget.org/packages/laraveladmin%2Fthink-schedule) | 1.0.0 |  | Laravel-style task scheduler for ThinkPHP: define tasks in PHP and keep only on… |
| 2026-10-18 11:38:13 | [ehundu/andamio-multilingue](https://www.nuget.org/packages/ehundu%2Fandamio-multilingue) | v0.16.0 |  | Una web completa en dos idiomas (castellano y euskera) hecha con Ehundu, con su… |
| 2026-10-18 11:38:43 | [asyntai/cakephp-ai-chatbot](https://www.nuget.org/packages/asyntai%2Fcakephp-ai-chatbot) | 1.0.0 | Asyntai | Asyntai AI chatbot for CakePHP. Adds an AI chat assistant to your CakePHP app t… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
