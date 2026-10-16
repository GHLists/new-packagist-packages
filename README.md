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

## Latest list — 2026-10-16 12:21 UTC

New packages created between 2026-10-16 11:22 UTC and 2026-10-16 12:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-16T12-21-25-750193Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-16 11:24:20 | [webchatagent/typo3-webchatagent](https://www.nuget.org/packages/webchatagent%2Ftypo3-webchatagent) | 1.0.0 | WebChatAgent | AI chatbot and live chat for TYPO3: answers visitors from your website content,… |
| 2026-10-16 11:32:18 | [jmonitor/easyadmin-bundle](https://www.nuget.org/packages/jmonitor%2Feasyadmin-bundle) | v1.0.0 | Jonathan Plantey | Live monitoring pages inside EasyAdmin: system, PHP, MySQL, Redis and Symfony m… |
| 2026-10-16 12:05:45 | [shapperize/laravel-activation](https://www.nuget.org/packages/shapperize%2Flaravel-activation) | v0.1.0 | Technologies Shapperize Inc. | Aha-moment activation for Laravel SaaS apps: proof-of-value steps, plan gates,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
