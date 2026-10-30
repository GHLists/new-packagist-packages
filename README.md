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

## Latest list — 2026-10-30 07:20 UTC

New packages created between 2026-10-30 06:20 UTC and 2026-10-30 07:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T07-20-00-491685Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 06:47:39 | [zeyen/filse](https://www.nuget.org/packages/zeyen%2Ffilse) | v0.0.5 | zeyen | PHP client for the image-hosting / file-uploads gateway: upload, private URL, f… |
| 2026-10-30 07:10:04 | [mattfor/emoji-mixer](https://www.nuget.org/packages/mattfor%2Femoji-mixer) | v2.2.0 | MattFor | Get the URL of a Google Emoji Kitchen image for two emojis. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
