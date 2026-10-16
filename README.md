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

## Latest list — 2026-10-16 19:20 UTC

New packages created between 2026-10-16 18:20 UTC and 2026-10-16 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T19-20-16-677931Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 18:29:25 | [ernestdefoe/club](https://www.nuget.org/packages/ernestdefoe%2Fclub) | v1.0.0 | Ernest Defoe | Book and watch clubs for Marquee titles: a monthly pick, a reading or watching… |
| 2026-10-16 18:33:49 | [ernestdefoe/shelf](https://www.nuget.org/packages/ernestdefoe%2Fshelf) | v1.0.0 | Ernest Defoe | Members rate, log and list the movies, shows, games, albums and books Marquee l… |
| 2026-10-16 18:58:17 | [attachmentav/virus-scan-sdk](https://www.nuget.org/packages/attachmentav%2Fvirus-scan-sdk) | v1.0.0 | widdix | An SDK to integrate virus and malware scan capabilities into PHP applications.… |
| 2026-10-16 18:58:46 | [x-laravel/federated-identity](https://www.nuget.org/packages/x-laravel%2Ffederated-identity) | v1.0.0 | Mehmet ÖĞMEN | Verify Google, Apple and any OpenID Connect ID token sent from mobile and singl… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
