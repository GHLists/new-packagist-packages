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

## Latest list — 2026-10-10 11:21 UTC

New packages created between 2026-10-10 10:20 UTC and 2026-10-10 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T11-21-48-331151Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 10:28:54 | [jamesforsyth/laravel-uk-kyb-edge](https://www.nuget.org/packages/jamesforsyth%2Flaravel-uk-kyb-edge) | v1.0.0 | James Forsyth | Sub-20ms UK Companies House address sanitization, geocoding, and director KYB f… |
| 2026-10-10 10:34:45 | [duva-mail/symfony-mailer](https://www.nuget.org/packages/duva-mail%2Fsymfony-mailer) | v0.1.0 | 9573-4562 Québec inc. | Symfony Mailer transport for Duva, the transactional email API hosted in Canada. |
| 2026-10-10 10:58:12 | [codeconjure/foxpost](https://www.nuget.org/packages/codeconjure%2Ffoxpost) | 0.1.0 |  | FoxPost WebAPI protokoll-kliens — keretrendszer-független, PSR-18 alapon. |
| 2026-10-10 11:04:09 | [codeconjure/foxpost-sylius-plugin](https://www.nuget.org/packages/codeconjure%2Ffoxpost-sylius-plugin) | 0.1.0 |  | FoxPost szállítási integráció Syliushoz: csomagfeladás, címke, nyomkövetés. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
