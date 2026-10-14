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

## Latest list — 2026-10-14 21:20 UTC

New packages created between 2026-10-14 20:22 UTC and 2026-10-14 21:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T21-20-59-516775Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 20:28:59 | [directorytree/screenshot](https://www.nuget.org/packages/directorytree%2Fscreenshot) | v1.0.0 | Steve Bauman | Create browser screenshots with PHP and Laravel. |
| 2026-10-14 20:52:38 | [projectsaturnstudios/starlight-inertia](https://www.nuget.org/packages/projectsaturnstudios%2Fstarlight-inertia) | 0.10.0 | Angel Gonzalez | A Starlight-shaped documentation theme for Laravel + Inertia (Vue): tokens, chr… |
| 2026-10-14 21:01:39 | [yasser-elgammal/green-ai-assistant](https://www.nuget.org/packages/yasser-elgammal%2Fgreen-ai-assistant) | v1.0.0 | Yasser Elgammal | Green Framework AI Assistant Package |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
