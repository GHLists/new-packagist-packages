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

## Latest list — 2026-10-02 10:21 UTC

New packages created between 2026-10-02 09:18 UTC and 2026-10-02 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-02T10-21-51-631286Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-02 09:20:15 | [tobimori/kirby-global-blocks](https://www.nuget.org/packages/tobimori%2Fkirby-global-blocks) | 0.1.1 |  | Reusable global blocks for Kirby blocks and layout fields |
| 2026-10-02 09:23:21 | [nordwerk/contao-sections-bundle](https://www.nuget.org/packages/nordwerk%2Fcontao-sections-bundle) | v0.1.0 |  | Page sections for Contao content pages: hero, page head, promises, picture and… |
| 2026-10-02 09:57:21 | [siberfx/linkedin-autopost](https://www.nuget.org/packages/siberfx%2Flinkedin-autopost) | 1.1.0 | Selim Görmüş | Connect one LinkedIn account to your Laravel app and share models to LinkedIn a… |
| 2026-10-02 10:06:16 | [besnovatyj/yii2-cms-blocks](https://www.nuget.org/packages/besnovatyj%2Fyii2-cms-blocks) | v1.0.0 | Besnovatyj | Модуль блоков Yii2 CMS: управляемое из админки содержимое мест, объявленных тем… |
| 2026-10-02 10:17:27 | [hirasso/wp-sync-deploy](https://www.nuget.org/packages/hirasso%2Fwp-sync-deploy) | 3.0.0 |  | Bash scripts to sync and deploy WordPress sites |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
