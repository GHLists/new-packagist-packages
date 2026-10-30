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

## Latest list — 2026-10-30 09:21 UTC

New packages created between 2026-10-30 08:19 UTC and 2026-10-30 09:21 UTC.

[Full CSV](data/new-packagist-packages-2026-10-30T09-21-57-042126Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-30 08:31:14 | [webx-ui/module-orders](https://www.nuget.org/packages/webx-ui%2Fmodule-orders) | v0.90.0 | WebX UI | Orders and the checkout for WebX UI sites: an order is a snapshot of the cart w… |
| 2026-10-30 08:35:27 | [vanta/meminfo](https://www.nuget.org/packages/vanta%2Fmeminfo) | 0.2.0 | Benoit Jacquemont; Vlad Shash… | PHP extension that dumps the content of PHP memory as JSON, to hunt down memory… |
| 2026-10-30 08:36:33 | [snorky22/symfony-api-forge](https://www.nuget.org/packages/snorky22%2Fsymfony-api-forge) | v0.1.0 | snorky22 | Generate Symfony services for REST APIs and webhooks from the API's documentati… |
| 2026-10-30 08:40:52 | [esoboy/ui](https://www.nuget.org/packages/esoboy%2Fui) | v0.1.0 |  | shadcn/ui style component library for Laravel and Livewire. |
| 2026-10-30 08:44:29 | [sebastian/version-requirement](https://www.nuget.org/packages/sebastian%2Fversion-requirement) | 1.0.0 | Sebastian Bergmann | Library for working with version requirements |
| 2026-10-30 09:03:50 | [justbetter/statamic-images](https://www.nuget.org/packages/justbetter%2Fstatamic-images) | 1.0.0 | Bob Wezelman | Responsive picture elements for Statamic assets |
| 2026-10-30 09:14:29 | [hanshs474/fitv-freeimagetovideo](https://www.nuget.org/packages/hanshs474%2Ffitv-freeimagetovideo) | v0.1.0 | hanshs474 | Free image to video AI with no daily cap: your first clip needs no sign-up, the… |
| 2026-10-30 09:19:19 | [carbon/editor-image](https://www.nuget.org/packages/carbon%2Feditor-image) | 0.2.0 |  | Image focal point and map editor for Neos CMS |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
