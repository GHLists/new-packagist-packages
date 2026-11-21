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

## Latest list — 2026-11-21 07:21 UTC

New packages created between 2026-11-21 06:19 UTC and 2026-11-21 07:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T07-21-27-27224Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 06:31:01 | [consentinel/module-cookie-consent](https://www.nuget.org/packages/consentinel%2Fmodule-cookie-consent) | 1.0.0 | Consentinel | Consentinel Cookie Consent and Pre-Consent Script Blocker with Google Consent M… |
| 2026-11-21 06:39:15 | [schachbulle/contao-galeriemetadaten-bundle](https://www.nuget.org/packages/schachbulle%2Fcontao-galeriemetadaten-bundle) | 1.0.0 | Frank Hoppe | Abweichende Metadaten (Titel, Alternativtext, Link, Bildunterschrift) für einze… |
| 2026-11-21 06:50:05 | [js-upup/video-subtitle-window](https://www.nuget.org/packages/js-upup%2Fvideo-subtitle-window) | v0.1.0 |  | Clip and rebase subtitle cues for a video excerpt. |
| 2026-11-21 06:51:53 | [tohawk89/laravel-sso-client](https://www.nuget.org/packages/tohawk89%2Flaravel-sso-client) | v0.1.0 | Nazar | Plug-and-play Single Sign-On client for Laravel apps: OAuth 2.0 + PKCE login, u… |
| 2026-11-21 07:08:11 | [pingoline/laravel-sdk](https://www.nuget.org/packages/pingoline%2Flaravel-sdk) | v1.0.0 | PingoLine | Official PingoLine SDK for Laravel - Automated Order Confirmation Calls, SMS Ga… |
| 2026-11-21 07:16:22 | [tobento/service-repository-relation](https://www.nuget.org/packages/tobento%2Fservice-repository-relation) | 2.0 | Tobias Strub | Relations between storage repositories such as many to one, one to many and man… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
