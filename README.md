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

## Latest list — 2026-10-06 00:20 UTC

New packages created between 2026-10-05 23:20 UTC and 2026-10-06 00:20 UTC.

[Full CSV](data/new-packagist-packages-2026-10-06T00-20-46-336439Z.csv)

| Created (UTC) | Package | Version | Author | Description |
| :------------ | :------ | :------ | :------ | :----------- |
| 2026-10-05 23:23:49 | [miraiportal/afterglow](https://www.nuget.org/packages/miraiportal%2Fafterglow) | 1.0.0 |  |  |
| 2026-10-05 23:28:38 | [rafalmasiarek/dashboard-kit-addon-mail-tracking](https://www.nuget.org/packages/rafalmasiarek%2Fdashboard-kit-addon-mail-tracking) | v0.1.1 |  | Open-tracking pixel addon for dashboard-kit outgoing email — decorates MailerIn… |
| 2026-10-05 23:29:21 | [rosvit/module-cms-content-sync](https://www.nuget.org/packages/rosvit%2Fmodule-cms-content-sync) | 1.0.0 | Rosvit | Export and import CMS Pages and Blocks between environments as JSON. |
| 2026-10-05 23:37:02 | [contenir/contenir-asset-mezzio](https://www.nuget.org/packages/contenir%2Fcontenir-asset-mezzio) | v2.0.0 |  | Mezzio adapter for Contenir assets — keyed, profile-driven responsive image var… |
| 2026-10-05 23:37:41 | [upturnstudio/module-google-feed](https://www.nuget.org/packages/upturnstudio%2Fmodule-google-feed) | 1.0.0 | Brideo | Google Merchant Center product feeds with configurable attribute mapping, ad-cl… |
| 2026-10-05 23:59:41 | [toreador/flarum-job-queue](https://www.nuget.org/packages/toreador%2Fflarum-job-queue) | v1.0.5 | Toreador | List, inspect, requeue and auto-requeue failed database queue jobs from the Fla… |
| 2026-10-06 00:11:44 | [contenir/contenir-resource-mezzio](https://www.nuget.org/packages/contenir%2Fcontenir-resource-mezzio) | v2.0.0-RC1 |  | Mezzio adapter for contenir/contenir-resource: workflow routing and navigation… |
| 2026-10-06 00:12:08 | [avdeb/qr-php](https://www.nuget.org/packages/avdeb%2Fqr-php) | v0.1.0 | AVDEB | Simple PHP library for generating QR codes. |

## Data source

Data comes from the [Packagist.org API](https://packagist.org/apidoc),
operated by packagist.org. Package metadata is provided by the package
authors. This project is not affiliated with or endorsed by packagist.org or
the Composer project.
