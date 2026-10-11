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

## Latest list — 2026-10-11 10:21 UTC

New packages created between 2026-10-11 09:20 UTC and 2026-10-11 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T10-21-48-761978Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 09:21:17 | [inupress/theme-default](https://www.nuget.org/packages/inupress%2Ftheme-default) | v0.1.0 |  | The default Inupress theme: a clean starting point built on Tailwind CSS and Al… |
| 2026-10-11 09:47:54 | [robyajo/pasak](https://www.nuget.org/packages/robyajo%2Fpasak) | v1.0.2 | Roby | Pasak - enterprise-grade headless self-hosted WAF, threat detection engine, zer… |
| 2026-10-11 09:51:39 | [planafolio/finanzrechner](https://www.nuget.org/packages/planafolio%2Ffinanzrechner) | 1.0.0 | Planafolio | Free German finance calculators (ETF savings plan, compound interest, capital g… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
