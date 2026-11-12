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

## Latest list — 2026-11-12 00:20 UTC

New packages created between 2026-11-11 23:21 UTC and 2026-11-12 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T00-20-42-07842Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-11 23:33:24 | [angelitosystems/pdf](https://www.nuget.org/packages/angelitosystems%2Fpdf) | v0.1.1 |  | HTML/CSS to PDF for Laravel without Chromium: a native Rust engine (angelito-pd… |
| 2026-11-11 23:44:24 | [pushinbr/pam-native-web](https://www.nuget.org/packages/pushinbr%2Fpam-native-web) | v1.48.0 |  | Compiles a PAM Native app to a static HTML/JS app for web-based TVs (Samsung Ti… |
| 2026-11-12 00:03:12 | [christianoerick/nfse-nacional](https://www.nuget.org/packages/christianoerick%2Fnfse-nacional) | v0.1.0 | Christiano Erick | NFS-e Nacional (Sefin Nacional / ADN) em PHP puro, sem framework: DPS completa… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
