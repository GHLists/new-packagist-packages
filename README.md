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

## Latest list — 2026-11-16 12:18 UTC

New packages created between 2026-11-16 11:19 UTC and 2026-11-16 12:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T12-18-28-574794Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 11:25:30 | [digitalize/sms](https://www.nuget.org/packages/digitalize%2Fsms) | v1.0.1 | Digitalize Lab | PHP client for the Digitalize Lab SMS API: OTP and alert messages from approved… |
| 2026-11-16 11:29:53 | [pact-protocol/core](https://www.nuget.org/packages/pact-protocol%2Fcore) | v0.2.0 |  | Independent PHP implementation of PACT Core and Swarm |
| 2026-11-16 11:30:07 | [pact-protocol/laravel](https://www.nuget.org/packages/pact-protocol%2Flaravel) | v0.2.0 |  | Laravel master and client runtime for PACT personal federations |
| 2026-11-16 11:33:49 | [buildwebproject/sylius-admin-two-factor-plugin](https://www.nuget.org/packages/buildwebproject%2Fsylius-admin-two-factor-plugin) | v1.0.0 | BuildWebProject | Two-factor sign-in (TOTP authenticator app + one-time backup codes) for the Syl… |
| 2026-11-16 11:47:51 | [felipeverse/blougly](https://www.nuget.org/packages/felipeverse%2Fblougly) | v0.1.0 | Felipe Alves (felipeverse) | Blougly: an ugly static site generator that gets out of your way |
| 2026-11-16 11:49:02 | [mr-glubschi/seat-quick-sell](https://www.nuget.org/packages/mr-glubschi%2Fseat-quick-sell) | v0.1.0 |  | SeAT plugin: price items for selling at the market where you are and copy them… |
| 2026-11-16 12:03:09 | [buildwebproject/sylius-razorpay-plugin](https://www.nuget.org/packages/buildwebproject%2Fsylius-razorpay-plugin) | v1.0.0-beta.1 | BuildWebProject | Razorpay Standard Checkout for Sylius 2: UPI, cards, netbanking and wallets, si… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
