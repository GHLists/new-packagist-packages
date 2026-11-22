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

## Latest list — 2026-11-22 22:19 UTC

New packages created between 2026-11-22 21:20 UTC and 2026-11-22 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T22-19-52-820278Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 21:34:09 | [foresi/vat](https://www.nuget.org/packages/foresi%2Fvat) | v0.9.29 |  | The VAT of the firm: its VAT periods with the due dates from the country's rule… |
| 2026-11-22 21:53:01 | [delgraf/module-seo-html-sitemap-tree](https://www.nuget.org/packages/delgraf%2Fmodule-seo-html-sitemap-tree) | v1.0.0 | Delgraf | Hierarchical, collapsible tree view for the Swissup SEO HTML Sitemap on Magento… |
| 2026-11-22 21:57:00 | [foresi/activities](https://www.nuget.org/packages/foresi%2Factivities) | v0.9.29 |  | Meetings, calls, notes and tasks logged or planned on any record, on its timeli… |
| 2026-11-22 22:03:11 | [jenswittmann/kirby-jolitypo](https://www.nuget.org/packages/jenswittmann%2Fkirby-jolitypo) | v0.1.0 | Jens Wittmann | Microtypography for Kirby: JoliTypo as a field and blocks method (quotes, dashe… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
