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

## Latest list — 2026-10-11 07:21 UTC

New packages created between 2026-10-11 06:19 UTC and 2026-10-11 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T07-21-28-697972Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 06:28:16 | [smaily/module-connect-hyva](https://www.nuget.org/packages/smaily%2Fmodule-connect-hyva) | 3.0.0-rc11 | Smaily | Hyvä theme compatibility for Smaily Connect (Smaily_Connect): framework-free br… |
| 2026-10-11 06:56:56 | [php-concept/skeleton-2](https://www.nuget.org/packages/php-concept%2Fskeleton-2) | v1.0.1 |  | FormSite-level starter for PHP Concept 2 — thin Core, opt-in Extensions, explic… |
| 2026-10-11 07:13:29 | [astral-php/astral-shipping](https://www.nuget.org/packages/astral-php%2Fastral-shipping) | 0.1.0 | astral-php | Frais de port multi-options pour Astral : forfait, barèmes poids/pays, Colissim… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
