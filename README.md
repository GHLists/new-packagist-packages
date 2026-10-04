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

## Latest list — 2026-10-04 10:21 UTC

New packages created between 2026-10-04 09:22 UTC and 2026-10-04 10:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-04T10-21-32-214126Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-04 09:29:44 | [masterlink/mpesa-dependency](https://www.nuget.org/packages/masterlink%2Fmpesa-dependency) | v1.0.0 | Rafael Munguambe | online payment manager using mpesa gateway |
| 2026-10-04 09:30:23 | [mage2kishan/module-cachemanager](https://www.nuget.org/packages/mage2kishan%2Fmodule-cachemanager) | 1.1.2 | Kishan Savaliya | Smart cache invalidation on entity save and automated cache warmup with concurr… |
| 2026-10-04 09:33:34 | [hipdevteam/ion-mu](https://www.nuget.org/packages/hipdevteam%2Fion-mu) | v3.2.0 | ION | ION MU — WordPress mu-plugin that fire-and-forgets activity events to Site Inte… |
| 2026-10-04 09:35:30 | [harmovich67/ai-translator](https://www.nuget.org/packages/harmovich67%2Fai-translator) | v1.0.0 | harmovich67 | Framework-agnostic translations, inline live editing, full-page Gemini translat… |
| 2026-10-04 09:44:36 | [larawellui/starter-kit](https://www.nuget.org/packages/larawellui%2Fstarter-kit) | v2026.10.0 | Krishnaprasad R | A Laravel starter kit with sign in, registration and settings, built from Laraw… |
| 2026-10-04 10:03:04 | [mage2kishan/module-social-meta](https://www.nuget.org/packages/mage2kishan%2Fmodule-social-meta) | 1.1.4 | Kishan Savaliya | Panth Social Meta — OpenGraph and Twitter Card head tags for Magento 2, with CM… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
