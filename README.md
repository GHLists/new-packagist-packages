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

## Latest list — 2026-10-31 17:20 UTC

New packages created between 2026-10-31 16:18 UTC and 2026-10-31 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-31T17-20-41-174744Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-31 16:51:19 | [bbwdadfg/hospitalbagchecklist-url-tools](https://www.nuget.org/packages/bbwdadfg%2Fhospitalbagchecklist-url-tools) | v0.1.0 | wangneo276-lgtm | A free hospital bag checklist that tracks what you have, what to buy, what’s pa… |
| 2026-10-31 16:53:50 | [ernestdefoe/flarumverse](https://www.nuget.org/packages/ernestdefoe%2Fflarumverse) | 1.0.0 | Ernest Defoe | Flarumverse — Flarum forums pair with each other and show each other's new disc… |
| 2026-10-31 16:59:40 | [crazypartsnatcher/oem-normalizer](https://www.nuget.org/packages/crazypartsnatcher%2Foem-normalizer) | v1.0.2 | CrazyPartSnatcher Engineering | Zero-dependency PHP utility to normalize, validate, and cross-reference commerc… |
| 2026-10-31 17:07:33 | [rem42/sylius-admin-kit-bundle](https://www.nuget.org/packages/rem42%2Fsylius-admin-kit-bundle) | v1.0.0 | Rem42 | Opt-in admin features (quick filter, active filters, environment indicator, ent… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
