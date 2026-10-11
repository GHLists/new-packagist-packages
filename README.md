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

## Latest list — 2026-10-11 17:20 UTC

New packages created between 2026-10-11 16:19 UTC and 2026-10-11 17:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-11T17-20-08-02854Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-11 16:51:23 | [vivutio/operator-pack](https://www.nuget.org/packages/vivutio%2Foperator-pack) | v0.1.0 | Ezekiel Mjema | What a tour operator of vivutio installs: the tours it sells, and the rooms it… |
| 2026-10-11 16:51:23 | [vivutio/supplier-pack](https://www.nuget.org/packages/vivutio%2Fsupplier-pack) | v0.1.0 | Ezekiel Mjema | What a supplier of vivutio installs: the camps, lodges and hotels it runs, and… |
| 2026-10-11 17:09:57 | [tenma/stubs](https://www.nuget.org/packages/tenma%2Fstubs) | 0.1 | Lento Leisenfeld | Stubs of Tenma's PHP API (Tenma::serve(), Tenma\Http, Tenma\Fs, ...) for IDEs a… |
| 2026-10-11 17:11:52 | [alibabacloud/epg-20260715](https://www.nuget.org/packages/alibabacloud%2Fepg-20260715) | 1.0.0 | Alibaba Cloud SDK | Alibaba Cloud EPG (20260715) SDK Library for PHP |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
