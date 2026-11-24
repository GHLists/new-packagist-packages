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

## Latest list — 2026-11-24 08:19 UTC

New packages created between 2026-11-24 07:20 UTC and 2026-11-24 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-24T08-19-47-082237Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-24 07:25:32 | [designos/renderer-blade](https://www.nuget.org/packages/designos%2Frenderer-blade) | v0.1.0 |  | Server-side Blade renderer for DesignOS PageDocument data. |
| 2026-11-24 07:52:08 | [inertiaui/notifications](https://www.nuget.org/packages/inertiaui%2Fnotifications) | 1.0.1 | Pascal Baljet | Toasts and notifications for Laravel + Inertia.js |
| 2026-11-24 07:59:14 | [nobuhiko/twig](https://www.nuget.org/packages/nobuhiko%2Ftwig) | v1.34.0-p1 | Fabien Potencier; Twig Team;… | Twig 1.34.0 with security fixes backported, for EC-CUBE 3.0.x shops that cannot… |
| 2026-11-24 07:59:18 | [nobuhiko/symfony](https://www.nuget.org/packages/nobuhiko%2Fsymfony) | v2.7.52-p1 | Fabien Potencier; Symfony Com… | The Symfony 2.7 components EC-CUBE 3.0.18 ships (2.7.52) with security fixes ba… |
| 2026-11-24 07:59:21 | [nobuhiko/swiftmailer](https://www.nuget.org/packages/nobuhiko%2Fswiftmailer) | v5.4.12-p1 | Chris Corbyn; Fabien Potencier | Swift Mailer 5.4.12 with security fixes backported, for EC-CUBE 3.0.x shops tha… |
| 2026-11-24 07:59:25 | [nobuhiko/carbon](https://www.nuget.org/packages/nobuhiko%2Fcarbon) | 1.36.2-p1 | Brian Nesbitt | Carbon 1.36.2 with security fixes backported, for EC-CUBE 3.0.x shops that cann… |
| 2026-11-24 07:59:29 | [nobuhiko/random_compat](https://www.nuget.org/packages/nobuhiko%2Frandom_compat) | v1.4.3-p1 | Paragon Initiative Enterprises | random_compat 1.4.3 with security fixes backported, for EC-CUBE 3.0.x shops tha… |
| 2026-11-24 08:04:50 | [filefabrik/rfc9421](https://www.nuget.org/packages/filefabrik%2Frfc9421) | v1.10.1 | RT Filefabrik | Create and validate RFC 9421 HTTP Signatures for ActivityPub. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
