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

## Latest list — 2026-10-30 22:20 UTC

New packages created between 2026-10-30 21:21 UTC and 2026-10-30 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T22-20-49-712609Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 21:27:45 | [ernestdefoe/quickdraw](https://www.nuget.org/packages/ernestdefoe%2Fquickdraw) | 1.0.4 | Ernest Defoe | Quickdraw — a floating action button for Flarum discussion pages. Reply, follow… |
| 2026-10-30 21:30:42 | [kiwicaptcha/kiwicaptcha-php](https://www.nuget.org/packages/kiwicaptcha%2Fkiwicaptcha-php) | v1.0.1 | Bel Consulting OÜ | KiwiCaptcha: privacy-first, self-hosted proof-of-work anti-abuse engine for PHP… |
| 2026-10-30 21:30:54 | [kiwicaptcha/kiwicaptcha-risk-php](https://www.nuget.org/packages/kiwicaptcha%2Fkiwicaptcha-risk-php) | v1.0.1 | Bel Consulting OÜ | KiwiCaptcha Adaptive Risk Engine for PHP: privacy-first, self-hosted risk scori… |
| 2026-10-30 21:31:14 | [bel-consulting/kiwicaptcha-symfony](https://www.nuget.org/packages/bel-consulting%2Fkiwicaptcha-symfony) | v1.0.1 | Bel Consulting OÜ | Self-contained Symfony bundle for KiwiCaptcha proof-of-work CAPTCHA. No externa… |
| 2026-10-30 21:40:13 | [phpstats/phit-polyfill](https://www.nuget.org/packages/phpstats%2Fphit-polyfill) | v0.1.0 |  | Pure-PHP polyfill for the phit native extension: descriptive statistics, OLS/lo… |
| 2026-10-30 22:09:57 | [timvandendries/clock](https://www.nuget.org/packages/timvandendries%2Fclock) | v1.0.0 | Tim van den Dries | Configurable analog, digital and count-down bar clocks |
| 2026-10-30 22:13:44 | [piotrpress/github-backup](https://www.nuget.org/packages/piotrpress%2Fgithub-backup) | v1.0.0 | Piotr Niewiadomski | CLI tool for bulk downloading GitHub repositories as ZIP archives. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
