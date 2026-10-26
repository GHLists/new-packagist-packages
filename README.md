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

## Latest list — 2026-10-26 22:18 UTC

New packages created between 2026-10-26 21:21 UTC and 2026-10-26 22:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-26T22-18-55-54736Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-26 21:23:38 | [wilycode/form](https://www.nuget.org/packages/wilycode%2Fform) | v0.1.0 | Simon Piter | Typed form fields, fieldsets and collections using independent filter/validator… |
| 2026-10-26 21:33:23 | [fast-forward/code-standards](https://www.nuget.org/packages/fast-forward%2Fcode-standards) | v0.1.0 | Felipe Sayão Lobato Abreu | Focused PHP style presets, syntax checks and changed-file automation. |
| 2026-10-26 21:37:56 | [tryhackx/flarum-homepage-blocks](https://www.nuget.org/packages/tryhackx%2Fflarum-homepage-blocks) | 2.11.0 | TryHackX | Customizable homepage blocks for tracker-style Flarum forums featuring dual sta… |
| 2026-10-26 21:38:11 | [samuelezoncada/monad](https://www.nuget.org/packages/samuelezoncada%2Fmonad) | v0.1.2 | Samuele Zoncada | A single-file PHP micro-framework. |
| 2026-10-26 21:43:15 | [wilycode/form-image-upload](https://www.nuget.org/packages/wilycode%2Fform-image-upload) | v0.1.0 | Simon Piter | Optional image upload metadata fieldset for WilyCode Form. |
| 2026-10-26 21:45:25 | [bugdeployer/horus-sdk](https://www.nuget.org/packages/bugdeployer%2Fhorus-sdk) | v0.4.0-beta.1 | bugdeployer | Bounded opt-in runtime capture for Horus |
| 2026-10-26 22:03:17 | [wilycode/jwt-token](https://www.nuget.org/packages/wilycode%2Fjwt-token) | v0.1.0 | Simon Piter | Minimal, strict HS256 JWT issuing and verification for PHP 8.4+ |
| 2026-10-26 22:09:01 | [data-health/data-health](https://www.nuget.org/packages/data-health%2Fdata-health) | v0.1.0 | Jascha Gerles | Check for inconsistencies in your data and fix them |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
