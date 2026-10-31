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

## Latest list — 2026-10-31 14:20 UTC

New packages created between 2026-10-31 13:19 UTC and 2026-10-31 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T14-20-48-435181Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 13:23:32 | [rapttor/yii2-metadata](https://www.nuget.org/packages/rapttor%2Fyii2-metadata) | v1.0.0 | Rapttor | Yii2 component for per-record metadata kept as JSON in one shared table (key, r… |
| 2026-10-31 13:28:07 | [ryzecompany/invmenu](https://www.nuget.org/packages/ryzecompany%2Finvmenu) | v4.7.5 | Muqsit; RyzeCompany | Virtual inventory API for multiversion RyzeMP |
| 2026-10-31 13:41:19 | [futuraweb/contao-backend-suite](https://www.nuget.org/packages/futuraweb%2Fcontao-backend-suite) | v2.1.0 | Dinko Skopljak | Backend-Werkzeuge für Contao 5 – ID-/Alias-Suche, Style-Selector für CSS-Klasse… |
| 2026-10-31 13:47:05 | [jaocero/conversational-forms](https://www.nuget.org/packages/jaocero%2Fconversational-forms) | v0.9.0 | Jay-Are Ocero | Typeform-style conversational forms for Filament. One question at a time, fully… |
| 2026-10-31 13:50:11 | [routegroup/php-ing-pay](https://www.nuget.org/packages/routegroup%2Fphp-ing-pay) | v1.0.0 | Kajetan Nobel | ING Pay payment gateway client for plain PHP |
| 2026-10-31 13:52:56 | [routegroup/laravel-ing-pay](https://www.nuget.org/packages/routegroup%2Flaravel-ing-pay) | v1.0.0 | Kajetan Nobel | Laravel integration for the ING Pay payment gateway |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
