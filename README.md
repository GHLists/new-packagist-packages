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

## Latest list — 2026-11-05 18:20 UTC

New packages created between 2026-11-05 17:19 UTC and 2026-11-05 18:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-05T18-20-25-959528Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-05 17:22:20 | [jlorente/laravel-appsflyer](https://www.nuget.org/packages/jlorente%2Flaravel-appsflyer) | 1.0.0 | José Lorente | Laravel 5.6 integration for the Jlorente Appsflyer package. |
| 2026-11-05 17:22:21 | [php-io-extensions/fontconfig](https://www.nuget.org/packages/php-io-extensions%2Ffontconfig) | v0.11.0 | Project Saturn Studios, LLC | 1:1 PHP bindings of fontconfig: configuration, patterns, font matching and sort… |
| 2026-11-05 17:27:00 | [isapp/filament-firebase-auth](https://www.nuget.org/packages/isapp%2Ffilament-firebase-auth) | v5.0.0 | ISAPP; ISAP OÜ | Firebase Authentication for Filament panels through Laravel auth contracts. |
| 2026-11-05 17:28:53 | [beliq/shopware-beliq](https://www.nuget.org/packages/beliq%2Fshopware-beliq) | 0.1.0 | beliq | Generate compliant EN 16931 e-invoices from Shopware orders through the beliq A… |
| 2026-11-05 17:36:25 | [nowo-tech/slack-kit-bundle](https://www.nuget.org/packages/nowo-tech%2Fslack-kit-bundle) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Slack for Symfony: a hardened Web API client, signed interactions and Events AP… |
| 2026-11-05 17:54:13 | [larevio/persian-providers](https://www.nuget.org/packages/larevio%2Fpersian-providers) | 1.0.0 | larevio | Laravel integrations for Iranian payment, SMS, inquiry, and exchange providers |
| 2026-11-05 18:07:05 | [nandordudas/state-machine](https://www.nuget.org/packages/nandordudas%2Fstate-machine) | v3.0.0 |  | A small, strictly typed finite state machine for PHP (inspired by xstate.js and… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
