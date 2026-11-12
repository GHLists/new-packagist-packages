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

## Latest list — 2026-11-12 04:21 UTC

New packages created between 2026-11-12 03:20 UTC and 2026-11-12 04:21 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T04-21-41-301402Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 03:44:43 | [reyhanitsme/auth-engine](https://www.nuget.org/packages/reyhanitsme%2Fauth-engine) | v1.0.0 | reyhanitsme | Plug-and-play, framework-agnostic PHP authentication engine (Native PHP & Larav… |
| 2026-11-12 03:50:35 | [mahesh-kerai/payment-gateways](https://www.nuget.org/packages/mahesh-kerai%2Fpayment-gateways) | v1.0.0 | Mahesh Kerai | A Laravel package for integrating multiple payment gateways (Stripe, Razorpay,… |
| 2026-11-12 03:59:27 | [vocamax/ipa-audios](https://www.nuget.org/packages/vocamax%2Fipa-audios) | v0.1.0 | vuthaihoc | One recording per American English IPA sound (24 consonants, 11 vowels, 5 dipht… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
