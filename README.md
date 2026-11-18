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

## Latest list — 2026-11-18 11:21 UTC

New packages created between 2026-11-18 10:23 UTC and 2026-11-18 11:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-18T11-21-34-255611Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-18 10:33:01 | [mertaydin/laravel-system-monitor](https://www.nuget.org/packages/mertaydin%2Flaravel-system-monitor) | v0.1.2 |  | A customizable Laravel system monitoring dashboard for server resources, PHP, d… |
| 2026-11-18 10:37:16 | [agent001/magento-support-assistant](https://www.nuget.org/packages/agent001%2Fmagento-support-assistant) | 1.1.0 |  | Agent001 catalog synchronization and storefront assistant for Magento 2 |
| 2026-11-18 10:42:17 | [mom/microsoft](https://www.nuget.org/packages/mom%2Fmicrosoft) | v6.4.0 | Darwin Luague | A Microsoft 365 connector for mom/connectors: sign in with Microsoft and read a… |
| 2026-11-18 11:10:30 | [chmuzamil/pakdatakit](https://www.nuget.org/packages/chmuzamil%2Fpakdatakit) | v2.5.0 | Muzamil Chaudhery | Pakistani data utilities for PHP and Laravel: validate CNIC, mobile, IBAN, NTN/… |
| 2026-11-18 11:13:10 | [klxm/fluid](https://www.nuget.org/packages/klxm%2Ffluid) | 1.0.0-beta.1 | Thomas Skerbis; KLXM Crossmed… | Blöcke mit Feldschema und Bearbeiten direkt auf der Website für REDAXO 6 |
| 2026-11-18 11:13:15 | [klxm/fluid_demo](https://www.nuget.org/packages/klxm%2Ffluid_demo) | 1.0.0-beta.1 | Thomas Skerbis; KLXM Crossmed… | Ergänzung für das REDAXO-6-AddOn fluid: Demo-Modus – Besucher bearbeiten die We… |
| 2026-11-18 11:13:19 | [klxm/image_editor](https://www.nuget.org/packages/klxm%2Fimage_editor) | 1.0.0-beta.1 | Thomas Skerbis; KLXM Crossmed… | Bilder zerstörungsfrei bearbeiten für REDAXO 6: Zuschneiden, Drehen, Spiegeln,… |
| 2026-11-18 11:13:23 | [klxm/video_editor](https://www.nuget.org/packages/klxm%2Fvideo_editor) | 1.0.0-beta.1 | Thomas Skerbis; KLXM Crossmed… | Videos im REDAXO-6-Medienpool bearbeiten: analysieren, für das Web optimieren,… |
| 2026-11-18 11:13:27 | [klxm/navigation_array](https://www.nuget.org/packages/klxm%2Fnavigation_array) | 1.0.0-beta.1 | Thomas Skerbis; KLXM Crossmed… | Navigation als Array für REDAXO 6: Kategorien und Artikel mit Hierarchie, Filte… |
| 2026-11-18 11:13:31 | [klxm/quickbar](https://www.nuget.org/packages/klxm%2Fquickbar) | 1.0.0-beta.1 | Thomas Skerbis; KLXM Crossmed… | Successor of quick_navigation for REDAXO 6: command palette with live search ac… |
| 2026-11-18 11:13:35 | [klxm/tiptap](https://www.nuget.org/packages/klxm%2Ftiptap) | 1.0.0-beta.1 | Thomas Skerbis; KLXM Crossmed… | WYSIWYG and Markdown editor for REDAXO 6 based on TipTap: profiles with toolbar… |
| 2026-11-18 11:13:39 | [klxm/klxm_meta](https://www.nuget.org/packages/klxm%2Fklxm_meta) | 1.0.0-beta.1 | Thomas Skerbis; KLXM Crossmed… | Shared meta fields for REDAXO 6: alternative text per language and “decorative”… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
