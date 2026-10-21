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

## Latest list — 2026-10-21 19:19 UTC

New packages created between 2026-10-21 18:19 UTC and 2026-10-21 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-21T19-19-05-262247Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-21 18:33:38 | [exactstudios/framework](https://www.nuget.org/packages/exactstudios%2Fframework) | v1.0.0 | Exact Studios | Exact Studios framework |
| 2026-10-21 18:52:06 | [bautrukevich/fractional-indexing](https://www.nuget.org/packages/bautrukevich%2Ffractional-indexing) | v1.0.0 | Manolis Dermitzakis | Fractional Indexing implementation in PHP |
| 2026-10-21 19:13:46 | [ahmedibrahimyassindev/tamara-php-sdk](https://www.nuget.org/packages/ahmedibrahimyassindev%2Ftamara-php-sdk) | v1.0.0 | Ahmed Ibrahim Yassin | Modern, framework-agnostic PHP SDK for Tamara Buy Now Pay Later (BNPL) Payment… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
