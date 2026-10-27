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

## Latest list — 2026-10-27 17:19 UTC

New packages created between 2026-10-27 16:18 UTC and 2026-10-27 17:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-27T17-19-37-552851Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-27 16:19:56 | [tryhackx/flarum-homepage-blocks](https://www.nuget.org/packages/tryhackx%2Fflarum-homepage-blocks) | 2.12.3 | TryHackX | Customizable homepage blocks for tracker-style Flarum forums featuring dual sta… |
| 2026-10-27 16:22:31 | [bernskiold/laravel-import-engine](https://www.nuget.org/packages/bernskiold%2Flaravel-import-engine) | v0.1.0 | Bernskiold; Erik Bernskiöld | Import CSV and Excel files into Laravel. Map the columns, preview the result, r… |
| 2026-10-27 16:29:02 | [letsdeploy/statamic-turnstile](https://www.nuget.org/packages/letsdeploy%2Fstatamic-turnstile) | 1.0.0 |  |  |
| 2026-10-27 16:30:16 | [agencenous/wp-ant-it](https://www.nuget.org/packages/agencenous%2Fwp-ant-it) | 0.0.3 | Bastien Ho | Manage an object oriented anthill in WordPress plugins. |
| 2026-10-27 16:47:30 | [karlmantle/core-security-hardening](https://www.nuget.org/packages/karlmantle%2Fcore-security-hardening) | 1.1.0 |  | Disables various seldom used features of WordPress to improve security. |
| 2026-10-27 17:04:15 | [particle-academy/change-council](https://www.nuget.org/packages/particle-academy%2Fchange-council) | v0.1.0 |  | A consumer-agent voting ledger for major package changes: a zero-dependency cha… |
| 2026-10-27 17:11:29 | [dainc007/laravel-discord-server](https://www.nuget.org/packages/dainc007%2Flaravel-discord-server) | v0.1.0 | Daniel Heinze | Manage a Discord server from Laravel: config, a test fake, rate limits shared t… |
| 2026-10-27 17:14:28 | [noehassiel/preview-bridge](https://www.nuget.org/packages/noehassiel%2Fpreview-bridge) | v0.1.0 | noehassiel | Lets a Laravel site be reviewed inside the noehassiel client portal: allows fra… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
