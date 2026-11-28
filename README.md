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

## Latest list — 2026-11-28 05:22 UTC

New packages created between 2026-11-28 04:19 UTC and 2026-11-28 05:22 UTC.

[Full CSV](data/new-packagist-packages-2026-11-28T05-22-30-542382Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-28 04:46:44 | [firstlightui/custom-tabs](https://www.nuget.org/packages/firstlightui%2Fcustom-tabs) | v1.0.0 |  | Let people choose and reorder the tabs of your NativePHP Mobile app, within the… |
| 2026-11-28 04:50:58 | [agentisend/craft](https://www.nuget.org/packages/agentisend%2Fcraft) | v1.0.0 | AgentiSend | Craft CMS mail adapter that posts each message to POST /emails. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
