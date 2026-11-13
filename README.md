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

## Latest list — 2026-11-13 22:21 UTC

New packages created between 2026-11-13 21:20 UTC and 2026-11-13 22:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T22-21-29-564316Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 21:34:01 | [polygonlab/mcp-php-kit](https://www.nuget.org/packages/polygonlab%2Fmcp-php-kit) | v0.1.0 | PolygonLab | Build MCP (Model Context Protocol) servers in plain PHP, with an optional Cloud… |
| 2026-11-13 21:37:03 | [tornado-engine/chat](https://www.nuget.org/packages/tornado-engine%2Fchat) | v0.1.0 |  | Tornado Engine module: talk with Claude from the website, and have it build new… |
| 2026-11-13 22:02:02 | [papercut/math](https://www.nuget.org/packages/papercut%2Fmath) | v0.11.0 | One Learning Community | Math layout for PHP: fractions, roots, scripts and stretchy delimiters from an… |
| 2026-11-13 22:03:59 | [letterncms/youtube](https://www.nuget.org/packages/letterncms%2Fyoutube) | 0.1.0 |  | A YouTube block that shows the video’s poster and loads YouTube only when a vis… |
| 2026-11-13 22:04:33 | [letterncms/spotify](https://www.nuget.org/packages/letterncms%2Fspotify) | 0.1.0 |  | A Spotify block: a track, album, playlist, artist, podcast episode or show with… |
| 2026-11-13 22:12:42 | [letterncms/starter](https://www.nuget.org/packages/letterncms%2Fstarter) | 0.1.0 |  | A complete site to make your own: a home page, work, a journal, about and conta… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
