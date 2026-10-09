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

## Latest list — 2026-10-09 10:18 UTC

New packages created between 2026-10-09 09:20 UTC and 2026-10-09 10:18 UTC.

[Full CSV](data/new-packagist-packages-2026-10-09T10-18-45-47013Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-09 09:32:11 | [vadimermolenko8787/scanner-trap](https://www.nuget.org/packages/vadimermolenko8787%2Fscanner-trap) | 0.1.0 | Vadym Yermolenko | Blacklists vulnerability scanners on their first probe of a decoy path such as… |
| 2026-10-09 09:35:41 | [soderlind/ps-last-updated](https://www.nuget.org/packages/soderlind%2Fps-last-updated) | 1.0.0 | Per Soderlind | Adds a sortable Last Updated column to public post type admin lists. |
| 2026-10-09 09:36:41 | [tombroucke/acorn-wpml-livewire-fix](https://www.nuget.org/packages/tombroucke%2Facorn-wpml-livewire-fix) | 1.0.0 | Tom Broucke | Prevents WPML from appending the language path to home_url() when Acorn sets th… |
| 2026-10-09 09:50:55 | [sitepark/oparl-client](https://www.nuget.org/packages/sitepark%2Foparl-client) | 1.0.0 | Felix Becker | Client for OParl 1.0 and 1.1, the standard interface of German council informat… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
