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

## Latest list — 2026-11-14 22:19 UTC

New packages created between 2026-11-14 21:19 UTC and 2026-11-14 22:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-14T22-19-22-427641Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-14 21:24:28 | [mj-zana/captcha](https://www.nuget.org/packages/mj-zana%2Fcaptcha) | v2.25.0 |  | CAPTCHA providers for Zana applications: Cloudflare Turnstile, Google reCAPTCHA… |
| 2026-11-14 21:25:29 | [mortalkiller/filament-appearance](https://www.nuget.org/packages/mortalkiller%2Ffilament-appearance) | v1.0.0 |  | Colour palettes, a palette picker and a phone-friendly panel shell for Filament. |
| 2026-11-14 21:48:01 | [xivig/captcha](https://www.nuget.org/packages/xivig%2Fcaptcha) | v2.0.0 | CyberWord | Privacy-conscious, framework-agnostic PHP challenge and anti-abuse toolkit |
| 2026-11-14 21:53:50 | [sailantis/azera-app](https://www.nuget.org/packages/sailantis%2Fazera-app) | v0.4.0 |  | A starter project for the Azera PHP framework |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
