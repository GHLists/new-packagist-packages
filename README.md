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

## Latest list — 2026-11-17 19:22 UTC

New packages created between 2026-11-17 18:22 UTC and 2026-11-17 19:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-17T19-22-10-233808Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-17 18:25:09 | [sightpress/core](https://www.nuget.org/packages/sightpress%2Fcore) | 0.1.0 |  | The core of SightPress, a powerful multi-site, multilingual CMS for everyone, d… |
| 2026-11-17 18:25:41 | [sightpress/skeleton](https://www.nuget.org/packages/sightpress%2Fskeleton) | 0.1.0 |  | Start a new SightPress project: a powerful multi-site, multilingual CMS for eve… |
| 2026-11-17 18:27:21 | [susantokun/lir-kit](https://www.nuget.org/packages/susantokun%2Flir-kit) | v0.2.0 |  | Passwordless email-code (OTP) sign-in, sender email settings with an editable t… |
| 2026-11-17 18:28:08 | [backdrop-dev/icons](https://www.nuget.org/packages/backdrop-dev%2Ficons) | v1.0.0 | Benjamin Lu | Iconoir SVG icons for ClassicPress and WordPress themes and plugins, with helpe… |
| 2026-11-17 18:30:52 | [zhylon/maillab-client](https://www.nuget.org/packages/zhylon%2Fmaillab-client) | v0.0.1 | TobyMaxham | Laravel mail transport and API client for Zhylon Maillab. |
| 2026-11-17 18:31:12 | [ospo/theme-frontend-hyva](https://www.nuget.org/packages/ospo%2Ftheme-frontend-hyva) | 1.0.0 | Splendid Internet GmbH | Kind-Theme des Hyvä Default Themes mit eigenem Tailwind-Bau, damit Blog, Widget… |
| 2026-11-17 18:47:00 | [tualo/encrypted-data](https://www.nuget.org/packages/tualo%2Fencrypted-data) | 1.0.2 | Thomas Hoffmann | tualo - encrypted-data: clientseitig verschluesselte Datenelemente (RSA-OAEP +… |
| 2026-11-17 19:09:33 | [outstand/accordion](https://www.nuget.org/packages/outstand%2Faccordion) | 1.0.0 | Sérgio Santos | Accessible accordion blocks for the block editor, powered by the Interactivity… |
| 2026-11-17 19:14:43 | [ktulchu/yii2-chart](https://www.nuget.org/packages/ktulchu%2Fyii2-chart) | v0.1.0 | Roman V Komorin | ActiveRecord time-series charts for Yii2 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
