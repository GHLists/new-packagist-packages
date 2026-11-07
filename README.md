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

## Latest list — 2026-11-07 19:19 UTC

New packages created between 2026-11-07 18:21 UTC and 2026-11-07 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-07T19-19-29-958208Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-07 18:55:35 | [codehq-dk/my-dashboard-widget-tester](https://www.nuget.org/packages/codehq-dk%2Fmy-dashboard-widget-tester) | 1.0.0 | Jesper Østergaard Jensen | Mydashboard widget tester for development of new widgets |
| 2026-11-07 18:57:27 | [noldors/oauth2-jwt-bearer](https://www.nuget.org/packages/noldors%2Foauth2-jwt-bearer) | v0.1.0 |  | RFC 7523 JWT Bearer Grant for League OAuth2 Server with optional Laravel Passpo… |
| 2026-11-07 19:12:35 | [dskripchenko/laravel-llm](https://www.nuget.org/packages/dskripchenko%2Flaravel-llm) | v0.1.0 | Denis Skripchenko | Local LLMs for Laravel through OpenAI-compatible APIs (Ollama, vLLM, LM Studio,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
