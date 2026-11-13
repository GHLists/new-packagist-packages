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

## Latest list — 2026-11-13 11:19 UTC

New packages created between 2026-11-13 10:19 UTC and 2026-11-13 11:19 UTC.

[Full CSV](data/new-packagist-packages-2026-11-13T11-19-20-762885Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-13 10:27:57 | [nonini/diff](https://www.nuget.org/packages/nonini%2Fdiff) | v0.4.0 | Thomas Gelf | php-diff wrapper supporting ipl/html |
| 2026-11-13 10:36:24 | [dusmamud/indycheck](https://www.nuget.org/packages/dusmamud%2Findycheck) | v0.2.4 | dusmamud | PHP FFI binding for indycheck — offline validator for Indian IDs (PAN, Aadhaar,… |
| 2026-11-13 10:38:40 | [nonini/zfdb](https://www.nuget.org/packages/nonini%2Fzfdb) | v0.6.0 |  | Zend_Db from Zend Framework 1. For compatibility reasons only |
| 2026-11-13 10:54:34 | [sigta/ui](https://www.nuget.org/packages/sigta%2Fui) | v0.1.0 | Søren Risbøll Frisk | Sigta UI — Livewire/Blade component library carrying the Sigta brand. Paper, in… |
| 2026-11-13 10:57:51 | [nonini/translation](https://www.nuget.org/packages/nonini%2Ftranslation) | v0.2.0 | Thomas Gelf | Translation helpers |
| 2026-11-13 11:07:56 | [autoheal/laravel-sdk](https://www.nuget.org/packages/autoheal%2Flaravel-sdk) | v0.1.0 |  | Reports exceptions, error logs, deployments, heartbeats and health checks from… |
| 2026-11-13 11:10:25 | [nonini/web](https://www.nuget.org/packages/nonini%2Fweb) | v0.15.0 | Thomas Gelf | Various web widgets |
| 2026-11-13 11:14:00 | [jamalofski/simple-qrcode](https://www.nuget.org/packages/jamalofski%2Fsimple-qrcode) | 4.3.0 | Simple Software LLC; Jamal Ta… | Simple QrCode is a QR code generator made for Laravel. Maintained drop-in repla… |
| 2026-11-13 11:15:27 | [photos-sh/photos](https://www.nuget.org/packages/photos-sh%2Fphotos) | v1.0.0 |  | PHP client for the Photos.sh API: background removal, resizing, upscaling, obje… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
