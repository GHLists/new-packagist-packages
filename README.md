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

## Latest list — 2026-11-13 23:20 UTC

New packages created between 2026-11-13 22:21 UTC and 2026-11-13 23:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T23-20-33-100647Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 22:28:32 | [marcodiperna/filament-queue-monitor](https://www.nuget.org/packages/marcodiperna%2Ffilament-queue-monitor) | v1.1.0 | Marco Di Perna | Code, job falliti e batch di Laravel nel pannello Filament, sulle tabelle stand… |
| 2026-11-13 22:40:29 | [codehq-dk/my-dashboard-url-monitor-widget](https://www.nuget.org/packages/codehq-dk%2Fmy-dashboard-url-monitor-widget) | 1.0.0 | Jesper Østergaard Jensen | Url monitor widget to be used in the CodeHq-dk Mydashboard project |
| 2026-11-13 22:57:41 | [koraitech/opentelemetry-php-extras](https://www.nuget.org/packages/koraitech%2Fopentelemetry-php-extras) | v0.2.0 |  | Extra OpenTelemetry auto-instrumentation for PHP: one span per Laravel event an… |
| 2026-11-13 23:00:40 | [polygonlab/facture-electronique-fr-outils](https://www.nuget.org/packages/polygonlab%2Ffacture-electronique-fr-outils) | v0.1.1 | PolygonLab | Lecture des factures électroniques CII, UBL et Factur-X et contrôle des mention… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
