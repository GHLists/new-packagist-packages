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

## Latest list — 2026-10-15 22:20 UTC

New packages created between 2026-10-15 21:19 UTC and 2026-10-15 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-15T22-20-12-853698Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-15 21:30:59 | [1994/promo-bar-statamic](https://www.nuget.org/packages/1994%2Fpromo-bar-statamic) | v1.0.0 | 1994 | Promo bars for Statamic: scheduled, targeted announcement bars with call-to-act… |
| 2026-10-15 21:31:58 | [iranimij/openfilter](https://www.nuget.org/packages/iranimij%2Fopenfilter) | v1.0.0 | Iman Aboheydary | OpenFilter: layered navigation for Magento 2 and Hyvä. Multi-select filters wit… |
| 2026-10-15 21:32:01 | [iranimij/openfilter-hyva](https://www.nuget.org/packages/iranimij%2Fopenfilter-hyva) | v1.0.0 | Iman Aboheydary | OpenFilter render package for Hyvä themes: filter templates, one Alpine compone… |
| 2026-10-15 21:32:05 | [iranimij/openfilter-hyva-bundle](https://www.nuget.org/packages/iranimij%2Fopenfilter-hyva-bundle) | v1.0.0 | Iman Aboheydary | OpenFilter for Hyvä in one require: layered navigation for Magento 2 and Hyvä (… |
| 2026-10-15 21:54:06 | [pelock/lua-virtualizer](https://www.nuget.org/packages/pelock%2Flua-virtualizer) | 1.0.0 | Bartosz Wójcik | Lua Virtualizer Web API interface can help you obfuscate and protect Lua .lua s… |
| 2026-10-15 21:59:53 | [1994/back-in-stock-statamic](https://www.nuget.org/packages/1994%2Fback-in-stock-statamic) | v1.0.0 | 1994 | Back in stock alerts for Cargo: shoppers leave their email on a sold-out produc… |
| 2026-10-15 22:10:37 | [marcelofecchio/siscomex](https://www.nuget.org/packages/marcelofecchio%2Fsiscomex) | v0.1.0 | Marcelo Fecchio | SDK PHP 8.4 para a API Pública do Portal Único Siscomex: autenticação (IMPEXP),… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
