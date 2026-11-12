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

## Latest list — 2026-11-12 09:21 UTC

New packages created between 2026-11-12 08:21 UTC and 2026-11-12 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T09-21-23-195563Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 08:31:16 | [cboxdk/laravel-relay-client](https://www.nuget.org/packages/cboxdk%2Flaravel-relay-client) | v0.1.0 | Sylvester Damgaard | Cbox Relay client for Laravel: publish events, send mail and push, judge conten… |
| 2026-11-12 08:34:27 | [kvadro/post-core](https://www.nuget.org/packages/kvadro%2Fpost-core) | 1.0.2 |  | Extends Post Core Module |
| 2026-11-12 09:01:31 | [florentingarnier/cookie-consent](https://www.nuget.org/packages/florentingarnier%2Fcookie-consent) | v0.1.0 | Florentin Garnier | Cookie consent policy, purpose by purpose: the categories, the consent cookie r… |
| 2026-11-12 09:04:04 | [vois/vois-php](https://www.nuget.org/packages/vois%2Fvois-php) | v1.0.0 |  | VOIS SMS ve Ses API istemcisi (PHP 8.1+, Laravel desteği) |
| 2026-11-12 09:06:10 | [florentingarnier/cookie-consent-bundle](https://www.nuget.org/packages/florentingarnier%2Fcookie-consent-bundle) | v0.1.0 | Florentin Garnier | Symfony integration of florentingarnier/cookie-consent: a consent banner, a bro… |
| 2026-11-12 09:06:48 | [pteal79/image-resize](https://www.nuget.org/packages/pteal79%2Fimage-resize) | 1.0.1 |  | NativePHP Mobile v4 plugin that shrinks a JPEG, PNG or HEIC photo to a maximum… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
