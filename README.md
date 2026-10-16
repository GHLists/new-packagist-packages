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

## Latest list — 2026-10-16 05:21 UTC

New packages created between 2026-10-16 04:21 UTC and 2026-10-16 05:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T05-21-41-14919Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 04:28:13 | [hanshs474/emaki](https://www.nuget.org/packages/hanshs474%2Femaki) | v0.1.0 | emaki | Official SDK for emaki (emaki.ai), the Japanese-language AI video generator for… |
| 2026-10-16 04:31:24 | [skynettechnologies/silverstripe-skyneta11ypdfremediation](https://www.nuget.org/packages/skynettechnologies%2Fsilverstripe-skyneta11ypdfremediation) | 1.0.0 | Skynet Technologies USA LLC | AI-powered PDF accessibility remediation - upload PDFs, scan website PDFs, and… |
| 2026-10-16 05:03:56 | [docuhook/docuhook](https://www.nuget.org/packages/docuhook%2Fdocuhook) | v1.0.0 | DocuHook | Official DocuHook PHP client — merge JSON into HTML templates via the DocuHook… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
