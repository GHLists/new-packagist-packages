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

## Latest list — 2026-10-02 06:22 UTC

New packages created between 2026-10-02 05:21 UTC and 2026-10-02 06:22 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T06-22-02-286956Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 05:34:36 | [urlund/wordpress-updater](https://www.nuget.org/packages/urlund%2Fwordpress-updater) | 1.0.0 | Henrik Urlund | WordPress plugin and theme updater with GitHub integration and CLI release tools |
| 2026-10-02 05:44:12 | [whitesmoke/core](https://www.nuget.org/packages/whitesmoke%2Fcore) | v0.2.0 |  | Whitesmoke Framework core: HTTP, routing, views, sessions, security, validation… |
| 2026-10-02 05:46:16 | [rad-themes/radpack-crm](https://www.nuget.org/packages/rad-themes%2Fradpack-crm) | v1.0.1 | Rad Themes | A free, full-featured CRM for Statamic: contacts, companies, quotes, invoices,… |
| 2026-10-02 05:47:08 | [whitesmoke/framework](https://www.nuget.org/packages/whitesmoke%2Fframework) | v0.2.1 |  | Whitesmoke Framework application skeleton. |
| 2026-10-02 06:04:03 | [mage2kishan/module-footer](https://www.nuget.org/packages/mage2kishan%2Fmodule-footer) | 1.0.13 | Kishan Savaliya | Panth Footer — configurable footer module for Magento 2 with Hyva and Luma them… |
| 2026-10-02 06:07:43 | [mage2kishan/module-theme-customizer](https://www.nuget.org/packages/mage2kishan%2Fmodule-theme-customizer) | 1.1.5 |  | Hyva Theme Customizer - Backend-driven theme configuration with CSS custom prop… |
| 2026-10-02 06:12:00 | [mage2kishan/module-blog](https://www.nuget.org/packages/mage2kishan%2Fmodule-blog) | 1.3.7 | Kishan Savaliya | Panth_Blog - SEO-grade blog module for Magento 2 with first-class AEO/AIO suppo… |
| 2026-10-02 06:15:34 | [mage2kishan/module-advanced-contact-us](https://www.nuget.org/packages/mage2kishan%2Fmodule-advanced-contact-us) | 1.1.6 |  | Advanced Contact Us Page - Custom fields, bot protection, submission management… |
| 2026-10-02 06:19:03 | [mage2kishan/theme-frontend-panth-infotech](https://www.nuget.org/packages/mage2kishan%2Ftheme-frontend-panth-infotech) | 1.0.6 | Kishan Savaliya | Hyva child theme Panth/Infotech for Magento 2, based on the Hyva/default parent… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
