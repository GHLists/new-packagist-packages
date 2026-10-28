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

## Latest list — 2026-10-28 20:20 UTC

New packages created between 2026-10-28 19:19 UTC and 2026-10-28 20:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-28T20-20-33-230252Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-28 19:42:23 | [juststeveking/sdk-toolbox](https://www.nuget.org/packages/juststeveking%2Fsdk-toolbox) | v0.0.1 | Steve McDougall | Build PHP SDKs on PSR-18, typed end to end, with the HTTP standards an API clie… |
| 2026-10-28 19:46:48 | [juhe-it-solutions/contao-consent-bundle](https://www.nuget.org/packages/juhe-it-solutions%2Fcontao-consent-bundle) | 1.0.0 | JUHE IT-solutions | Consent banner and settings for Contao 5.7 and 6: consent groups, blocking of s… |
| 2026-10-28 19:48:15 | [pushinbr/pam-native-i18n](https://www.nuget.org/packages/pushinbr%2Fpam-native-i18n) | v0.1.0 |  | Optional message catalogs, translation, locale preferences and formatting for P… |
| 2026-10-28 19:48:25 | [twstec/kit-webhooks](https://www.nuget.org/packages/twstec%2Fkit-webhooks) | v2.0.0-beta.15 | TWS | Webhooks de saída do TWS Laravel Starter Kit, sem telas: endpoints por conta (e… |
| 2026-10-28 19:50:57 | [nexus-lab/cpanel-installer](https://www.nuget.org/packages/nexus-lab%2Fcpanel-installer) | v1.0.0 | NextPHP Architecture Team | Zero-SSH graphical web installer for NextPHP and Nexus applications on cPanel s… |
| 2026-10-28 19:55:22 | [automattic/jetpack-monitor](https://www.nuget.org/packages/automattic%2Fjetpack-monitor) | v0.1.0 |  | Downtime monitoring for connected sites: the module's email alerts and status f… |
| 2026-10-28 19:56:29 | [webmasterskaya/php-unisender-api](https://www.nuget.org/packages/webmasterskaya%2Fphp-unisender-api) | v1.0.0 | Artem Vasilev | Unofficial PHP SDK for the UniSender email and SMS API |
| 2026-10-28 20:15:18 | [bundle/identity-laravel](https://www.nuget.org/packages/bundle%2Fidentity-laravel) | v1.0.0 |  | Laravel scope authorization SDK for Bundle Identity |
| 2026-10-28 20:17:07 | [overclock/lab-kit](https://www.nuget.org/packages/overclock%2Flab-kit) | v0.1.0 |  | Optional bridge between a Laravel app and the Overclock Lab panel. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
