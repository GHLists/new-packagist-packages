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

## Latest list — 2026-10-25 22:20 UTC

New packages created between 2026-10-25 21:20 UTC and 2026-10-25 22:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-25T22-20-28-984405Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-25 21:24:22 | [psbits/security-tools](https://www.nuget.org/packages/psbits%2Fsecurity-tools) | 0.1.0-alpha | Daniel Ablass | security tools for TYPO3 extensions |
| 2026-10-25 21:30:28 | [acencyril/fineprint-bundle](https://www.nuget.org/packages/acencyril%2Ffineprint-bundle) | v0.2.0 | Cyril | Legal pages for Symfony sites, assembled from jurisdiction packs (France, EU) a… |
| 2026-10-25 21:36:00 | [stevelacey/ui-avatars](https://www.nuget.org/packages/stevelacey%2Fui-avatars) | 1.0.0 | Steve Lacey | Deterministic avatar URLs: Gravatar photos with a colorful initials fallback. |
| 2026-10-25 22:10:22 | [stablevoy/stablevoy-php](https://www.nuget.org/packages/stablevoy%2Fstablevoy-php) | v1.0.0 |  | PHP client for the Stablevoy API: non-custodial USDT and USDC payments, invoice… |
| 2026-10-25 22:19:13 | [monkeysoftnl/laravel-livewire-shield](https://www.nuget.org/packages/monkeysoftnl%2Flaravel-livewire-shield) | v1.0.0 |  | Turns tampered Livewire payloads into a quiet 403, a log line and a per-address… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
