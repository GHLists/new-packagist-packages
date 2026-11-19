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

## Latest list — 2026-11-19 12:22 UTC

New packages created between 2026-11-19 11:19 UTC and 2026-11-19 12:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-19T12-22-22-949171Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-19 11:37:12 | [daika7ana/dragonstar-php-sdk](https://www.nuget.org/packages/daika7ana%2Fdragonstar-php-sdk) | v1.0.0 | Dan-Radu Pana | Typed PHP SDK for the Dragon Star Courier API. |
| 2026-11-19 11:44:33 | [inspirecz/dresscode-standard](https://www.nuget.org/packages/inspirecz%2Fdresscode-standard) | v1.0.0 | INSPIRE CZ s.r.o. | INSPIRE coding standard for DressCode: presets translated from inspirecz/coding… |
| 2026-11-19 11:52:48 | [justinholtweb/craft-chisel](https://www.nuget.org/packages/justinholtweb%2Fcraft-chisel) | 6.0.0-beta.1 | Justin Holt | Run allowlisted Artisan commands from the Craft CP — forms built from each comm… |
| 2026-11-19 12:07:04 | [daika7ana/fancourier-php-sdk](https://www.nuget.org/packages/daika7ana%2Ffancourier-php-sdk) | v1.0.0 | Dan-Radu Pana | Typed PHP SDK for the FAN Courier API. |
| 2026-11-19 12:16:38 | [justinholtweb/craft-dipstick](https://www.nuget.org/packages/justinholtweb%2Fcraft-dipstick) | 6.0.0-beta.1 | Justin Holt | Check the engine before you run Craft on Octane: finds state that leaks between… |
| 2026-11-19 12:18:47 | [ozioma/otp](https://www.nuget.org/packages/ozioma%2Fotp) | 1.0.1 |  | Framework-independent one-time password generation and verification for PHP, wi… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
