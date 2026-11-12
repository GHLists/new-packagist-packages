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

## Latest list — 2026-11-12 18:21 UTC

New packages created between 2026-11-12 17:22 UTC and 2026-11-12 18:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T18-21-15-140708Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 17:35:11 | [momotombo/nativephp-alarms](https://www.nuget.org/packages/momotombo%2Fnativephp-alarms) | v0.1.0 | Momotombo Devs | Exact, alarm-clock-grade alarms for NativePHP Mobile on Android: foreground pla… |
| 2026-11-12 17:38:10 | [sad_spirit/el2sql](https://www.nuget.org/packages/sad_spirit%2Fel2sql) | v0.1.0 | Alexey Borzov | Translator from Symfony's ExpressionLanguage to Postgres SQL dialect |
| 2026-11-12 17:53:55 | [ergebnis/differ](https://www.nuget.org/packages/ergebnis%2Fdiffer) | 1.0.0 | Andreas Möller | Provides a composer package with a differ for creating a unified diff of two st… |
| 2026-11-12 18:01:15 | [nowo-tech/short-link-bundle](https://www.nuget.org/packages/nowo-tech%2Fshort-link-bundle) | v0.1.0 | Héctor Franco Aceituno; Nowo.… | Short links for Symfony: per-tenant short codes behind a public stateless redir… |
| 2026-11-12 18:05:46 | [generoi/gds-monitoring](https://www.nuget.org/packages/generoi%2Fgds-monitoring) | v1.0.0 | Genero | Logs what a person should look at on a WordPress site (lost form submissions, f… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
