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

## Latest list — 2026-10-31 05:19 UTC

New packages created between 2026-10-31 04:18 UTC and 2026-10-31 05:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T05-19-38-513934Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 04:25:32 | [hibira-io/filament-approvals](https://www.nuget.org/packages/hibira-io%2Ffilament-approvals) | v0.1.0 | Hibira | A live Filament inbox for Laravel AI SDK tool approvals: your agent pauses befo… |
| 2026-10-31 04:28:09 | [hibira-io/filament-support](https://www.nuget.org/packages/hibira-io%2Ffilament-support) | v0.1.0 | Hibira | AI live chat support for Filament: a chat widget for your website, answered fir… |
| 2026-10-31 04:28:46 | [larasell-dev/phpstan-rules](https://www.nuget.org/packages/larasell-dev%2Fphpstan-rules) | v0.1.0 | Nils Haberkamp | PHPStan rules shared by the Larasell packages |
| 2026-10-31 04:30:44 | [osopostal/laravel](https://www.nuget.org/packages/osopostal%2Flaravel) | v0.0.1 |  | Integración oficial de OsoPostal para Laravel: cliente de la API de códigos pos… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
