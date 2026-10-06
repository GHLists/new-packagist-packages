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

## Latest list — 2026-10-06 15:21 UTC

New packages created between 2026-10-06 14:22 UTC and 2026-10-06 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T15-21-52-473265Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-06 14:25:11 | [vortech/laravel-stash](https://www.nuget.org/packages/vortech%2Flaravel-stash) | v1.0.0 | Mate Papp | Store and retrieve loose, non-sensitive values in a file, a database or any cus… |
| 2026-10-06 14:26:37 | [bartollo/pipeline-kit](https://www.nuget.org/packages/bartollo%2Fpipeline-kit) | v1.0.0 |  | Artisan command that installs/merges the Claude Code + Sloppy + Laravel Boost q… |
| 2026-10-06 15:00:24 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.14 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |
| 2026-10-06 15:06:03 | [mage2kishan/module-advanced-contact-us](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-contact-us) | 1.1.12 |  | Advanced Contact Us Page - Custom fields, bot protection, submission management… |
| 2026-10-06 15:10:05 | [se7enxweb/sevenx_authentication_2fa](https://www.nuget.org/packages/se7enxweb%2Fsevenx_authentication_2fa) | v1.0.2 | 7x | Two-factor authentication (TOTP / email OTP) and OAuth social-login handler ske… |
| 2026-10-06 15:10:18 | [ernestdefoe/manticore](https://www.nuget.org/packages/ernestdefoe%2Fmanticore) | 0.1.0 | Ernest Defoe | Light, typo-tolerant Manticore Search driver for Flarum 2 — free and MIT. |
| 2026-10-06 15:10:58 | [mage2kishan/module-dynamic-forms](https://www.nuget.org/packages/mage2kishan%2Fmodule-dynamic-forms) | 1.2.10 |  | Dynamic Forms module for Magento 2 - Create and manage custom forms with drag-a… |
| 2026-10-06 15:11:27 | [ernestdefoe/sonic](https://www.nuget.org/packages/ernestdefoe%2Fsonic) | 0.1.0 | Ernest Defoe | A light search driver for Flarum 2, backed by Sonic, the tiny Rust search backe… |
| 2026-10-06 15:17:34 | [mage2kishan/module-blog](https://www.nuget.org/packages/mage2kishan%2Fmodule-blog) | 1.3.13 | Kishan Savaliya | Panth_Blog - SEO-grade blog module for Magento 2 with first-class AEO/AIO suppo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
