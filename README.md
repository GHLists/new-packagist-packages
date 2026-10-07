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

## Latest list — 2026-10-07 18:21 UTC

New packages created between 2026-10-07 17:21 UTC and 2026-10-07 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T18-21-58-121722Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 17:23:10 | [mdakashhossain1/arknox-monitor](https://www.nuget.org/packages/mdakashhossain1%2Farknox-monitor) | v1.1.0 |  | Usage tracking, billing and payment enforcement for Laravel sites (requests, Cl… |
| 2026-10-07 18:01:45 | [fusio/adapter-ftp](https://www.nuget.org/packages/fusio%2Fadapter-ftp) | v0.1.0 | Christoph Kappestein | Adapter to serve files via FTP |
| 2026-10-07 18:02:24 | [dereuromark/cakephp-passkeys](https://www.nuget.org/packages/dereuromark%2Fcakephp-passkeys) | 0.1.0 | Mark Scherer | Public-quality passkey / WebAuthn authentication plugin for CakePHP 5 |
| 2026-10-07 18:06:12 | [mammaaddeveloper/laravel-flex-settings](https://www.nuget.org/packages/mammaaddeveloper%2Flaravel-flex-settings) | v0.1.0 | mammaadDeveloper | A lovely package for managing Laravel settings. |
| 2026-10-07 18:06:28 | [crawlora/fotmob](https://www.nuget.org/packages/crawlora%2Ffotmob) | v0.1.4 |  | FotMob client for the Crawlora hosted API |
| 2026-10-07 18:06:34 | [crawlora/youtube](https://www.nuget.org/packages/crawlora%2Fyoutube) | v0.1.4 |  | YouTube client for the Crawlora hosted API |
| 2026-10-07 18:08:54 | [crawlora/sofascore](https://www.nuget.org/packages/crawlora%2Fsofascore) | v0.2.0 |  | SofaScore client for the Crawlora hosted API |
| 2026-10-07 18:09:24 | [crawlora/flashscore](https://www.nuget.org/packages/crawlora%2Fflashscore) | v0.2.0 |  | Flashscore client for the Crawlora hosted API |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
