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

## Latest list — 2026-11-16 14:20 UTC

New packages created between 2026-11-16 13:19 UTC and 2026-11-16 14:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-16T14-20-36-189024Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-16 13:25:08 | [friendzy/magento-module](https://www.nuget.org/packages/friendzy%2Fmagento-module) | 1.0.1 | SWARMSOFT S.R.L. | Friendzy: shoppers browse your store together, and with your advisers. |
| 2026-11-16 13:42:20 | [dakotajune/normalize](https://www.nuget.org/packages/dakotajune%2Fnormalize) | v1.0.0 |  | An Eloquent cast that normalizes string attributes through Stringable operation… |
| 2026-11-16 13:49:14 | [dakotajune/blueprint_policies](https://www.nuget.org/packages/dakotajune%2Fblueprint_policies) | v1.0.0 |  | First-class authorization policies for Laravel Blueprint: describe who can do w… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
