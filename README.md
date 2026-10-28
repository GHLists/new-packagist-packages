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

## Latest list — 2026-10-28 17:21 UTC

New packages created between 2026-10-28 16:21 UTC and 2026-10-28 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T17-21-42-548333Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 16:33:54 | [alecgarcia/laravel-ai-vertex](https://www.nuget.org/packages/alecgarcia%2Flaravel-ai-vertex) | v0.1.0 |  | A Google Vertex AI driver for the Laravel AI SDK, with Gemini text over generat… |
| 2026-10-28 16:55:55 | [psyao/kami](https://www.nuget.org/packages/psyao%2Fkami) | v0.1.0 | Steve Aguet | Psyao Kami: a Laravel and Filament CMS for developers, at home on shared hostin… |
| 2026-10-28 16:58:12 | [pushinbr/pam-native-notifications](https://www.nuget.org/packages/pushinbr%2Fpam-native-notifications) | v0.1.1 |  | Optional native notifications, conversation actions and push rendering for PAM… |
| 2026-10-28 16:58:12 | [pushinbr/pam-native-webview](https://www.nuget.org/packages/pushinbr%2Fpam-native-webview) | v0.1.1 |  | Optional hardened native WebView for PAM Native. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
