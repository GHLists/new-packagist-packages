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

## Latest list — 2026-10-29 17:21 UTC

New packages created between 2026-10-29 16:20 UTC and 2026-10-29 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T17-21-05-915318Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 16:44:03 | [ark4ne/openapi-writer](https://www.nuget.org/packages/ark4ne%2Fopenapi-writer) | v1.0.0 |  | Framework-agnostic, fluent and immutable PHP builder for OpenAPI 3.0, 3.1 and 3… |
| 2026-10-29 16:45:27 | [waynestate/weld](https://www.nuget.org/packages/waynestate%2Fweld) | 0.1.0 |  | The Wayne State app stack, welded into one application. |
| 2026-10-29 16:59:36 | [silarhi/cap-bundle](https://www.nuget.org/packages/silarhi%2Fcap-bundle) | v0.1.0 | SILARHI | Cap CAPTCHA (trycap.dev) for Symfony forms: a self-hosted, proof-of-work reCAPT… |
| 2026-10-29 17:02:54 | [astral-php/astral-forum](https://www.nuget.org/packages/astral-php%2Fastral-forum) | 0.1.0 |  | Astral Forum — forums, sujets, posts et FAQ modérée (create-project starter 2.0) |
| 2026-10-29 17:05:01 | [wyxos/laravel-authentication](https://www.nuget.org/packages/wyxos%2Flaravel-authentication) | 0.2.0 |  | Switchable authentication history, new-device alerts and selected-recipient log… |
| 2026-10-29 17:08:47 | [betocampoy/champs-cron-monitor](https://www.nuget.org/packages/betocampoy%2Fchamps-cron-monitor) | v0.1.0 | Beto Campoy | Monitoramento das rotinas do cron para projetos Symfony: wrapper com trava e lo… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
