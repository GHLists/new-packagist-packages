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

## Latest list — 2026-10-14 13:21 UTC

New packages created between 2026-10-14 12:21 UTC and 2026-10-14 13:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-14T13-21-31-872014Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-14 12:22:23 | [web-tp3/pdf](https://www.nuget.org/packages/web-tp3%2Fpdf) | 1.0.0 | Thomas Ruta | pdf renderings |
| 2026-10-14 12:37:12 | [patrykgruszka/composer-dist-probe](https://www.nuget.org/packages/patrykgruszka%2Fcomposer-dist-probe) | 0.0.2 |  | Disposable probe: does Packagist honor a dist key in composer.json? Will be del… |
| 2026-10-14 12:47:05 | [pdftoolkit/opentype](https://www.nuget.org/packages/pdftoolkit%2Fopentype) | v0.1.0 | Mathias STRASSER | Explicit OpenType font objects, bounded SFNT reading and glyph substitutions |
| 2026-10-14 12:47:10 | [esigner/sdk](https://www.nuget.org/packages/esigner%2Fsdk) | v0.2.0 |  | Official PHP client for the esigner e-signing API: BankID, MitID and other eID… |
| 2026-10-14 13:00:22 | [sivasakthi/jeephp](https://www.nuget.org/packages/sivasakthi%2Fjeephp) | v1.0.0 |  | A small, readable PHP framework with simple database helpers. |
| 2026-10-14 13:01:36 | [fluidstan/typo3](https://www.nuget.org/packages/fluidstan%2Ftypo3) | 0.1.0 | Sascha Egerer | TYPO3 integration for FluidStan: boots TYPO3, registers its Fluid namespaces an… |
| 2026-10-14 13:03:18 | [hawkforge/laravel-ai-blog](https://www.nuget.org/packages/hawkforge%2Flaravel-ai-blog) | v0.1.0 | Mr Hawk | The AI-native blog for Laravel. Headless by default, SEO built in, AI as your e… |
| 2026-10-14 13:14:06 | [helsingborg-stad/wpmu-allow-sentry-agent](https://www.nuget.org/packages/helsingborg-stad%2Fwpmu-allow-sentry-agent) | 0.1.0 | Thor Brink | Allow connecting to a local Sentry agent. |
| 2026-10-14 13:16:24 | [mykholy/laravel-flowguard](https://www.nuget.org/packages/mykholy%2Flaravel-flowguard) | v0.1.0-beta.1 | Ahmed El-Kholy | Fail-closed Laravel operations with idempotency, reconciliation, durable inbox/… |
| 2026-10-14 13:17:35 | [mohemian/flink-sdk-php](https://www.nuget.org/packages/mohemian%2Fflink-sdk-php) | v0.1.0 |  | Verify FLINK's signed assertions (eID prefill, flow results) in a Laravel backe… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
