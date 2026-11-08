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

## Latest list — 2026-11-08 21:21 UTC

New packages created between 2026-11-08 20:18 UTC and 2026-11-08 21:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-08T21-21-26-878536Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-08 20:21:09 | [codingagency/laravel-spam-strike](https://www.nuget.org/packages/codingagency%2Flaravel-spam-strike) | v0.2.0 | Coding Agency | Stop contact form spam in Laravel without a CAPTCHA, then hit back: a JavaScrip… |
| 2026-11-08 20:22:09 | [roundly-consulting/webhooks-for-laravel](https://www.nuget.org/packages/roundly-consulting%2Fwebhooks-for-laravel) | 1.0.1 | Andrej Mihaliak | Receive and send signed webhooks in Laravel: verified per-sender endpoints with… |
| 2026-11-08 20:59:35 | [pushery/ses-inbound-mail-for-laravel](https://www.nuget.org/packages/pushery%2Fses-inbound-mail-for-laravel) | v0.1.0 | Pushery | Receive mail through Amazon SES in Laravel: a verified SNS endpoint, takeover f… |
| 2026-11-08 21:07:08 | [pushery/http-api-for-laravel](https://www.nuget.org/packages/pushery%2Fhttp-api-for-laravel) | v0.1.0 | Pushery | The IETF HTTP API standards for Laravel: Idempotency-Key replays that compare t… |
| 2026-11-08 21:14:10 | [jeffersongoncalves/laravel-centrifugo](https://www.nuget.org/packages/jeffersongoncalves%2Flaravel-centrifugo) | 1.0.0 | Jefferson Gonçalves | Laravel broadcasting driver for Centrifugo: publishes through the server HTTP A… |
| 2026-11-08 21:18:05 | [nowo-tech/brand-contracts](https://www.nuget.org/packages/nowo-tech%2Fbrand-contracts) | v1.0.0 | Héctor Franco Aceituno; Nowo.… | Shared brand contract for PHP apps and nowo-tech bundles: brand name, colours a… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
