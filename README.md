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

## Latest list — 2026-10-07 19:20 UTC

New packages created between 2026-10-07 18:21 UTC and 2026-10-07 19:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-07T19-20-53-160319Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-07 18:22:37 | [larasell-dev/cushion](https://www.nuget.org/packages/larasell-dev%2Fcushion) | 0.1.1 |  | Form draft persistence for Laravel: server-backed auto-save for Inertia forms. |
| 2026-10-07 18:39:04 | [iamtime/uzpay](https://www.nuget.org/packages/iamtime%2Fuzpay) | v0.1.0 |  | Payme, Click, Uzum, Paynet and Octo (Visa, Mastercard) for Uzbekistan shops: me… |
| 2026-10-07 18:49:10 | [emerson-pombo/idempotency-linter](https://www.nuget.org/packages/emerson-pombo%2Fidempotency-linter) | v0.1.0 | Emerson Pombo | Analisador estático que identifica jobs de fila Laravel sem proteção contra ree… |
| 2026-10-07 18:56:13 | [jauhar/captcha-generator](https://www.nuget.org/packages/jauhar%2Fcaptcha-generator) | v1.0 | jauharimtikhan | Captcha Generator PHP |
| 2026-10-07 19:07:30 | [rafalmasiarek/captcha](https://www.nuget.org/packages/rafalmasiarek%2Fcaptcha) | v1.0.0 |  | Universal CAPTCHA verification for PHP: Google reCAPTCHA (v2/v3), Cloudflare Tu… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
