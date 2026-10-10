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

## Latest list — 2026-10-10 17:20 UTC

New packages created between 2026-10-10 16:20 UTC and 2026-10-10 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-10T17-20-04-446919Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-10 16:21:29 | [roadrunner/symfony-lock-driver](https://www.nuget.org/packages/roadrunner%2Fsymfony-lock-driver) | 1.3.0 | Pavel Buchnev; Alexander Stri… | Symfony Lock store backed by the RoadRunner lock plugin: use RoadRunner distrib… |
| 2026-10-10 16:23:19 | [pivotphp/core-routing](https://www.nuget.org/packages/pivotphp%2Fcore-routing) | v2.2.1 | Caio Alberto Fernandes | Simple, focused routing engine for PivotPHP - Express.js-inspired API (PSR-7) |
| 2026-10-10 16:24:33 | [roadrunner/tcp](https://www.nuget.org/packages/roadrunner%2Ftcp) | 4.3.0 | Anton Titov; Pavel Buchnev; A… | PHP worker for the RoadRunner TCP plugin: handle raw TCP connection events and… |
| 2026-10-10 16:26:04 | [runlight/runlight](https://www.nuget.org/packages/runlight%2Frunlight) | v0.1.0 |  | Privacy friendly web analytics that lives inside your PHP app. Mount a route, a… |
| 2026-10-10 16:36:05 | [reinfyteam/discordwebhookapi](https://www.nuget.org/packages/reinfyteam%2Fdiscordwebhookapi) | 2.0.0 |  | A PocketMine-MP Virion to easily send messages via Discord Webhooks |
| 2026-10-10 16:41:53 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.5.5 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-10 16:54:05 | [itxshakil/aadhaar-offline](https://www.nuget.org/packages/itxshakil%2Faadhaar-offline) | v0.1.0 | Shakil Alam | Read and verify Aadhaar Offline e-KYC (share-code ZIP / signed XML) and Secure… |
| 2026-10-10 16:56:00 | [b44x/edoreczenia](https://www.nuget.org/packages/b44x%2Fedoreczenia) | v0.2.1 | Michell Hoduń | Unofficial, framework-agnostic PHP SDK for the Polish e-Doręczenia (e-Delivery)… |
| 2026-10-10 17:13:27 | [rasuvaeff/schema](https://www.nuget.org/packages/rasuvaeff%2Fschema) | v0.1.0 | Victor Razuvaev | Schema-as-code combinators: runtime validation, property-based generators and J… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
