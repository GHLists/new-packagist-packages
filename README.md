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

## Latest list — 2026-11-16 15:21 UTC

New packages created between 2026-11-16 14:20 UTC and 2026-11-16 15:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T15-21-59-768769Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 14:25:36 | [veyqo/veyqo-php](https://www.nuget.org/packages/veyqo%2Fveyqo-php) | v0.1.0 |  | Official PHP library for the Veyqo payments API: payments, checkout, refunds, s… |
| 2026-11-16 14:35:02 | [company4-dev/ico](https://www.nuget.org/packages/company4-dev%2Fico) | 1.4 | Jas-n | An easy-to-use library to generate valid ICO files. |
| 2026-11-16 14:39:30 | [starbug/css](https://www.nuget.org/packages/starbug%2Fcss) | v0.9.0 | Ali Gangji | Stylesheet discovery and the css template helper. |
| 2026-11-16 14:42:24 | [theagency2627/socialite-launcher](https://www.nuget.org/packages/theagency2627%2Fsocialite-launcher) | v0.1.0 |  | Socialite provider voor inloggen met de Game Launcher. |
| 2026-11-16 14:43:28 | [tornado-engine/access-microsoft-ad](https://www.nuget.org/packages/tornado-engine%2Faccess-microsoft-ad) | v0.1.0 |  | Tornado Engine module: gives roles to Active Directory OUs, groups and users, s… |
| 2026-11-16 14:43:38 | [tornado-engine/access-microsoft-entra](https://www.nuget.org/packages/tornado-engine%2Faccess-microsoft-entra) | v0.1.0 |  | Tornado Engine module: gives roles to Entra ID groups and users, synced nightly. |
| 2026-11-16 14:47:05 | [funset/mfa-email](https://www.nuget.org/packages/funset%2Fmfa-email) | v14.0.2 | Ralf Freit; Benno Nijholt | E-Mail MFA Provider: provides multi-factor authentication via e-mail for the TY… |
| 2026-11-16 15:01:06 | [starbug/doctrine](https://www.nuget.org/packages/starbug%2Fdoctrine) | v0.9.0 | Ali Gangji | Doctrine based implementations of database module interfaces. |
| 2026-11-16 15:08:21 | [citrus-framework/notification](https://www.nuget.org/packages/citrus-framework%2Fnotification) | v1.0.0 | take64 | php notification library |
| 2026-11-16 15:16:41 | [ahmedelpopown/lpg-laravel-payment-gateway](https://www.nuget.org/packages/ahmedelpopown%2Flpg-laravel-payment-gateway) | v1.0.0 |  | Reusable Laravel Payment Core for Stripe, PayPal, refunds, webhooks and reconci… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
