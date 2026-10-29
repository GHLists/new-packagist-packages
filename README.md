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

## Latest list — 2026-10-29 19:19 UTC

New packages created between 2026-10-29 18:20 UTC and 2026-10-29 19:19 UTC.

[Full CSV](data/new-packagist-packages-2026-10-29T19-19-05-358966Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-29 18:38:56 | [simp/adjustment](https://www.nuget.org/packages/simp%2Fadjustment) | v1.0.0 | Chance Nyasulu | This is library for php that can be used to manage additional changes to order… |
| 2026-10-29 19:07:26 | [ernestdefoe/surveyor](https://www.nuget.org/packages/ernestdefoe%2Fsurveyor) | 1.0.0 | Ernest Defoe | An SEO workspace for Flarum that works alongside FoF SEO, FoF Sitemap and Detou… |
| 2026-10-29 19:14:08 | [ernestdefoe/buzz](https://www.nuget.org/packages/ernestdefoe%2Fbuzz) | 1.0.0 | Ernest Defoe | Buzz — a live activity feed for Flarum. New discussions, replies, members, rank… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
