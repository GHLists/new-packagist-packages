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

## Latest list — 2026-11-04 09:18 UTC

New packages created between 2026-11-04 08:20 UTC and 2026-11-04 09:18 UTC.

[Full CSV](data/new-packagist-packages-2026-11-04T09-18-52-96611Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-11-04 08:46:58 | [yolow92/pagesift](https://www.nuget.org/packages/yolow92%2Fpagesift) | v1.1.0 | YOLOW92 | PHP (ext-ffi) binding of libpagesift: HTML, PDF, Office and other documents to… |
| 2026-11-04 08:48:23 | [amanuellegese/omnipay-arifpay](https://www.nuget.org/packages/amanuellegese%2Fomnipay-arifpay) | v0.1.0 | Amanuel Legese | ArifPay driver for the Omnipay PHP payment processing library |
| 2026-11-04 09:00:59 | [solophp/tokens](https://www.nuget.org/packages/solophp%2Ftokens) | v1.0.0 | Vitaliy Olos | Tokens for reset links, invitations and sessions: random secrets stored only as… |
| 2026-11-04 09:11:05 | [prasanth/form-builder](https://www.nuget.org/packages/prasanth%2Fform-builder) | v1.0.0 | Prasanth Kumar | Dynamic Form Builder Package |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
