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

## Latest list — 2026-11-20 22:20 UTC

New packages created between 2026-11-20 21:21 UTC and 2026-11-20 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T22-20-18-658901Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 21:26:12 | [aristonis/filament-shortcut-keys](https://www.nuget.org/packages/aristonis%2Ffilament-shortcut-keys) | v1.0.0 | Mekad Alibrahem | Keyboard shortcuts for a Filament panel, assigned automatically from its resour… |
| 2026-11-20 21:29:17 | [otten-it/version-report](https://www.nuget.org/packages/otten-it%2Fversion-report) | v1.0.0 | Otten IT | Lets a monitoring dashboard read which Laravel, PHP and package versions a Lara… |
| 2026-11-20 21:48:13 | [serverfy/sense](https://www.nuget.org/packages/serverfy%2Fsense) | v2.0.0 | Serverfy Core Team | Serverfy Sense - Zero-overhead Deep APM, Waterfall Tracing, Error Tracking and… |
| 2026-11-20 21:50:23 | [reachbell/reachbell](https://www.nuget.org/packages/reachbell%2Freachbell) | v1.0.1 | DotSpheres Technologies Pvt L… | ReachBell server SDK for PHP: transactional push, email, SMS and WhatsApp, even… |
| 2026-11-20 21:59:59 | [instatus/otel](https://www.nuget.org/packages/instatus%2Fotel) | v0.1.0 | Instatus | Errors, logs and traces for PHP on OpenTelemetry, with the Sentry SDK's API. |
| 2026-11-20 22:06:19 | [xihanfun/xihan-framework](https://www.nuget.org/packages/xihanfun%2Fxihan-framework) | v0.2.0-rc.1 | XiHanFun | XiHan Framework SDK for PHP: primitives, manifest, invocation context, pipeline… |
| 2026-11-20 22:06:45 | [koderia-creative-lab/laravel-smslive247](https://www.nuget.org/packages/koderia-creative-lab%2Flaravel-smslive247) | v1.0.0 | Koderia Creative Lab | A modern Laravel client and Notification Channel driver for the SMSLive247 SMS… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
