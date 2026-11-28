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

## Latest list — 2026-11-28 11:20 UTC

New packages created between 2026-11-28 10:21 UTC and 2026-11-28 11:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T11-20-29-703339Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 10:48:25 | [mignuti/typo3-trackd-analytics](https://www.nuget.org/packages/mignuti%2Ftypo3-trackd-analytics) | v1.1.2 | Mignuti Media | trackd.one Analytics - Cookieless, privacy-friendly web analytics for TYPO3 (no… |
| 2026-11-28 10:51:27 | [fanzly/whatsapp](https://www.nuget.org/packages/fanzly%2Fwhatsapp) | v1.0.1 | Fanzly SDK | Professional PHP & Laravel package for Fanzly.net WhatsApp Messaging, Campaigns… |
| 2026-11-28 11:10:20 | [sec/ip2location](https://www.nuget.org/packages/sec%2Fip2location) | 1.0.8 | Stefan Eik Christiansen | IP-based CMS content visibility. |
| 2026-11-28 11:16:05 | [carrier/app](https://www.nuget.org/packages/carrier%2Fapp) | v0.2.0 | Helge Sverre | A new bulletin board system on Carrier. |
| 2026-11-28 11:16:05 | [carrier/framework](https://www.nuget.org/packages/carrier%2Fframework) | v0.2.0 | Helge Sverre | A framework for building telnet, SSH and web bulletin board systems, on Tempest… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
