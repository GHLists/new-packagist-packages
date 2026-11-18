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

## Latest list — 2026-11-18 00:20 UTC

New packages created between 2026-11-17 23:21 UTC and 2026-11-18 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T00-20-38-646369Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 23:24:34 | [berrycookie/module-consent-banner](https://www.nuget.org/packages/berrycookie%2Fmodule-consent-banner) | 1.0.0 | BerryCookie | BerryCookie – Cookie Consent: the BerryCookie cookie banner, script blocking an… |
| 2026-11-17 23:50:25 | [fisharebest/badge](https://www.nuget.org/packages/fisharebest%2Fbadge) | 1.0.1 |  | Generate SVG badges from PHP CI results without an external service |
| 2026-11-17 23:52:33 | [juaniquillo/table-component-action](https://www.nuget.org/packages/juaniquillo%2Ftable-component-action) | v0.1.0 | Juaniquillo | Table cell action/recipe components and table builders for backend tables. |
| 2026-11-18 00:17:02 | [jeffersongoncalves/laravel-us-privacy](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-us-privacy) | 1.0.0 | Jefferson Gonçalves | US state privacy laws for Laravel: the rules of 18 state laws (Virginia, Colora… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
