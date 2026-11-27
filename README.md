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

## Latest list — 2026-11-27 16:19 UTC

New packages created between 2026-11-27 15:19 UTC and 2026-11-27 16:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-27T16-19-17-272401Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-27 15:21:30 | [jimbo2150/css-indexed-dom](https://www.nuget.org/packages/jimbo2150%2Fcss-indexed-dom) | v1.0.1 | Jim Robinson | Fast, indexed CSS selector queries over PHP's native Dom\HTMLDocument and Dom\D… |
| 2026-11-27 15:27:11 | [kariricode/sse](https://www.nuget.org/packages/kariricode%2Fsse) | v4.0.0 | Walmir Silva | Server-Sent Events for PHP 8.4 (WHATWG HTML §9.2): immutable events, a wire-for… |
| 2026-11-27 15:41:07 | [infrangible/m2-page-cache-vary-fix](https://www.nuget.org/packages/infrangible%2Fm2-page-cache-vary-fix) | 1.0.0 | Andreas Knollmann | Fixes the built-in full page cache of Magento 2.4.8, which shows logged-in cust… |
| 2026-11-27 15:42:57 | [concept7/statamic-bard-set-clipboard](https://www.nuget.org/packages/concept7%2Fstatamic-bard-set-clipboard) | v1.0.0 | Concept7 | Copy Bard sets from the set menu and paste them with a toolbar button or Cmd/Ct… |
| 2026-11-27 16:08:06 | [filevora/filevora](https://www.nuget.org/packages/filevora%2Ffilevora) | v0.1.0 |  | Headless PHP SDK for resumable uploads, private storage, background derivatives… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
