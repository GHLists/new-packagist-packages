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

## Latest list — 2026-11-10 12:20 UTC

New packages created between 2026-11-10 11:23 UTC and 2026-11-10 12:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-10T12-20-13-323985Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-10 11:26:13 | [alnv/genai-bundle](https://www.nuget.org/packages/alnv%2Fgenai-bundle) | 0.1.0 | Alexander Naumov |  |
| 2026-11-10 11:30:51 | [rubeen/drk-dienstabende](https://www.nuget.org/packages/rubeen%2Fdrk-dienstabende) | v0.1.3 |  | Inhaltselement „Dienstabende“: zeigt Termine aus einer JSON-Adresse als Akkorde… |
| 2026-11-10 11:36:10 | [wika-group/sessionservice-for-laravel](https://www.nuget.org/packages/wika-group%2Fsessionservice-for-laravel) | 0.1.0 | WIKA Group | Handles the communication with the session service |
| 2026-11-10 11:48:43 | [voorhof/stickler-light](https://www.nuget.org/packages/voorhof%2Fstickler-light) | v1.9.1 |  | A starter kit for the Laravel framework. |
| 2026-11-10 12:12:16 | [elmphant/tui](https://www.nuget.org/packages/elmphant%2Ftui) | v0.1.0 | Wolfgang Klinger | The Elm Architecture for terminal UIs (TUI) in PHP |
| 2026-11-10 12:15:55 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.26.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
