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

## Latest list — 2026-10-08 22:20 UTC

New packages created between 2026-10-08 21:21 UTC and 2026-10-08 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-08T22-20-03-175624Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-08 21:21:58 | [tey/mod](https://www.nuget.org/packages/tey%2Fmod) | v0.1.0 | Jasper Tey | Lightweight toolkit for modular development in Laravel. Choose or extend common… |
| 2026-10-08 21:38:38 | [hoceineel/filament-quick-action-dock](https://www.nuget.org/packages/hoceineel%2Ffilament-quick-action-dock) | v0.2.0 | Hoceine El Idrissi | A floating launcher for the Filament actions people reach for most, on every pa… |
| 2026-10-08 21:38:53 | [hoceineel/filament-undo-toast](https://www.nuget.org/packages/hoceineel%2Ffilament-undo-toast) | v0.2.0 | Hoceine El Idrissi | Gmail-style undo toasts for Filament delete, restore, edit and detach actions,… |
| 2026-10-08 21:39:03 | [hoceineel/filament-keyboard-shortcuts](https://www.nuget.org/packages/hoceineel%2Ffilament-keyboard-shortcuts) | v0.2.0 | Hoceine El Idrissi | A ? cheat sheet, Gmail-style navigation chords and keyboard table navigation fo… |
| 2026-10-08 21:40:04 | [daggerhartlab/daglab_paragraphs](https://www.nuget.org/packages/daggerhartlab%2Fdaglab_paragraphs) | 1.0.0 | Jonathan Daggerhart | Drupal module with reports and cleanup tools for paragraphs. |
| 2026-10-08 22:07:47 | [signlphp/laravel-valkyrie](https://www.nuget.org/packages/signlphp%2Flaravel-valkyrie) | v0.9.0 | Kim Eric Helle | Roles and abilities for Laravel — scoped grants, ownership rules, forbids that… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
