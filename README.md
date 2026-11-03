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

## Latest list — 2026-11-03 11:20 UTC

New packages created between 2026-11-03 10:18 UTC and 2026-11-03 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-03T11-20-46-760518Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-03 10:30:10 | [bedud5495/php_xpub](https://www.nuget.org/packages/bedud5495%2Fphp_xpub) | v1.1.0 | bedud5495 | Derive BTC, LTC, DOGE, BCH, DASH and ETH extended public keys and addresses wit… |
| 2026-11-03 10:34:48 | [sentry/sentry-php-tracer](https://www.nuget.org/packages/sentry%2Fsentry-php-tracer) | 0.1.0 |  | Experimental Sentry tracing extension for PHP |
| 2026-11-03 10:43:23 | [fortytwo-studio/colour-palettes](https://www.nuget.org/packages/fortytwo-studio%2Fcolour-palettes) | 1.0.0 | FortyTwo Studio | Colour palettes with solid colours, gradients and custom attributes. |
| 2026-11-03 10:46:50 | [nakipelo/orchid-2fa](https://www.nuget.org/packages/nakipelo%2Forchid-2fa) | 0.1.0 | nakipelo | Two-factor authentication for the Laravel Orchid admin panel: a one-time code b… |
| 2026-11-03 10:59:13 | [complianty/typo3-connector](https://www.nuget.org/packages/complianty%2Ftypo3-connector) | v0.1.0 | Complianty | Shows the Complianty website scan status, starts scans and outputs the approved… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
