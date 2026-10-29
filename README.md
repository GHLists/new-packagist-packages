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

## Latest list — 2026-10-29 16:20 UTC

New packages created between 2026-10-29 15:22 UTC and 2026-10-29 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T16-20-45-349558Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 15:32:44 | [zerofront/module-zero-cache-warmer](https://www.nuget.org/packages/zerofront%2Fmodule-zero-cache-warmer) | 1.3.5 | Roman Pasichnyk | Zero for Magento Open Source: warms the full page cache after a deploy, a flush… |
| 2026-10-29 15:32:44 | [zerofront/module-zero-index-doctor](https://www.nuget.org/packages/zerofront%2Fmodule-zero-index-doctor) | 1.3.5 | Roman Pasichnyk | Zero for Magento Open Source: what slows Magento's indexers down or stops them,… |
| 2026-10-29 15:41:30 | [cosmemilton/acbr-printer-php](https://www.nuget.org/packages/cosmemilton%2Facbr-printer-php) | v0.1.0 |  | Impressão PHP com ACBrPosPrinter, FortesReport e DANFE via runtime Free Pascal/… |
| 2026-10-29 15:47:26 | [dataemergencia/emergency-bff](https://www.nuget.org/packages/dataemergencia%2Femergency-bff) | v0.1.0 |  | Backend-for-frontend for the DataEmergencia emergency module. |
| 2026-10-29 15:48:51 | [xiaogan80/flarum-hot-board](https://www.nuget.org/packages/xiaogan80%2Fflarum-hot-board) | v1.3.0 |  | 在讨论列表上方显示「推荐帖子 / 最新帖子 / 热门浏览」三列看板，每条自动填充帖子首图或用户头像。 |
| 2026-10-29 15:57:05 | [goletter/hyperf-2fa](https://www.nuget.org/packages/goletter%2Fhyperf-2fa) | v1.0.0 | goletter | Google Authenticator (TOTP) 2FA for Hyperf: bind user, per-module verify, idle… |
| 2026-10-29 16:05:27 | [elcuro/sulu-slug-replacers](https://www.nuget.org/packages/elcuro%2Fsulu-slug-replacers) | v1.0.0 | Juraj Jancuska | Configure the character replacers Sulu applies when generating URL slugs (e.g.… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
