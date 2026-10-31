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

## Latest list — 2026-10-31 02:19 UTC

New packages created between 2026-10-31 01:20 UTC and 2026-10-31 02:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T02-19-18-779038Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 01:20:49 | [stellarwp/foundation-view](https://www.nuget.org/packages/stellarwp%2Ffoundation-view) | 2.0.0 |  | Render scoped PHP views to strings with immutable runtime directory selection. |
| 2026-10-31 01:20:57 | [stellarwp/foundation-shutdown](https://www.nuget.org/packages/stellarwp%2Ffoundation-shutdown) | 2.0.0 |  | Run application shutdown tasks once in deterministic priority order. |
| 2026-10-31 01:24:08 | [edulazaro/larachat](https://www.nuget.org/packages/edulazaro%2Flarachat) | 0.1.1 | Edu Lazaro | A website chat for Laravel that a bot answers and you can take over: retrieval… |
| 2026-10-31 01:39:50 | [axisvela/praxo-core](https://www.nuget.org/packages/axisvela%2Fpraxo-core) | v0.1.0 | AxisVela | Embeddable MIT-licensed agent framework for PHP: tools, policy, events, memory,… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
