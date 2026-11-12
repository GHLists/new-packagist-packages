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

## Latest list — 2026-11-12 12:19 UTC

New packages created between 2026-11-12 11:21 UTC and 2026-11-12 12:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T12-19-15-100551Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 11:24:06 | [darkterminal/turso-platform-laravel](https://www.nuget.org/packages/darkterminal%2Fturso-platform-laravel) | v1.0.0 | Imam Ali Mustofa | Laravel integration for the Turso Platform API PHP SDK |
| 2026-11-12 11:25:23 | [kith-web-studio/google-business-profile-php](https://www.nuget.org/packages/kith-web-studio%2Fgoogle-business-profile-php) | v0.1.1-rc.1 |  | PHP SDK for Google Business Profile APIs |
| 2026-11-12 11:25:44 | [bhekor/laravel-opay](https://www.nuget.org/packages/bhekor%2Flaravel-opay) | v1.0.0 | Ibidapo Adeolu | A Laravel package for integrating OPay Checkout payment APIs |
| 2026-11-12 11:52:20 | [codeconjure/gls](https://www.nuget.org/packages/codeconjure%2Fgls) | 0.1.0 |  | MyGLS API protokoll-kliens — keretrendszer-független, PSR-18 alapon. |
| 2026-11-12 11:57:12 | [robuust/craft-inertia](https://www.nuget.org/packages/robuust%2Fcraft-inertia) | v0.1.0-beta.1 | Robuust | Opt-in public Inertia frontend integration for Craft CMS 6. |
| 2026-11-12 12:02:04 | [phalcon4to5/rector](https://www.nuget.org/packages/phalcon4to5%2Frector) | v0.1.0 | xuwenxiong | Rector upgrade rules for Phalcon Framework 4 to 5 |
| 2026-11-12 12:02:04 | [xuwenxiong/phalcon4to5-rector](https://www.nuget.org/packages/xuwenxiong%2Fphalcon4to5-rector) | v0.1.0 | xuwenxiong | Rector upgrade rules for Phalcon Framework 4 to 5 |
| 2026-11-12 12:07:19 | [getkirby/actions](https://www.nuget.org/packages/getkirby%2Factions) | 0.2.0 |  | Reusable workflows and GitHub Actions for the CI of Kirby's core, libraries and… |
| 2026-11-12 12:12:31 | [vytux/vytux_cousins](https://www.nuget.org/packages/vytux%2Fvytux_cousins) | 2.2.0 | Vytautas Krivickas | A webtrees custom module that adds a Cousins tab to the individual page. |
| 2026-11-12 12:15:28 | [codeconjure/gls-sylius-plugin](https://www.nuget.org/packages/codeconjure%2Fgls-sylius-plugin) | 0.1.0 |  | GLS szállítási integráció Syliushoz: szállítási módok, csomagpont, díj, és — My… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
