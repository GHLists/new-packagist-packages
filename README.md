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

## Latest list — 2026-11-21 17:21 UTC

New packages created between 2026-11-21 16:20 UTC and 2026-11-21 17:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-21T17-21-00-369587Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-21 16:45:00 | [imrandevbd/laravel-role-matrix](https://www.nuget.org/packages/imrandevbd%2Flaravel-role-matrix) | v1.1.0 | Imran Ahmed | Premium role and permission management for Laravel, with a Role × Module × Acti… |
| 2026-11-21 16:51:17 | [websitepruefen/typo3-connect](https://www.nuget.org/packages/websitepruefen%2Ftypo3-connect) | v0.1.0 |  | Connects a TYPO3 website with websiteprüfen.de: finished articles arrive as new… |
| 2026-11-21 16:55:32 | [xincheng/yii2-rabbitmq](https://www.nuget.org/packages/xincheng%2Fyii2-rabbitmq) | 3.0.0 | Mikhail Bakulin | Wrapper based on php-amqplib to incorporate messaging in your Yii2 application… |
| 2026-11-21 17:07:09 | [sinemacula/laravel-authentication](https://www.nuget.org/packages/sinemacula%2Flaravel-authentication) | v0.1.0 | Ben Carey | Stateless contextual authentication primitives (Identity, Principal, Session, T… |
| 2026-11-21 17:07:14 | [sinemacula/laravel-mfa](https://www.nuget.org/packages/sinemacula%2Flaravel-mfa) | v0.1.0 | Ben Carey | Driver-based multi-factor authentication (TOTP, email, SMS, passkeys and recove… |
| 2026-11-21 17:07:19 | [sinemacula/laravel-sso](https://www.nuget.org/packages/sinemacula%2Flaravel-sso) | v0.1.0 | Ben Carey | Tenant single sign-on over SAML 2.0 and OpenID Connect for Laravel 12 and 13: c… |
| 2026-11-21 17:07:24 | [sinemacula/laravel-audit-log](https://www.nuget.org/packages/sinemacula%2Flaravel-audit-log) | v0.1.0 | Ben Carey | Event-driven audit logging of user activity for Laravel 12 and 13: automatic ca… |
| 2026-11-21 17:07:29 | [sinemacula/laravel-authorization](https://www.nuget.org/packages/sinemacula%2Flaravel-authorization) | v0.1.0 | Ben Carey | Role-based access control and IAM-style policy evaluation for Laravel 12 and 13. |
| 2026-11-21 17:07:53 | [quikcast/quikcast](https://www.nuget.org/packages/quikcast%2Fquikcast) | 0.0.1 |  | PHP client library for the Quikcast native management API. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
