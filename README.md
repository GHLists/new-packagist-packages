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

## Latest list — 2026-11-21 18:21 UTC

New packages created between 2026-11-21 17:21 UTC and 2026-11-21 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T18-21-48-393595Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 17:30:23 | [filertia/panel](https://www.nuget.org/packages/filertia%2Fpanel) | v0.4.0 | Pol Cámara | Resource-driven admin panels for Laravel, Inertia, Vue 3, and Tailwind CSS 4 |
| 2026-11-21 17:31:08 | [kongono/framework](https://www.nuget.org/packages/kongono%2Fframework) | v1.0.0 | Anthony Iovanna | A modern, zero-legacy PHP 8.5+ application framework built from the ground up w… |
| 2026-11-21 17:34:19 | [mopux/mopux-php](https://www.nuget.org/packages/mopux%2Fmopux-php) | v0.1.1 | Mopux | Official PHP client for the Mopux API, with first-class Laravel integration. |
| 2026-11-21 17:55:37 | [sinemacula/laravel-iam](https://www.nuget.org/packages/sinemacula%2Flaravel-iam) | v0.1.0 | Ben Carey | Identity and access management for Laravel: installs the authentication, author… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
