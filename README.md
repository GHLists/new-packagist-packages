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

## Latest list — 2026-10-14 02:19 UTC

New packages created between 2026-10-14 01:22 UTC and 2026-10-14 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T02-19-52-122407Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 01:32:01 | [setechsolutions/php-whois](https://www.nuget.org/packages/setechsolutions%2Fphp-whois) | 4.2.0 | Sergey Sedyshev; SETechSoluti… | Drop-in replacement for io-developer/php-whois: parsed and raw domain lookups o… |
| 2026-10-14 01:36:54 | [jeffersongoncalves/filament-cnpj-field](https://www.nuget.org/packages/jeffersongoncalves%2Ffilament-cnpj-field) | 3.0.0 | Jefferson Gonçalves | The Filament CNPJ Field is a custom input component for Brazilian company regis… |
| 2026-10-14 02:00:52 | [digiemp/laravel-boost-command-code](https://www.nuget.org/packages/digiemp%2Flaravel-boost-command-code) | v0.0.1 |  | Command Code agent for Laravel Boost. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
