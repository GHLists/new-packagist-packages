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

## Latest list — 2026-11-07 14:19 UTC

New packages created between 2026-11-07 13:19 UTC and 2026-11-07 14:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T14-19-35-167324Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 13:21:13 | [clesson-de/silverstripe-codeguard](https://www.nuget.org/packages/clesson-de%2Fsilverstripe-codeguard) | 0.0.1 |  | A read-only quality and security gate for SilverStripe modules and applications. |
| 2026-11-07 13:25:20 | [ahmedsalheia/pyhp](https://www.nuget.org/packages/ahmedsalheia%2Fpyhp) | v0.1.0 | Ahmed Salheia | Use Python libraries (pandas, NumPy, ...) from PHP through a persistent Python… |
| 2026-11-07 13:27:38 | [maco-studios/hephaestus](https://www.nuget.org/packages/maco-studios%2Fhephaestus) | v0.0.20 | Marcos "Marcão" Aurelio | An interactive Composer project factory for standalone Mage-OS projects. |
| 2026-11-07 14:09:40 | [tualo/modsecuritylog](https://www.nuget.org/packages/tualo%2Fmodsecuritylog) | 1.0.1 | Thomas Hoffmann | ModSecurity Audit-Log Viewer for tualo office |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
