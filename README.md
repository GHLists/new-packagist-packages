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

## Latest list — 2026-09-27 23:21 UTC

New packages created between 2026-09-27 22:20 UTC and 2026-09-27 23:21 UTC.

[Full CSV](data/new-packagist-packages-2026-09-27T23-21-42-593015Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-09-27 22:32:58 | [componenta/auth-app](https://www.nuget.org/packages/componenta%2Fauth-app) | v2.0.1 |  | Authentication context integration for Componenta DI v5 |
| 2026-09-27 22:32:58 | [componenta/auth-http](https://www.nuget.org/packages/componenta%2Fauth-http) | v1.0.0 |  | PSR-7/PSR-15 HTTP integration for Componenta Auth |
| 2026-09-27 22:32:58 | [componenta/auth-token](https://www.nuget.org/packages/componenta%2Fauth-token) | v1.0.0 |  | Purpose-separated one-time bearer tokens for Componenta authentication flows |
| 2026-09-27 22:32:59 | [componenta/auth-jwt](https://www.nuget.org/packages/componenta%2Fauth-jwt) | v1.0.0 |  | JWT access tokens and rotating refresh-token families for Componenta Auth 3 |
| 2026-09-27 22:32:59 | [componenta/auth-session](https://www.nuget.org/packages/componenta%2Fauth-session) | v1.0.0 |  | Authentication-session contracts and lifecycle for Componenta Auth |
| 2026-09-27 22:33:00 | [componenta/auth-session-app](https://www.nuget.org/packages/componenta%2Fauth-session-app) | v1.0.0 |  | Current authentication-session parameter integration for Componenta DI |
| 2026-09-27 22:33:00 | [componenta/auth-session-database](https://www.nuget.org/packages/componenta%2Fauth-session-database) | v1.0.0 |  | Cycle Database persistence for Componenta authentication sessions |
| 2026-09-27 22:33:01 | [componenta/auth-magic-link](https://www.nuget.org/packages/componenta%2Fauth-magic-link) | v1.0.0 |  | Pre-auth-bound magic-link authentication for Componenta Auth 3 |
| 2026-09-27 22:33:01 | [componenta/auth-session-http](https://www.nuget.org/packages/componenta%2Fauth-session-http) | v1.0.0 |  | PSR-7/PSR-15 browser transport for Componenta authentication sessions |
| 2026-09-27 22:33:02 | [componenta/auth-otp](https://www.nuget.org/packages/componenta%2Fauth-otp) | v1.0.0 |  | Bound one-time-code authentication challenges for Componenta Auth 3 |
| 2026-09-27 22:33:02 | [componenta/auth-password](https://www.nuget.org/packages/componenta%2Fauth-password) | v1.0.0 |  | Password authentication and password-reset HTTP flows for Componenta Auth 3 |
| 2026-09-27 22:33:03 | [componenta/auth-recovery-code](https://www.nuget.org/packages/componenta%2Fauth-recovery-code) | v1.0.0 |  | Single-use recovery codes for Componenta Auth 3 |
| 2026-09-27 22:33:03 | [componenta/auth-remember-me](https://www.nuget.org/packages/componenta%2Fauth-remember-me) | v1.0.0 |  | Rotating persistent remember-me grants for Componenta Auth 3 |
| 2026-09-27 22:33:04 | [componenta/auth-totp](https://www.nuget.org/packages/componenta%2Fauth-totp) | v1.0.0 |  | Encrypted TOTP enrollment and reauthentication for Componenta Auth 3 |
| 2026-09-27 22:33:04 | [componenta/auth-webauthn](https://www.nuget.org/packages/componenta%2Fauth-webauthn) | v1.0.0 |  | WebAuthn/passkey authentication and reauthentication for Componenta Auth 3 |
| 2026-09-27 23:03:14 | [ussaaass/hyperf-swagger](https://www.nuget.org/packages/ussaaass%2Fhyperf-swagger) | v3.2.6 |  | A swagger library for Hyperf. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
