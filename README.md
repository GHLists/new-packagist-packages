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

## Latest list — 2026-11-20 16:20 UTC

New packages created between 2026-11-20 15:18 UTC and 2026-11-20 16:20 UTC.

[Full CSV](data/new-packagist-packages-2026-11-20T16-20-41-136546Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-20 15:21:48 | [codeverseindia/tourkinet-appstarter](https://www.nuget.org/packages/codeverseindia%2Ftourkinet-appstarter) | v1.0.0 |  | Minimal PHP application starter powered by LightPHP Core |
| 2026-11-20 15:25:46 | [wnikk/qrcode-cute](https://www.nuget.org/packages/wnikk%2Fqrcode-cute) | v1.0.0 |  | QR codes in the shape of a square, circle, triangle or hexagon, as SVG, PNG and… |
| 2026-11-20 15:51:36 | [cengizkemec/flarum-google-news](https://www.nuget.org/packages/cengizkemec%2Fflarum-google-news) | v1.0.0 | Cengiz Kemec | Google News, structured data, sitemap and RSS/Atom integration for Flarum. |
| 2026-11-20 16:07:25 | [xiconfjs/vampire-invoicesuite](https://www.nuget.org/packages/xiconfjs%2Fvampire-invoicesuite) | v1.0.0 | Ralf Fuhrmann | A document validator for horstoeko/invoicesuite that checks e-invoices against… |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
