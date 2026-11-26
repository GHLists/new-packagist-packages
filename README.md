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

## Latest list — 2026-11-26 07:22 UTC

New packages created between 2026-11-26 06:21 UTC and 2026-11-26 07:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-26T07-22-12-81221Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-26 06:31:08 | [laveroadmin/forms](https://www.nuget.org/packages/laveroadmin%2Fforms) | v1.0.0 | Aleksandr Kireev | Public form builder, lead submissions inbox, and antispam for LaveroAdmin. |
| 2026-11-26 06:33:51 | [laveroadmin/mail-log](https://www.nuget.org/packages/laveroadmin%2Fmail-log) | v1.0.0 | Aleksandr Kireev | Outgoing email log & HTML preview for LaveroAdmin. |
| 2026-11-26 06:36:36 | [se7enxweb/tron](https://www.nuget.org/packages/se7enxweb%2Ftron) | 0.0.0.13 | 7x | tron, the open MCP server layer of Exponential: stdio and streamable HTTP trans… |
| 2026-11-26 06:37:25 | [laveroadmin/menus](https://www.nuget.org/packages/laveroadmin%2Fmenus) | v1.0.0 | Aleksandr Kireev | Public site navigation and multi-menu builder with drag-and-drop Tree and forev… |
| 2026-11-26 06:39:33 | [laveroadmin/notifications](https://www.nuget.org/packages/laveroadmin%2Fnotifications) | v1.0.0 | Aleksandr Kireev | Unified Telegram, Email, and Webhook notification channels & logs for LaveroAdm… |
| 2026-11-26 06:42:33 | [proudnerds/pn-export-redirects](https://www.nuget.org/packages/proudnerds%2Fpn-export-redirects) | 14.3.0 | Proud Nerds | Adds a CSV export to the redirects module |
| 2026-11-26 06:42:59 | [laveroadmin/seo](https://www.nuget.org/packages/laveroadmin%2Fseo) | v1.0.0 | Aleksandr Kireev | SEO redirects manager (301/302/410), robots.txt editor, and global meta setting… |
| 2026-11-26 06:45:03 | [laveroadmin/sessions](https://www.nuget.org/packages/laveroadmin%2Fsessions) | v1.0.0 | Aleksandr Kireev | Active admin sessions manager and login audit for LaveroAdmin. |
| 2026-11-26 06:46:50 | [laveroadmin/tiptap](https://www.nuget.org/packages/laveroadmin%2Ftiptap) | v1.0.0 | Aleksandr Kireev | Modern TipTap WYSIWYG editor field for LaveroAdmin forms. |
| 2026-11-26 06:49:44 | [laveroadmin/cache-manager](https://www.nuget.org/packages/laveroadmin%2Fcache-manager) | v1.0.0 | Aleksandr Kireev | Cache, OPcache, and Artisan optimization manager for LaveroAdmin (shared-hostin… |
| 2026-11-26 06:50:44 | [athenanetworks/acma-senderid](https://www.nuget.org/packages/athenanetworks%2Facma-senderid) | 1.0.0 |  | PHP client for the ACMA SMS Sender ID Register API (RCS Verification Authority… |
| 2026-11-26 07:17:39 | [mathsgod/light-io](https://www.nuget.org/packages/mathsgod%2Flight-io) | v1.0.0 |  | Text writers for PHP strings and streams |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
