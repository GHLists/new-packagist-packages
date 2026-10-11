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

## Latest list — 2026-10-11 19:20 UTC

New packages created between 2026-10-11 18:21 UTC and 2026-10-11 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T19-20-13-237861Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 18:27:03 | [bkubicki/declarative-queue](https://www.nuget.org/packages/bkubicki%2Fdeclarative-queue) | 1.0 |  | Explicit, declarative queue arguments for Magento's MessageQueue framework |
| 2026-10-11 18:30:07 | [morivasaraki/mormap](https://www.nuget.org/packages/morivasaraki%2Fmormap) | v1.0.0 | Morteza VASARAKI | MorMap: image-based port anchors and editable orthogonal cable maps inside Libr… |
| 2026-10-11 18:38:46 | [vivutio/agency-pack](https://www.nuget.org/packages/vivutio%2Fagency-pack) | v0.1.0 | Ezekiel Mjema | What a travel agency of vivutio installs: the tickets it buys from carriers for… |
| 2026-10-11 18:48:15 | [jeffersongoncalves/laravel-brazil-holidays](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-brazil-holidays) | 1.0.0 | Jefferson Gonçalves | Brazilian national holidays for Laravel: holiday list per year, holiday and bus… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
