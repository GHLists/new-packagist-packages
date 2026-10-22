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

## Latest list — 2026-10-22 08:21 UTC

New packages created between 2026-10-22 07:21 UTC and 2026-10-22 08:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-22T08-21-29-835438Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-22 07:26:08 | [electrik/slate-illustrations](https://www.nuget.org/packages/electrik%2Fslate-illustrations) | 0.1.0 | neerajsohal | A collection of animated UI scenes for Electrik Slate landing pages. Looks like… |
| 2026-10-22 07:31:14 | [phpsafe/guard](https://www.nuget.org/packages/phpsafe%2Fguard) | v0.1.0 | PHP Safe | Zero-dependency security layer for PHP: request shield, static code scanner and… |
| 2026-10-22 07:35:52 | [hoangkim28/codeigniter](https://www.nuget.org/packages/hoangkim28%2Fcodeigniter) | v0.1.0 |  | CodeIgniter 3 fork of pocketarc/codeigniter maintained by hoangkim28, with supp… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
