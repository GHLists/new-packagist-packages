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

## Latest list — 2026-10-29 14:20 UTC

New packages created between 2026-10-29 13:19 UTC and 2026-10-29 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T14-20-10-206062Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 13:21:15 | [dzkit/dzkit-php](https://www.nuget.org/packages/dzkit%2Fdzkit-php) | v0.1.0 | Siroukane | Algerian developer toolkit: CCP/RIP keys, NIF/NIS, phone numbers, licence plate… |
| 2026-10-29 13:22:23 | [atwx/silverstripe-friendlydesk](https://www.nuget.org/packages/atwx%2Fsilverstripe-friendlydesk) | 1.0.0 |  | Select and embed friendlydesk forms in Silverstripe |
| 2026-10-29 13:51:56 | [simp/multiform](https://www.nuget.org/packages/simp%2Fmultiform) | v1.0.0 | Chance Nyasulu | This is php library for build multi steps forms from assoc array |
| 2026-10-29 13:52:55 | [vitexsoftware/digest-modules](https://www.nuget.org/packages/vitexsoftware%2Fdigest-modules) | v1.1.0 | Vítězslav Dvořák | System-agnostic data collection modules for accounting digest reports, Zabbix m… |
| 2026-10-29 13:55:09 | [vitexsoftware/digest-renderer](https://www.nuget.org/packages/vitexsoftware%2Fdigest-renderer) | v1.1.0 | Vítězslav Dvořák | Markdown-first rendering library for accounting digest reports (HTML, PDF) |
| 2026-10-29 14:05:56 | [jiscariot/iblock-element-reader](https://www.nuget.org/packages/jiscariot%2Fiblock-element-reader) | v0.1.0 | JIscariot | Bitrix iblock element reader: load fields and properties from DB with batch res… |
| 2026-10-29 14:13:03 | [jeffersongoncalves/livewire-logs](https://www.nuget.org/packages/jeffersongoncalves%2Flivewire-logs) | 2.0.0 | Jefferson Gonçalves | Log the errors Livewire hides behind a 419 and add component context to Livewir… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
