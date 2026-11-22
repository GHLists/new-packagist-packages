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

## Latest list — 2026-11-22 05:20 UTC

New packages created between 2026-11-22 04:18 UTC and 2026-11-22 05:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-22T05-20-40-298631Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-22 04:32:51 | [datacircle/anthropic-tools](https://www.nuget.org/packages/datacircle%2Fanthropic-tools) | v0.1.0 | Wayne Hamadi | Find the best GTM APIs. Four tools for the tool runner of the Anthropic PHP SDK… |
| 2026-11-22 05:13:54 | [shipwelldev/afterburner](https://www.nuget.org/packages/shipwelldev%2Fafterburner) | v0.1 |  | Publishes Laravel application guidelines, skills, and project rules for coding… |
| 2026-11-22 05:17:44 | [isud/tm](https://www.nuget.org/packages/isud%2Ftm) | 1.0.0 | isud-opensource | 优标宝开放 API PHP SDK：零第三方运行时依赖，基于 cURL，契约驱动 |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
