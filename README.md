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

## Latest list — 2026-10-17 13:20 UTC

New packages created between 2026-10-17 12:19 UTC and 2026-10-17 13:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-17T13-20-43-305006Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-17 12:32:48 | [corvo-technology/corvo-nfse](https://www.nuget.org/packages/corvo-technology%2Fcorvo-nfse) | v0.1.1 | Corvo Technology | PHP SDK for the Corvo NFS-e API: issue Brazilian service invoices, calculate ta… |
| 2026-10-17 12:47:21 | [iso-doss/laravel-meridian](https://www.nuget.org/packages/iso-doss%2Flaravel-meridian) | v1.0.0 | DOSSOU Israël (Iso-Doss) | A Horizon-like dashboard and supervisor for Laravel database queues. |
| 2026-10-17 12:50:41 | [seoultra/open-consent](https://www.nuget.org/packages/seoultra%2Fopen-consent) | v0.2.0 | SEOULTRA | Free, open-source cookie consent: a browser consent engine with real script blo… |
| 2026-10-17 13:04:25 | [kraenzle-ritter/exif-extract](https://www.nuget.org/packages/kraenzle-ritter%2Fexif-extract) | v0.1.0 | Kraenzle & Ritter | Unified PHP interface for extracting technical metadata (EXIF, IPTC, XMP, …) fr… |
| 2026-10-17 13:15:29 | [raqmeyat/webrtc](https://www.nuget.org/packages/raqmeyat%2Fwebrtc) | v0.1.0 | Loai Kanou | WebRTC signaling, call-session lifecycle and ICE/TURN credential service for La… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
