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

## Latest list — 2026-11-12 16:22 UTC

New packages created between 2026-11-12 15:20 UTC and 2026-11-12 16:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-12T16-22-14-327924Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-12 15:28:16 | [iurigustavo/craft-livewire-bridge](https://www.nuget.org/packages/iurigustavo%2Fcraft-livewire-bridge) | 1.0.2 | Iúri Gustavo | Render Craft CMS Blade templates as full-page Livewire 4 components, with Craft… |
| 2026-11-12 15:31:15 | [diego-drese/nfse-nacional](https://www.nuget.org/packages/diego-drese%2Fnfse-nacional) | v0.2.0 | Diego Drese | NFS-e Nacional (Sefin Nacional/ADN) em PHP puro: monta e valida a DPS no leiaut… |
| 2026-11-12 15:32:51 | [silarhi/app-js-bundle](https://www.nuget.org/packages/silarhi%2Fapp-js-bundle) | v0.1.0 | SILARHI | load_page Twig function, TypeScript enums and typed form shapes for Symfony — t… |
| 2026-11-12 16:00:50 | [imarc/craft-padstone-mason](https://www.nuget.org/packages/imarc%2Fcraft-padstone-mason) | 0.1.0 |  | Control-panel assistant for Padstone Content Designer. |
| 2026-11-12 16:00:55 | [imarc/craft-padstone-mason-neo](https://www.nuget.org/packages/imarc%2Fcraft-padstone-mason-neo) | 0.1.0 |  | Neo structure adapter for Padstone Mason (Content Designer via Spicy Web Neo). |
| 2026-11-12 16:05:26 | [nonini/cli](https://www.nuget.org/packages/nonini%2Fcli) | v0.8.0 | Thomas Gelf | CLI utilities |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
