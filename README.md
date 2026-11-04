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

## Latest list — 2026-11-04 15:19 UTC

New packages created between 2026-11-04 14:20 UTC and 2026-11-04 15:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T15-19-51-354828Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 14:26:12 | [jinganix/pbwire](https://www.nuget.org/packages/jinganix%2Fpbwire) | v0.1.1 | jinganix | Dynamic protobuf over the pbwire C ABI, schema at runtime, no generated code |
| 2026-11-04 14:26:59 | [codebrainbv/omnikassapayment](https://www.nuget.org/packages/codebrainbv%2Fomnikassapayment) | 1.2.3 |  | Accepting payments with Rabo Smart Pay |
| 2026-11-04 14:50:31 | [itmosoft/laravel-checkout](https://www.nuget.org/packages/itmosoft%2Flaravel-checkout) | v1.0.1 |  | A reusable Laravel checkout orchestration package with address snapshots, cart… |
| 2026-11-04 14:54:59 | [pharaonic/laravel-likes](https://www.nuget.org/packages/pharaonic%2Flaravel-likes) | 13.0.1 | Moamen Eltouny (Raggi) | Polymorphic likes for Laravel Eloquent models, with database-enforced uniquenes… |
| 2026-11-04 14:55:50 | [pronamic/pronamic-pay-wp-icons](https://www.nuget.org/packages/pronamic%2Fpronamic-pay-wp-icons) | v1.0.0 | Pronamic; Remco Tolsma | WordPress icon collection with payment method icons by Pronamic Pay. |
| 2026-11-04 14:56:48 | [considbrs-webdev/modularity-simpleview-events](https://www.nuget.org/packages/considbrs-webdev%2Fmodularity-simpleview-events) | v1.0.0 | Consid | Modularity Simpleview Events Module |
| 2026-11-04 14:59:45 | [itmosoft/laravel-orders](https://www.nuget.org/packages/itmosoft%2Flaravel-orders) | v1.0.1 |  | Order management for Laravel applications with immutable item snapshots and aud… |
| 2026-11-04 15:03:17 | [nandordudas/state-machine](https://www.nuget.org/packages/nandordudas%2Fstate-machine) | v2.0.0 |  | A small, strictly typed finite state machine for PHP (inspired by xstate.js and… |
| 2026-11-04 15:17:29 | [romain-genin/symfony-starter](https://www.nuget.org/packages/romain-genin%2Fsymfony-starter) | v1.0.1 | Romain Genin | Starter Symfony 8 : Tailwind CSS v4, Alpine.js, Turbo, Twig Components, EasyAdm… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
