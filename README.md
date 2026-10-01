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

## Latest list — 2026-10-01 08:19 UTC

New packages created between 2026-10-01 07:21 UTC and 2026-10-01 08:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-01T08-19-01-086895Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-01 07:36:56 | [mage2kishan/module-zipcode-validation](https://www.nuget.org/packages/mage2kishan%2Fmodule-zipcode-validation) | 1.1.1 | Kishan Savaliya | Panth ZipcodeValidation — validates ZIP/PIN codes at checkout against configura… |
| 2026-10-01 07:40:06 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.3 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |
| 2026-10-01 07:40:10 | [trismegiste/parsoid-bundle](https://www.nuget.org/packages/trismegiste%2Fparsoid-bundle) | 1.0.0 |  |  |
| 2026-10-01 07:44:15 | [webware/webware-theme](https://www.nuget.org/packages/webware%2Fwebware-theme) | 1.0.0-alpha.1 | Joey Smith | Provides theme support via laminas-view to webware applications. |
| 2026-10-01 07:50:01 | [webware/webware-htmx](https://www.nuget.org/packages/webware%2Fwebware-htmx) | 1.0.0-alpha.1 | Joey Smith | Provides HTMX support via laminas-view to webware applications. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
