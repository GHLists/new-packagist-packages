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

## Latest list — 2026-10-09 09:20 UTC

New packages created between 2026-10-09 08:18 UTC and 2026-10-09 09:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T09-20-32-678888Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 08:19:18 | [bibilka/yandex-speechkit-php](https://www.nuget.org/packages/bibilka%2Fyandex-speechkit-php) | v1.0.0 | Igor Sazonov | PHP SDK for Yandex SpeechKit API with Laravel support. Async speech recognition… |
| 2026-10-09 08:26:56 | [wexample/symfony-stage-demo](https://www.nuget.org/packages/wexample%2Fsymfony-stage-demo) | 1.0.1 |  |  |
| 2026-10-09 08:43:50 | [webdados/wp-github-updates](https://www.nuget.org/packages/webdados%2Fwp-github-updates) | 1.0.0 | Webdados | Updates for private or public WordPress plugins and themes from GitHub releases… |
| 2026-10-09 08:48:08 | [mago-assistant/magento2-mago](https://www.nuget.org/packages/mago-assistant%2Fmagento2-mago) | v1.0.0 |  | AI-powered admin assistant for Magento 2. Chat with your store using Anthropic,… |
| 2026-10-09 08:55:08 | [ak279642/laravel-infrastructure](https://www.nuget.org/packages/ak279642%2Flaravel-infrastructure) | v1.4.3 | Avinash Kumar | Production-ready Laravel infrastructure for repositories, safe caching, validat… |
| 2026-10-09 08:56:40 | [dseguy/php-package-visibility](https://www.nuget.org/packages/dseguy%2Fphp-package-visibility) | v0.9.0 | Damien Seguy | Namespace-scoped visibility (private/protected/public) for PHP classes, interfa… |
| 2026-10-09 08:59:56 | [b44x/ksef-php](https://www.nuget.org/packages/b44x%2Fksef-php) | v0.2.0 | Michell Hoduń | Framework-agnostic PHP SDK for the Polish National e-Invoice System (KSeF) API… |
| 2026-10-09 09:06:31 | [thijsdezoete/tinify-statamic](https://www.nuget.org/packages/thijsdezoete%2Ftinify-statamic) | v1.0.0 | Thijs de Zoete | Automatic image optimization, conversion and thumbnails powered by TinyPNG |
| 2026-10-09 09:14:41 | [zfbase/zend1-bootstrap5](https://www.nuget.org/packages/zfbase%2Fzend1-bootstrap5) | v1.0.0 |  | Twitter Bootstrap v.5 Forms for Zend Framework v.1 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
