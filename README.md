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

## Latest list — 2026-10-29 04:20 UTC

New packages created between 2026-10-29 03:21 UTC and 2026-10-29 04:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T04-20-44-682101Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 03:27:31 | [waynestate/sourdough](https://www.nuget.org/packages/waynestate%2Fsourdough) | 0.1.0 | Wayne State University, Enter… | A starter that makes a Wayne State app with the stack already wired in. |
| 2026-10-29 03:27:39 | [waynestate/squire](https://www.nuget.org/packages/waynestate%2Fsquire) | 0.1.0 | Wayne State University, Enter… | The Citadel kit: standard build.sh, release script and health check, and local… |
| 2026-10-29 03:27:46 | [waynestate/rollcall](https://www.nuget.org/packages/waynestate%2Frollcall) | 0.1.0 | Wayne State University, Enter… | WELD's fleet scanner: every app answers present with its PHP image, Laravel and… |
| 2026-10-29 03:28:00 | [waynestate/pinstripe](https://www.nuget.org/packages/waynestate%2Fpinstripe) | 0.1.0 |  | The coding standard for the Wayne State app stack: shared Pint and PHPStan pres… |
| 2026-10-29 03:31:03 | [waynestate/advisor](https://www.nuget.org/packages/waynestate%2Fadvisor) | 0.1.0 | Wayne State University, Enter… | Wayne State's own MCP server: orients a developer and gives their coding agent… |
| 2026-10-29 03:35:53 | [particle-academy/fancy-formula](https://www.nuget.org/packages/particle-academy%2Ffancy-formula) | v0.0.1 | Particle Academy | A deterministic spreadsheet-formula engine with Google Sheets semantics. Formul… |
| 2026-10-29 03:36:05 | [webrteu/shipping](https://www.nuget.org/packages/webrteu%2Fshipping) | v0.1.1 | WeBRTeu | Core shipping abstraction for Romanian couriers in Laravel |
| 2026-10-29 03:36:57 | [ghf/webgeeker-validation](https://www.nuget.org/packages/ghf%2Fwebgeeker-validation) | v0.1.0 | photondragon | Validation for WebGeeker (fork of photondragon/webgeeker-validation, PHP 8.4/8.… |
| 2026-10-29 03:38:46 | [webrteu/payments](https://www.nuget.org/packages/webrteu%2Fpayments) | v0.1.1 | WeBRTeu | Core payments abstraction for Romanian payment processors in Laravel |
| 2026-10-29 03:42:26 | [webrteu/fancourier](https://www.nuget.org/packages/webrteu%2Ffancourier) | v0.1.1 | WeBRTeu | FAN Courier API v2 integration for Laravel (Romania) |
| 2026-10-29 03:42:52 | [webrteu/cargus](https://www.nuget.org/packages/webrteu%2Fcargus) | v0.1.1 | WeBRTeu | Cargus (UrgentOnlineAPI) integration for Laravel (Romania) |
| 2026-10-29 03:43:11 | [webrteu/dpd](https://www.nuget.org/packages/webrteu%2Fdpd) | v0.1.1 | WeBRTeu | DPD Romania API v1 integration for Laravel |
| 2026-10-29 03:43:31 | [webrteu/gls](https://www.nuget.org/packages/webrteu%2Fgls) | v0.1.1 | WeBRTeu | GLS (MyGLS API) integration for Laravel (Romania and CEE) |
| 2026-10-29 03:43:49 | [webrteu/sameday](https://www.nuget.org/packages/webrteu%2Fsameday) | v0.1.1 | WeBRTeu | Sameday Courier and easybox integration for Laravel (Romania) |
| 2026-10-29 03:50:13 | [relaylayerio/laravel-notification](https://www.nuget.org/packages/relaylayerio%2Flaravel-notification) | v0.1.0 |  | Send Laravel notifications through RelayLayer with a secret key. |
| 2026-10-29 03:54:19 | [normann/silverstripe-svg-sanitization](https://www.nuget.org/packages/normann%2Fsilverstripe-svg-sanitization) | 1.0.0 | Normann Lou | Sanitises SVG files in Silverstripe CMS, so an uploaded SVG can't run script or… |
| 2026-10-29 04:09:38 | [webrteu/btipay](https://www.nuget.org/packages/webrteu%2Fbtipay) | v0.1.0 | WeBRTeu | BT iPay (Banca Transilvania) payment integration for Laravel |
| 2026-10-29 04:09:55 | [webrteu/euplatesc](https://www.nuget.org/packages/webrteu%2Feuplatesc) | v0.1.0 | WeBRTeu | EuPlatesc.ro payment integration for Laravel (Romania) |
| 2026-10-29 04:10:08 | [webrteu/librapay](https://www.nuget.org/packages/webrteu%2Flibrapay) | v0.1.0 | WeBRTeu | LibraPay (Libra Internet Bank) payment integration for Laravel (Romania) |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
