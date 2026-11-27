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

## Latest list — 2026-11-27 17:19 UTC

New packages created between 2026-11-27 16:19 UTC and 2026-11-27 17:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T17-19-39-638954Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 16:24:36 | [abolaradev/geo-guard](https://www.nuget.org/packages/abolaradev%2Fgeo-guard) | v1.0.0 | abolaradev | GeoGuard is a Laravel package for IP geolocation, visitor profiling, and geogra… |
| 2026-11-27 16:35:41 | [bootcndev/bootcn](https://www.nuget.org/packages/bootcndev%2Fbootcn) | v0.6.1 |  | The bootcn CLI for PHP and Laravel projects, no Node.js needed: install copy-pa… |
| 2026-11-27 16:36:40 | [kariricode/http](https://www.nuget.org/packages/kariricode%2Fhttp) | v4.0.0 | Walmir Silva | PSR-7, PSR-15 and PSR-17 for PHP 8.4: validated messages, a middleware dispatch… |
| 2026-11-27 16:42:05 | [yuccastream/tuna-sdk-php](https://www.nuget.org/packages/yuccastream%2Ftuna-sdk-php) | v0.1.0 | tuna.am authors | Expose local HTTP and TCP services through tuna.am tunnels |
| 2026-11-27 16:50:28 | [agentisend/symfony-mailer](https://www.nuget.org/packages/agentisend%2Fsymfony-mailer) | v0.1.0 | AgentiSend | Symfony Mailer transport that posts each message to POST /emails. DSNs: agentis… |
| 2026-11-27 17:01:29 | [nubos/starterkit](https://www.nuget.org/packages/nubos%2Fstarterkit) | v1.56.0 |  | A Laravel starter kit for multi-tenant business applications. Start with teams,… |
| 2026-11-27 17:03:48 | [mignuti/drupal-chatbot](https://www.nuget.org/packages/mignuti%2Fdrupal-chatbot) | v1.0.0 | Mignuti Media | Mignuti Chatbot for Drupal: AI chatbot trained on your own content, added to ev… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
