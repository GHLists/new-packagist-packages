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

## Latest list — 2026-10-16 11:22 UTC

New packages created between 2026-10-16 10:19 UTC and 2026-10-16 11:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T11-22-05-520003Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 10:32:45 | [manasija/drishti-sdk](https://www.nuget.org/packages/manasija%2Fdrishti-sdk) | v1.0.0 | Manasija | PHP client for the Drishti API (/v1): Indian stock market news, filings, earnin… |
| 2026-10-16 10:48:53 | [cap-rel/dolibarr-module-tests](https://www.nuget.org/packages/cap-rel%2Fdolibarr-module-tests) | v1.0.1 |  | Shared PHPUnit harness (HTTP and integration) and generic tests for Dolibarr mo… |
| 2026-10-16 10:59:59 | [mykholy/laravel-failurelab](https://www.nuget.org/packages/mykholy%2Flaravel-failurelab) | v1.0.0 | Ahmed El-Kholy | Deterministic fault-injection and delivery-replay assertions for Laravel integr… |
| 2026-10-16 11:05:44 | [thedomeffm/email-canonicalizer](https://www.nuget.org/packages/thedomeffm%2Femail-canonicalizer) | v1.0.0 | Domenic G. | Canonicalize addresses at public email providers (Gmail, Outlook, Proton, Fastm… |
| 2026-10-16 11:05:51 | [maximal/hyperloglog](https://www.nuget.org/packages/maximal%2Fhyperloglog) | v1.0 | maximal | Set cardinality estimator using the HyperLogLog algorithm |
| 2026-10-16 11:13:28 | [gia/gsdd](https://www.nuget.org/packages/gia%2Fgsdd) | v1.0.0 | Gia | Support to your Spec-Driven Development sessions in your own Laravel app. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
